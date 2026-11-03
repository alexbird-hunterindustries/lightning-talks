from tools.collate.section import Section


def titled_image(title: str , image: str) -> str:
    return (f"""
        # {title}
        ![bg center 80%]({image})
    """)


introduction_slides = (
    Section()
    .with_auto_animated_slide("""
        # For Sale: Cabin In The Woods
        
        ![bg right ](./images/poor-fit.jpeg)
    """, animate_each_line="""
        - cozy off-grid cabin
        - beautiful mountain view from the deck
        - wood stove

    """)
    .with_auto_animated_slide("""
        # Project: Cabin In The Woods
        
        ![bg right ](./images/poor-fit.jpeg)
    """, animate_each_line="""
        - large concrete pad
        - located to get the best view
        - cedar siding, metal roof
        - wood stove
    """)
    .with_slide("""
        ## What went wrong?
        
        What parts of this picture look off?

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_auto_animated_slide("""
        ## What went wrong?
        
        ![bg right ](./images/poor-fit.jpeg)
    """, animate_each_line="""
        - concrete pad too big
        - concrete pad in wrong place 
        - no time for windows 
    """)
    .with_auto_animated_slide("""
        ## What went wrong?
        
        ![bg right ](./images/poor-fit.jpeg)
    """, animate_each_line="""
        - Product owners: "devs took forever to start"
        - Customers: "...why is it like this??"
        - Devs worked hard, but nobody's happy
    """)
    .with_slide("""
        ## So what happened?
        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        # But first, Hi 👋🏻
        
        I'm Alex Bird  
        Distinguished Software Engineer  
        Hunter Industries  
           
        [mstdn.ca/@alexanderbird](https://mstdn.ca/@alexanderbird)  
        [alexanderbird.software](https://alexanderbird.software)  
        
        ![bg right](./images/alexanderbird.jpg)
    """)
    .with_slide("""
        ![bg fit](./images/feedback-email.png)
    """)
    .with_slide("""
        ## So what happened?
        ![bg right](./images/poor-fit.jpeg)
    """)
    .with_slide(titled_image("Product Owner's Feature List", "./images/PO-feature-list.jpg"))
    .with_slide(titled_image("Product Owner's Expected Burn-Up", "./images/PO-burn-up-dream.png"))
    .with_slide(titled_image("Product Owner's Expected Burn-Up", "./images/PO-burn-up-dream-stress-chart.png"))
    .with_slide("# But...")
    .with_slide(titled_image("Dev Team's Feature List", "./images/dev-team-feature-list.jpg"))
    .with_slide(titled_image("Week 1", "./images/actual-burn-up-1.png"))
    .with_slide(titled_image("Week 2", "./images/week-2-status.png"))
    .with_slide(titled_image("Week 2", "./images/actual-burn-up-2.png"))
    .with_slide(titled_image("Week 3", "./images/week-3-status.png"))
    .with_slide(titled_image("Week 3", "./images/actual-burn-up-3.png"))
    .with_slide(titled_image("Weeks 4-5", "./images/week-5-status.png"))
    .with_slide(titled_image("Weeks 4-5", "./images/actual-burn-up-5.png"))
    .with_slide(titled_image("Last Minute Calendar Invite", "./images/project-checkin-meeting-invite.png"))
    .with_slide(titled_image("Last Minute Calendar Invite", "./images/week-5-status-updated.png"))
    .with_slide(titled_image("Week 6", "./images/week-6-status.png"))
    .with_slide(titled_image("Week 6", "./images/actual-burn-up-6.png"))
    .with_slide(titled_image("Week 7", "./images/week-7-status.png"))
    .with_slide(titled_image("Week 7", "./images/actual-burn-up-7.png"))
    .with_slide("""
        # On Time
        # On Budget
        # 😉
        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide(titled_image("Dev Team's Feature List", "./images/dev-team-feature-list-at-end.png"))
    .with_slide(titled_image("Product Owner's Feature List", "./images/PO-feature-list-at-end.png"))
    .with_auto_animated_slide("""
        # Find Architecture-Product Fit
    """, animate_each_line="""
        - De-stress Stakeholders
        - Delight Customers
        - Reduce Waste
    """)
)