from pathlib import Path

from tools.collate.presentation import Presentation
from _01_introduction_slides import introduction_slides
from _02_slides_to_tie_in_to_the_current_hype import slides_to_tie_in_to_the_current_hype
from _03_section_backlog_shapes import backlog_shapes
from _04_architecture_informed_2d_backlogs import architecture_informed_2d_backlogs
from _05_feature_architecture_hors_doeuvres import feature_architecture_hors_doeuvres
from _06_recap import recap

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
    .with_slides(recap)
    .with_slide("""
        # Thanks for Having Me!
        
        Alex Bird  
        Distinguished Software Engineer  
        Hunter Industries  
           
        [mstdn.ca/@alexanderbird](https://mstdn.ca/@alexanderbird)  
        [alexanderbird.software](https://alexanderbird.software)  
        
        ![bg right](./images/alexanderbird.jpg)
    """)
)


"""

Discuss tradeoff between "what infra to build first" with "what feature does PO want first"
show a user story map with a column on the far right for the architectural slice that accompanies each product slice

each iteration, we get more produce and a more complete infrastructure

Outro: yay iterative incremental dev, yay fast feedback, yay YAGNI / inventory waste



Happy stakeholders, happy customers, happy devs
"""




if __name__ == "__main__":
    presentation.write_markdown_to_file('presentation.md', directory=current_directory)
