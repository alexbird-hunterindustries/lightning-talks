from tools.collate.section import Section

recap = (
    Section()
    .with_animated_slide("""
            # The Essence
        """,
        animations=[
            " - Stakeholders and devs talk",
            "    - marketing goals vs product constraints",
            "    - combined into a better plan",
            " - Build the features that drive the infrastructure",
            "    - Rejig the priorities for visual progress",
            "        - (instead of the dreaded hockey stick)",
            " - Build the infrastructure to support the features",
            "    - Fake it at first"
        ])
    .with_slide("""
        # Wait isn't this just XP?
        
        - Yeah basically
        - This stuff still works!
    """)
)
