from pathlib import Path

from tools.collate.presentation import Presentation
from section_1 import section_1
from section_2 import section_2
from section_3 import section_3

current_directory = Path(__file__).resolve().parent

presentation = (
    Presentation()
    .with_metadata(
        background_image='./images/background.jpg'
    )
    .with_stylesheet(current_directory.parent / 'shared' / 'style.1.0.0.css')
    .with_title(title="Cool", subtitle="Beans")
    .with_slide("""
        # Neat
        ## Nifty

        - lots
        - of
        - stuff
    """)
    .with_section("First point", section_1)
    .with_section("Second point", section_2)
    .with_section("Third point", section_3)
    .with_slide("""
        # Closing Slide
        ## Final Remarks
        
        - neat
    """)
)

if __name__ == "__main__":
    presentation.write_markdown_to_file('presentation.md', directory=current_directory)
