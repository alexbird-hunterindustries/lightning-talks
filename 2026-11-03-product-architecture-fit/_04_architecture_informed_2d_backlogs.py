from tools.collate.section import Section

architecture_informed_2d_backlogs = (
    Section()
    .with_slide("""
        # Features as excuse for infra
        
        - devs say "we need a db"
        - play the simplest feature that needs db
        - e.g. when we return to the page tomorrow, data is still there
    """)
    .with_slide("""
        # Just enough infra for the feature
        
        - product says "when we return to the page tomorrow, data is still there"
        - build the simplest infra to support the feature
        - e.g. store data in local storage
    """)
    .with_slide("""
        # Features as excuse for infra
        
        - devs say "we need a db"
        - play the simplest feature that needs db
        - e.g. "when I browse from another device, data is still there"
    """)
    .with_slide("""
        # Just enough infra for the feature
        
        - product says "when I browse from another device, data is still there"
        - build the simplest infra to support the feature
        - e.g. basic db, no auth
    """)
    .with_slide("""
        # Features as excuse for infra
        
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
    .with_auto_animated_slide("""
        #### Architecture-Product Fit
        
        Basically we just need to talk to each other
        
        ![bg right ](./images/good-fit.jpeg)
    """, animate_each_line="""
        - devs to respect PO's business strategy
        - PO's to respect devs' technical advice
        - make a plan together
        - so we have stuff to show early on
    """)
    .with_auto_animated_slide("""
        # The Essence
    """, animate_each_line="""
        - Stakeholders and devs talk
           - marketing/product goals vs technical constraints
           - combined into a better plan
        - Build the features that drive the infrastructure
           - Rejig the priorities for reportable progress
               - (instead of the dreaded hockey stick)
        - Build the infrastructure to support the features
           - Fake it at first
    """)
    .with_slide("""
        # Wait isn't this just XP?
        
        - Yeah basically
        - This stuff still works!
        
        ![bg right fit](./images/xp-explained.jpg)
    """)
    .with_auto_animated_slide("""
        # Wait isn't this just XP?
    """, animate_each_line="""
        - Values: Communication, Simplicity, Feedback, Respect
        - Principles: Baby Steps, Improvement
        - Practices: Whole Team, Stories, Weekly Cycle
        - Practices: Incremental Design, Incremental Deployment, Negotiated Scope Contract
    """)
    .with_slide("""
        # Wait isn't this just XP?
        
        - Yeah basically
        - This stuff still works!
        
        ![bg right fit](./images/xp-explained.jpg)
    """)
)


"""
Contrast the linear graph with the hockey stick. 

observe how the frequent feature delivery reduces stakeholder stress

even if they're not the most important features, it's still visible progress
"""