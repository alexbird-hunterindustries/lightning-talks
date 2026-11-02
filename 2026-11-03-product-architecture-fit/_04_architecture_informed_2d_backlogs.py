from tools.collate.section import Section

architecture_informed_2d_backlogs = (
    Section()
    .with_slide("""
        # Build the features that drive the infra
        
        - devs say "we need a db"
        - play the simplest feature that needs db
        - e.g. when we return to the page tomorrow, data is still there
    """)
    .with_slide("""
        # Build the infra to support the feature
        
        - product says "when we return to the page tomorrow, data is still there"
        - build the simplest infra to support the feature
        - e.g. store data in local storage
    """)
    .with_slide("""
        # Build the features that drive the infra
        
        - devs say "we need a db"
        - play the simplest feature that needs db
        - e.g. "when I browser from another device, data is still there"
    """)
    .with_slide("""
        # Build the infra to support the feature
        
        - product says "when I browser from another device, data is still there"
        - build the simplest infra to support the feature
        - e.g. basic db, no auth
    """)
    .with_slide("""
        # Build the features that drive the infra
        
        - devs say "we need authentication"
        - play the simplest feature that needs db
        - e.g. "when I browse from user B's account, I can't see user A's data"
    """)
    .with_slide("# And so on")
    .with_slide("""
        # Why
        
        - de-stress stakeholders
        - delight customers 
        - reduce waste
    """)
    .with_slide("""
        # 1D backlogs make waste
        
        - we have to build a bunch of infra for our first feature
        - we have to build a bunch of features for the first user journey
    """)
    .with_slide("""
        # 1D backlogs make stress
        
        - we have nothing to report while we're building infra
        - the demos make no sense when the features are disjointed
    """)
    .with_slide("""
        # 1D backlogs make waste
        
        - we build too much infra
        - we build too many features
    """)
    .with_slide("""
        # 1D backlogs make customers sad
        
        - why can't I....????
        - why is it so.....????
    """)
    .with_slide("""
        # Architecture-Product Fit
        
        Basically we just need to talk to each other

        ![bg right ](./images/good-fit.jpeg)
    """)
)


"""
Contrast the linear graph with the hockey stick. 

observe how the frequent feature delivery reduces stakeholder stress

even if they're not the most important features, it's still visible progress
"""