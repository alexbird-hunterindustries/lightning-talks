from tools.collate.section import Section


def titled_image(title: str , image: str) -> str:
    return ("""
        # {title}
        ![bg center 80%]({image})
    """)


introduction_slides = (
    Section()
    .with_slide("""
        # What went wrong?

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        ## Wait, first
        # What went right?

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        ## Wait, first
        # What went right?
        - we have a cozy cabin!
        - heating works!
        - door locks!

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        # What went wrong?

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        # What went wrong?
        - concrete pad in wrong place
        - concrete pad too big
        - no time for windows

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        # What went wrong?
        - Product owners: "devs took forever to start"
        - Customers: "...why is it like this??"
        - Devs worked hard, but nobody's happy

        ![bg right ](./images/poor-fit.jpeg)
    """)
    .with_slide("""
        # So what happened?
    """)
    .with_slide("""
        # Product Owner's Feature List
        ![bg center 80%](./images/PO-feature-list.jpg)
    """)
    .with_slide("""
        # Dev Team's Feature List
        ![bg center 80%](./images/dev-team-feature-list.jpg)
    """)
    .with_slide("""
        # Product Owner's Expected Burn-Up
        ![bg center 80%](./images/PO-burn-up-dream.png)
    """)
    .with_slide(titled_image("Week 1", "./images/week-1-status.png"))
    .with_slide(titled_image("Week 1", "./images/actual-burn-up-1.png"))
    .with_slide(titled_image("Week 2", "./images/actual-burn-up-3.png"))
    .with_slide(titled_image("Week 3", "./images/actual-burn-up-4.png"))
    .with_slide(titled_image("Weeks 4-5", "./images/actual-burn-up-5.png"))
    .with_slide(titled_image("Weeks 4-5", "./images/week-3-status.png"))
    .with_slide(titled_image("Week 6", "./images/actual-burn-up-6.png"))
    .with_slide(titled_image("Week 5", "./images/week-6-status.png"))
    .with_slide(titled_image("Last Minute Calendar Invite", "./images/project-checkin-meeting-invite.png"))
    .with_slide(titled_image("Week 5", "./images/week-6-status-updated.png"))
    .with_slide(titled_image("Week 7", "./images/actual-burn-up-7.png"))
    # Here's what the product owners imagined
    # Wait we need a concrete pad to build on?
    # Here's what actually happened
    # The dreaded hockey stick
    # Problems:
    #   1. stressed stakeholders: the project "started" but we had no features for ages
    #   2. why did we build such a stupidly large concrete pad?? (db, kubernetes cluster, serverless deploy pipeline, etc.)
    #   3. shoot, no time for windows or other stuff. Just frame it, finish it, and install the wood stove
    #   4. cabin built, on time and on budget!
    # - stressed stakeholders, customers not quite delighted (although they're glad for the cabin), and waste of concrete pad
)