from pathlib import Path

from tools.collate.presentation import Presentation
from section_1 import section_1
from section_2 import section_2
from section_3 import section_3
from _01_introduction_slides import introduction_slides
from _02_slides_to_tie_in_to_the_current_hype import slides_to_tie_in_to_the_current_hype

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
    .with_section("First point", section_1)
    .with_section("Second point", section_2)
    .with_section("Third point", section_3)
    .with_slide("""
        # Closing Slide
        ## Final Remarks
        
        - neat
    """)
)


"""
If so, here's what I have:



Title image: A house is half on a concrete pad, half on stilts into mud. The concrete pad is about 10x bigger than it needs to be.





Title: Finding architecture-product fit

Subtitle: De-stress stakeholders, delight customers, and avoid waste with developer-led user story mapping





Intro:

Often, we build parts of our product that nobody needs, we miss parts that folks care deeply about, and our architecture is somehow too much for what we need and also not enough -- like this house, that has a way-too-big concrete pad, but it's not in the right spot so half the house is supported by stilts.
We're going to cover techniques to fit the product to the needs of the user, and the architecture to the needs of the product.
There are three reasons you might care about this:

if you care about stakeholders think, this will avoid the stress-intensifying waiting period while you build out the infrastructure with zero visible progress, saying "trust me, it's necessary". There is another way.
if you care about users, this makes for a product that better meets their needs -- so that when you're stuck in the minutia of a feature, you can still link it back to why it matters personally for some other human
if you care about the budget, this avoids the waste of building product that doesn't sell or architecture that is unnecessary for the product you've built
Before you say "AI", let me ask you if you have yet met a code generator that consistently builds just enough -- not too much, not too little?

No, the scoping is your job, even if you could get all the code for free
We'll be talking about a scoping technique to get you the right product with the right architecture to support it -- no less, no more

Outline:



antipattern: the 1d backlog. Make a list of things to build. "We need all of this". Build it for a few years. Maybe launch, maybe the project gets cancelled. If you launch, there's a bunch of stuff you built that folks don't use.
improvement: 2d backlog -- x axis customer journey, y axis is product owner's triage from abridged MVP to extended director's cut. (classic User Story Mapping). Build all the infra you need, then start with the most important features. Launch after about 4 months. 

The first 2.5 months were infra. Hockey stick graph. Stressed stakeholders.
Overlay stakeholder stress over the hockey stick feature graph -- the longer we go in "infra building mode", the more stressed the stakeholders get
even better: 2d backlog, with infra sliced into the features, so there's visible progress right away. 

Contrast the linear graph with the hockey stick. 

observe how the frequent feature delivery reduces stakeholder stress

even if they're not the most important features, it's still visible progress
Discuss architectural YAGNI

fake the API, fake the db
real API, canned data
real API, real db, hardcoded user info
user info from SSO integration, real API, real db, small scale
big scale data from API to db and back
Discuss tradeoff between "what infra to build first" with "what feature does PO want first"
show a user story map with a column on the far right for the architectural slice that accompanies each product slice

each iteration, we get more produce and a more complete infrastructure

Outro: yay iterative incremental dev, yay fast feedback, yay YAGNI / inventory waste



Happy stakeholders, happy customers, happy devs
"""




if __name__ == "__main__":
    presentation.write_markdown_to_file('presentation.md', directory=current_directory)
