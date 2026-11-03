import textwrap
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List

from tools.collate.section import Section

class IndexSlideBuilder:
    title: str
    items: List[str]

    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        self.items.append(item)

    def set_title(self, title: str):
        self.title = title

    def build(self):
        return IndexSlide(self.title, self.items)

@dataclass
class IndexSlide:
    title: str
    items: List[str]

    def render_for(self, active_item: str):
        lines = [f"# {self.title}", ""]
        past_current_item = False
        for item in self.items:
            if past_current_item:
                lines.append(f" - <span class='deemphasis'>{item}</span>")
            elif item == active_item:
                past_current_item = True
                lines.append(f" - <span class='emphasis'>{item}</span>")
            else:
                lines.append(f" - {item}")
        return "\n".join(lines)

@dataclass
class RenderingContext:
    index: IndexSlide

class Markdown(ABC):
    @abstractmethod
    def render(self, context: RenderingContext) -> str:
        pass

@dataclass
class StaticMarkdown(Markdown):
    markdown: str

    def render(self, context: RenderingContext):
        return self.markdown

@dataclass
class SectionMarkdown(Markdown):
    section_name: str
    slides: List[Markdown]

    def render(self, context: RenderingContext):
        index_markdown = context.index.render_for(self.section_name)
        slides = [index_markdown, *[x.render(context) for x in self.slides]]
        return join_slides(slides)

@dataclass
class MarkdownMetadata(Markdown):
    options: dict

    def render(self, context: RenderingContext) -> str:
        lines = ["---"]
        for key, value in self.options.items():
            lines.append(f"{key}: {value}")
        return "\n".join(lines)

def join_slides(slides: List[str]) -> str:
    return "\n\n---\n\n".join(slides)

class Presentation:
    slides: List[Markdown]
    index_builder: IndexSlideBuilder
    stylesheet: str
    can_add_stylesheet = True

    def __init__(self):
        self.slides = []
        self.stylesheet = ""
        self.index_builder = IndexSlideBuilder()

    def with_metadata(self, background_image: str):
        self.slides.append(MarkdownMetadata({
            "theme": 'gaia',
            "_class": 'lead',
            "paginate": 'true',
            "backgroundColor": '#fff',
            "backgroundImage": f"url('{background_image}')",
            "footer": '',
            "color": '#000',
            "breaks": 'off',
        }))
        return self

    def with_stylesheet(self, stylesheet_path: Path):
        if not self.can_add_stylesheet:
            raise Exception("You must add the stylesheet before adding any content (title, etc.)")

        css_content = Path(stylesheet_path).read_text(encoding='utf-8')
        self.stylesheet = f"<style>\n{css_content}\n</style>"
        return self

    def with_title(self, title: str, subtitle: str = ""):
        self.can_add_stylesheet = False
        self.index_builder.set_title(title)
        self.slides.append(StaticMarkdown(self.stylesheet + textwrap.dedent(f"""
            <div class='title-page'>
            
            # {title}
            ## {subtitle}
            
            </div>
        """)))
        return self

    def with_slide(self, markdown: str):
        self.slides.append(StaticMarkdown(markdown))
        return self

    def with_slides(self, section: Section):
        for slide in section.as_string_slides():
            self.slides.append(StaticMarkdown(slide))
        return self

    def with_section(self, title: str, section: Section):
        self.index_builder.add_item(title)
        self.slides.append(SectionMarkdown(
            section_name=title,
            slides=[StaticMarkdown(x) for x in section.as_string_slides()]
        ))
        return self

    def write_markdown_to_file(self, file_name: str, directory: Path):
        rendering_context = RenderingContext(
            index=self.index_builder.build()
        )
        markdown = self._apply_replacements(join_slides([textwrap.dedent(x.render(rendering_context)) for x in self.slides]))
        target_path = directory / file_name
        target_path.write_text(markdown, encoding='utf-8')

    @staticmethod
    def _apply_replacements(markdown: str):
        return markdown \
            .replace(" -- ", " &mdash; ")