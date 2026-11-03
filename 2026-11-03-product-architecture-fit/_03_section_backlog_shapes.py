from tools.collate.section import Section

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
        # 2D backlog
        
        - Horizontal Axis: Customer Journey
        - Vertical Axis: Priority
    """)
    .with_slide("""
        # User Story Map
        
        TODO: example user story map
        
        talk about journey left right
        
        rank top bottom
    """)
    .with_auto_animated_slide("# How to Rank", animate_each_line="""
        - Product Owners and Devs must collaborate
        - What is possible to build this week?
        - What is worth building this week?
        - What do we need to stitch that together into a complete user journey?
    """)
)