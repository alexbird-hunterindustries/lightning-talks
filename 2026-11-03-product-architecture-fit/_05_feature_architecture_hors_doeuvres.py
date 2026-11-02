from tools.collate.section import Section

feature_architecture_hors_doeuvres = (
    Section()
    .with_slide("""
        # Build features before infra
        
        Here are some patterns for getting a slice of a feature out before having all the infra built
    """)
    .with_slide("""Fake the API -- build frontend-only""")
    .with_slide("""Real API, canned data""")
    .with_slide("""Real API, real db, hardcoded user info""")
    .with_slide("""User info from SSO integration, real API, real db, small scale""")
    .with_slide("""Big scale data from API to db and back""")
)