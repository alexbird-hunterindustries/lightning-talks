from pathlib import Path

from tools.collate.presentation import Presentation
from _01_introduction_slides import introduction_slides
from _02_slides_to_tie_in_to_the_current_hype import slides_to_tie_in_to_the_current_hype
from _03_section_backlog_shapes import backlog_shapes
from _04_architecture_informed_2d_backlogs import architecture_informed_2d_backlogs
from _05_feature_architecture_hors_doeuvres import feature_architecture_hors_doeuvres
from _06_pitfalls import pitfalls
from _07_what_now import what_now
from _08_outro import outro

current_directory = Path(__file__).resolve().parent

presentation = (
    Presentation()
    .with_metadata(
        background_image='./images/watercolour-background.jpg'
    )
    .with_stylesheet(current_directory.parent / 'shared' / 'style.1.0.0.css')
    .with_title(
        title="Find Architecture-Product Fit",
        subtitle="De-stress stakeholders, delight customers, and avoid waste"
    )
    .with_slides(introduction_slides)
    .with_slides(slides_to_tie_in_to_the_current_hype)
    .with_section("Backlog Shapes: 1D, 2D", backlog_shapes)
    .with_section("Architecture-informed 2D Backlogs", architecture_informed_2d_backlogs)
    .with_section("Feature-Architecture Hors D'oeuvres", feature_architecture_hors_doeuvres)
    .with_section("Pitfalls", pitfalls)
    .with_section("Things to Try This Week", what_now)
    .with_slides(outro)
)


if __name__ == "__main__":
    presentation.write_markdown_to_file('presentation.md', directory=current_directory)
