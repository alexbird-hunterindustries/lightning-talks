import textwrap
from typing import List


class Section:
    slides: List[str]
    def __init__(self):
        self.slides = []

    def with_slide(self, markdown: str):
        self.slides.append(textwrap.dedent(markdown))
        return self

    def with_animated_slide(self, title: str, animations: List[str]):
        slide_so_far = textwrap.dedent(title)
        self.slides.append(slide_so_far)
        for appearance in animations:
            slide_so_far += "\n" + appearance
            self.slides.append(slide_so_far)
        return self

    def as_string_slides(self) -> List[str]:
        return self.slides