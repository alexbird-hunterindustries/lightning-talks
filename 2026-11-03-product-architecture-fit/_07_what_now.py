from tools.collate.section import Section

what_now = (
    Section()
    .with_auto_animated_slide("""
        # What Now?
    """, animate_each_line="""
        - Devs: take time to understand the code 
        - Devs: take time to keep the code malleable
        - Budget Owners: say yes to unit testing, refactoring
        - Budget Owners: say yes to learning time to get better at ⬆
        - Everyone: talk to each other often
            - Like, just hang out and stuff, you know?
    """)
    .with_auto_animated_slide("""
        # Or Else?
        
        If you don't want to invest in malleable code, embrace
    """, animate_each_line="""
           - big design up front
           - hockey stick status reports
           - stressed stakeholders
           - confused customers
    """)
    .with_auto_animated_slide("""
        # Business Tradeoff
    """, animate_each_line="""
        - Invest in architecture-product fit through iterative development
            - dev skills for malleable code, relationships between eng/product
            - benefit: predictable delivery, happier customers & sales
            - downside: $$$
        - Aim for architecture-product fit through big design up front
            - benefit: no need to learn dev skills for malleable code, OK to keep silos
            - cost: BDUF is expensive and often wrong ($$$)
            - cost: hockey stick status reports, stress, waste ($$$)
    """)
    .with_auto_animated_slide("""
        # Business Tradeoff
    """, animate_each_line="""
        - Invest in architecture-product fit through iterative development
            - people learn, talk to each other
            - $$$
        - Aim for architecture-product fit through big design up front
            - stress and waste
            - $$$
    """)
    .with_auto_animated_slide("""
        # Business Tradeoff
    """, animate_each_line="""
        - Invest in architecture-product fit through iterative development
            - remember to account for the learning cost
        - Aim for architecture-product fit through big design up front
            - it's been half a century, is BDUF working for anyone?
    """)
    .with_auto_animated_slide("""
        # Business Tradeoff
    """, animate_each_line="""
        - Invest in architecture-product fit through iterative development
            - remember to account for the business value of flexibility
        - Aim for architecture-product fit through big design up front
            - if you don't want to rock the boat, BDUF feels safer
    """)
    .with_slide("""
        ![bg center](./images/tradeoffs.gif)
    """)
    .with_slide("""
        If you want to explore the iterative approach,  
        Here are some retro templates
        
        ![bg right ](./images/good-fit.jpeg)
    """)
    .with_auto_animated_slide("""
        # Communication Retro
        ## An idea for a one-off team retro
    """, animate_each_line="""
        - "what devs knew and product didn't"
        - "what product knew and devs didn't"
        - "stuff we built that we didn't need"
        - "stuff we needed that we didn't build"
    """)
    .with_auto_animated_slide("""
        # Communication Retro
        ## An idea for a one-off team retro
        
        Possible action items
    """, animate_each_line="""
        - specific conversations to be had
            - "Sally and Bob should chat about X"
        - process experiments
            - "Next project kickoff, let's try a 2D backlog. Andy's going to facilitate."
        - what else??
            - (have a retro to find out 🙂)
    """)
    .with_auto_animated_slide("""
        # Code Malleability Retro
        ## An idea for a one-off team retro
    """, animate_each_line="""
        - "malleable: code that was easy to change"
        - "ossified: code that was hard to change"
        - "refactored: we learned X, then we changed Y"
        - "disappointed: code we used, wanted to change, but didn't"
    """)
    .with_auto_animated_slide("""
        # Code Malleability Retro
        ## An idea for a one-off team retro
        
        Possible action items
    """, animate_each_line="""
        - cleanup:
            - "we're often working on module X, which is ossified"
            - "Sue and Frank are going to take next week to clean it up, let them know if you have ideas"
    """)
    .with_auto_animated_slide("""
        # Code Malleability Retro
        ## An idea for a one-off team retro
        
        Possible action items
    """, animate_each_line="""
        - learning
            - "We're going to take an hour each morning this month to practice TDD and refactoring"
        - understanding
            - "This month, we're going to allocate time to review all the generated code before pushing it"
    """)
    .with_slide("""
        Quick aside to whoever's facilitating the retro:
        
        If there's no budget to take the actions, don't run the retros -- they'll just be frustrating
    """)
    .with_slide("""
        Aside from the aside:
        
        If there's no budget to take the actions, embrace the stress and hockey stick status updates of BDUF
    """)
)
