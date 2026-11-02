import textwrap
from typing import List


class Section:
    slides: List[str]
    def __init__(self):
        self.slides = []

    def with_slide(self, markdown: str):
        self.slides.append(textwrap.dedent(markdown))
        return self

    def as_string_slides(self) -> List[str]:
        return self.slides