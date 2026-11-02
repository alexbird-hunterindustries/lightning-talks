from tools.collate.section import Section


slides_to_tie_in_to_the_current_hype = (
    Section()
    .with_slide("""
        # "But can't AI just...?"
    """)
    .with_animated_slide(
        title="""
            # "But can't AI just...?"
        """,
        animations=[
            "- oops you built the wrong thing",
            "  - nobody wants it",
            "- oops you overengineered it",
            "  - it's too expensive to run",
            "- oops the bot did exactly what was asked",
            "  - but everyone hates it"
       ]
    )
    .with_animated_slide(
        title="""
            # "But can't AI just...?"
            
            The faster you go, the more important your direction
        """,
        animations=[
            "- Walking? Adjust as you go",
            "- Launching a rocket? Point it carefully"
       ]
    )
    .with_slide("""
        # "But can't AI just...?"
        
        What is the next most important thing to build?
    """)
    .with_animated_slide("""
        ### "But doesn't rapid prototyping answer...?"
        
        Yes, but it's our job to aim the machine
    """, animations=[
        " - Someone has to evaluate the experiments",
        " - Each experiment has a cost",
        " - So what shall we prototype next?"
    ])
    .with_slide("""
        # Someone has to aim the machine
        
        How do we aim the machine well?
        
        That's what we're talking about today
    """)
    .with_animated_slide("""
        # Today we're talking about how to:
    """, animations=[
        "- Build the right product",
        "- Build the right infrastructure",
        "- Make sure the two match",
    ])
    .with_slide("""
        # Find Architecture-Product Fit
        
        - De-stress Stakeholders
        - Delight Customers
        - Reduce Waste
        
        ![bg right ](./images/poor-fit.jpeg)
    """)
)