import streamlit as st

st.sidebar.image("sdslogo.png")

# Add social media links with icons to the sidebar
st.sidebar.markdown("""
    <style>
    .social-icon {
        width: 30px;
        height: 30px;
        margin: 5px;
    }
    .center-icons {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    </style>
    <div class="center-icons">
        <a href="https://www.linkedin.com/company/nussds" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/linkedin.svg" class="social-icon">
        </a>
        <a href="https://www.instagram.com/nus.sds" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/instagram.svg" class="social-icon">
        </a>
        <a href="https://linktr.ee/nussds" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/linktree.svg" class="social-icon">
        </a>
        <a href="https://www.nussds.com" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/internetarchive.svg" class="social-icon">
        </a>
        <a href="https://t.me/nussds" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/telegram.svg" class="social-icon">
        </a>
    </div>
    """, unsafe_allow_html=True)

st.title("Streamlit for Prototyping")
st.markdown("*by NUS Statistics and Data Science Society*")

# Create a button
if st.button('Sign up now!'):
    # Redirect to the desired website
    st.markdown("[Sign up form](https://bit.ly/nussds-streamlit)", unsafe_allow_html=True)


st.markdown("""

Feeling bored over the summer break? NUS SDS has planned the perfect introductory workshop for you!

Discover how to quickly and efficiently transform your data into interactive web applications using Streamlit, a powerful tool designed for data scientists and analysts. Whether you're looking to create stunning data visualizations, build rapid prototypes, or share insights with your team in real-time, this workshop will provide you with hands-on experience and practical knowledge. Perfect for beginners and seasoned professionals alike, our team will guide you through step-by-step tutorials, ensuring you leave with the skills and confidence to leverage Streamlit in your own projects. Don't miss this opportunity to elevate your data presentation and prototyping capabilities!


**Details of workshop:**

Date: 30 May 2024 (Thurs) \n
Time: 7 to 9pm \n
Venue: Zoom

This workshop is also open to students outside NUS! For the relevant fields, please fill your respective faculty (e.g NTU Business or SMU Law) accordingly. A pre-workshop installation guide and the workshop Zoom link will be emailed to all successful registrants prior to the workshop.

See you there on 30 May! For queries on this specific workshop, do contact Harry (@harrychangjr) or Kwang Yang (@kwangyyinc) on Telegram.

**Our links:**

Linktree: https://linktr.ee/nussds

Telegram: https://t.me/nussds

LinkedIn: https://linkedin.com/company/nussds

Instagram: https://instagram.com/nussds

Website: www.nussds.com

""")