from tools.collate.section import Section
from tools.collate.formatting import bottom_image

backlog_shapes = (
    Section()
    .with_slide("""
        # 1D backlog
        
        - List the stuff
    """)
    .with_animated_slide("""
        # If the devs get to rank the list
    """, animations=[
        '- Long gaps of invisible "backend work" 🏒',
        '- Technically related items grouped together',
        '    - Lots of features built, but no end-to-end customer experience',
        '- No cohesive product until the end',
    ])
    .with_animated_slide("""
        # If the POs get to rank the list
    """, animations=[
        '- Highest priority feature takes forever 🏒',
        '    - The devs end up doing lots of invisible "backend work" anyway',
        '- No cohesive product until the end'
    ])
    .with_slide("""
        # Book: User Story Mapping
        ## Discover the Whole Story, Build the Right Product
        
        *By* Jeff Patton
        ![bg right fit](./images/user-story-mapping-book.jpg)
    """)
    .with_auto_animated_slide("""
        # 2D backlog
        
        ![bg right fit](./images/user-story-mapping-book.jpg)
    """, animate_each_line="""
        - Horizontal Axis: Customer Journey
        - Vertical Axis: Priority or sequence
    """)
    .with_slide(f"""
        # User Story Map
        ## For a note-taking web app
        
        {bottom_image("./images/story-map-unsorted.png")}
    """)
    .with_auto_animated_slide("# How to Rank", animate_each_line="""
        - Product Owners and Devs must collaborate
        - What is possible to build this week?
        - What is worth building this week?
        - What do we need to stitch that together into a complete user journey?
    """)
    .with_slide(f"""
        # User Story Map
        ## Slice 1
        
        {bottom_image("./images/story-map-slice-1.png")}
    """)
    .with_slide(f"""
        # User Story Map
        ## Slice 2
        
        {bottom_image("./images/story-map-slice-2a.png")}
    """)
    .with_slide(f"""
        # User Story Map
        ## Slice 2 (Alternative)
        
        {bottom_image("./images/story-map-slice-2b.png")}
    """)
    .with_slide(f"""
        # User Story Map
        ## Slice 3
        
        {bottom_image("./images/story-map-slice-3.png")}
    """)
    .with_slide(f"""
        # User Story Map
        ## Slice 4: "backend work"
        
        {bottom_image("./images/story-map-slice-4.png")}
    """)
    .with_auto_animated_slide("""
        # Find Architecture-Product Fit
    """, animate_each_line="""
        - Our 2D backlog puts features in user context
        - We choose valuable features that give an excuse for infra
        - We build just enough infra to build valuable features
        - Delivered features earns trust
        - We spend trust on "backend work" -- on infra work
    """)
    .with_slide(f"""
        # User Story Map
        ## Status Reporting
        
        {bottom_image("./images/story-map-with-status-info.png")}
    """)
    .with_auto_animated_slide("""
        # Status Reporting
    """, animate_each_line="""
        - Whenever possible, the "work ticket" has a feature name
        - We do the infra work as part of the feature ticket
        - Benefit: devs have feature context for infra (avoid giant concrete pad)
        - Benefit: we report progress on features (even if it's lots of infra)
    """)
    .with_auto_animated_slide("""
        ### Find Architecture-Product Fit
        
        ![bg right ](./images/good-fit.jpeg)
    """, animate_each_line="""
        - Whenever possible, the "work ticket" has a feature name
        - 2D backlog for context
        - features as excuse for infra
        - just enough infra for features
        - features earn trust for infra 
        - report infra by the feature it enables
    """)
)
