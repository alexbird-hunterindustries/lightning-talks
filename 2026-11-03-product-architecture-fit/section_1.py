from tools.collate.section import Section

section_1 = (
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