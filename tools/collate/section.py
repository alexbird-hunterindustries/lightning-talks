import re
import textwrap
from typing import List


class Section:
    slides: List[str]

    def __init__(self):
        self.entirely_non_alphanumeric_bullet = re.compile("^ *- [^a-zA-Z0-9]*$")
        self.slides = []

    def with_slide(self, markdown: str):
        self.slides.append(textwrap.dedent(markdown))
        return self

    def with_auto_animated_slide(self, title: str, animate_each_line: str):
        each_line = textwrap.dedent(animate_each_line).split('\n')
        return self.with_animated_slide(title, [x for x in each_line if x.strip()])

    def with_animated_slide(self, title: str, animations: List[str]):
        slide_so_far = textwrap.dedent(title)
        self.slides.append(slide_so_far)
        for appearance in animations:
            slide_so_far += "\n" + self._sanitize(appearance)
            self.slides.append(slide_so_far)
        return self

    def as_string_slides(self) -> List[str]:
        return self.slides

    def _sanitize(self, text: str):
        if self.entirely_non_alphanumeric_bullet.match(text):
            return text.replace("- ", "- <span>") + "</span>"
        return text