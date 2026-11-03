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
        # What if we don't?
        
        If you don't want to invest in malleable code, embrace:
    """, animate_each_line="""
           - big design up front
           - hockey stick status reports
           - stressed stakeholders
           - confused customers
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Costs
        
        - Iterative development
            - <span></span>
            - <span></span>
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Costs
        
        - Iterative development
            - cost: dev skills for malleable code
            - cost: fostering relationships between eng/product
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Costs
        
        - Iterative development
            - cost: dev skills for malleable code
            - cost: fostering relationships between eng/product
        - Big design up front
            - if you get everything correct from the start, it's cheaper
            - cost: when do we ever get everything correct from the start?
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Benefits
        
        - Iterative development
            - <span></span>
            - <span></span>
            - <span></span>
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Benefits
        
        - Iterative development
            - benefit: predictable delivery
            - benefit: lower stress (linear progress vs hockey stick)
            - benefit: can respond quickly to change in business landscape
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        ## Two paths to architecture-product fit
        ### Benefits
        
        - Iterative development
            - benefit: predictable delivery
            - benefit: lower stress (linear progress vs hockey stick)
            - benefit: can respond quickly to change in business landscape
        - Big design up front
            - benefit: doesn't rock the boat
            - benefit: feels safer
    """)
    .with_slide("""
        # Business tradeoff
        
        - Iterative development
            - <span></span>
            - <span></span>
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        # Business tradeoff
        
        - Iterative development
            - pay for learning and collaboration
            - earn from predictable, reliable, flexible delivery
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        # Business tradeoff
        
        - Iterative development
            - pay for learning and collaboration
            - earn from predictable, reliable, flexible delivery
        - Big design up front
            - pay for rework when the plan goes wrong
            - enjoy the tradition and simplicity of silos and handoffs
    """)
    .with_slide("""
        # Personal tradeoff
        
        - Iterative development
            - <span></span>
            - <span></span>
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        # Personal tradeoff
        
        - Iterative development
            - rock the boat
            - more satisfying work outcomes
        - Big design up front
            - <span></span>
            - <span></span>
    """)
    .with_slide("""
        # Personal tradeoff
        
        - Iterative development
            - rock the boat
            - more satisfying work outcomes
        - Big design up front
            - a sense of control
            - no need to be a change agent
    """)
    .with_slide("""
        ![bg center](./images/tradeoffs.gif)
    """)
    .with_slide("""
        ## If you want an iterative approach
        
        ![bg right ](./images/good-fit.jpeg)
    """)
    .with_slide("""
        ## Here are some retro templates
         
        to try 2D backlogs and collaborative, iterative dev
        
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
        # Quick aside
        
        - No budget for retro actions?
            - Skip the retro
        - No budget for learning to make malleable code and collaborate?
            - Embrace Big Design Up Front
    """)
)
