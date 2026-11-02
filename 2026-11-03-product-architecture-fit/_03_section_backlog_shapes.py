from tools.collate.section import Section

backlog_shapes = (
    Section()
    .with_slide("""
        # Cool Cats

        - the first
        - the second
        - the third
    """)
    .with_slide("""
        # Eat My Shorts
        
        - now
        - later
        - or never
    """)
)
"""

antipattern: the 1d backlog. Make a list of things to build. "We need all of this". Build it for a few years. Maybe launch, maybe the project gets cancelled. If you launch, there's a bunch of stuff you built that folks don't use.
improvement: 2d backlog -- x axis customer journey, y axis is product owner's triage from abridged MVP to extended director's cut. (classic User Story Mapping). Build all the infra you need, then start with the most important features. Launch after about 4 months. 

The first 2.5 months were infra. Hockey stick graph. Stressed stakeholders.
Overlay stakeholder stress over the hockey stick feature graph -- the longer we go in "infra building mode", the more stressed the stakeholders get
even better: 2d backlog, with infra sliced into the features, so there's visible progress right away. 

Contrast the linear graph with the hockey stick. 

observe how the frequent feature delivery reduces stakeholder stress

even if they're not the most important features, it's still visible progress
"""