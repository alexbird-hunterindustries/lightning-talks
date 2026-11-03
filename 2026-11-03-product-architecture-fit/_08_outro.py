from tools.collate.section import Section

contact_info_slide = """
    # Thanks for Having Me!
    
    Alex Bird  
    Distinguished Software Engineer  
    Hunter Industries  
       
    [mstdn.ca/@alexanderbird](https://mstdn.ca/@alexanderbird)  
    [alexanderbird.software](https://alexanderbird.software)  
    
    ![bg right](./images/alexanderbird.jpg)
"""
outro = (
    Section()
    .with_auto_animated_slide(
    """
        # Final Thoughts
        
        ![bg right ](./images/good-fit.jpeg)
    """, animate_each_line="""
        - Rank your tasks with dev and product together
        - Build features that give an excuse to do infra work
        - Do just enough infra work to build the features
        - Invest in malleable code
        - Happy stakeholders, happy customers, happy devs!
    """)
    .with_slide(contact_info_slide)
    .with_slide("""
        ![bg fit](./images/feedback-email.png)
    """)
    .with_slide(contact_info_slide)
)
