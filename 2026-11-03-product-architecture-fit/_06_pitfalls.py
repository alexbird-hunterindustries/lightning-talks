from tools.collate.section import Section

pitfalls = (
    Section()
    .with_auto_animated_slide("""
        # Prerequisite: malleable code
    """, animate_each_line="""
        - Refactoring
        - Unit Testing
        - Understanding the code
    """)
    .with_slide("""
        # Example: Hardcoded Feature Flagging
        
        So we could release the feature
    """)
    .with_slide("""
        # Example: Hardcoded Algorithm
        
        So we could share the API
    """)
)
