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

st.header("Frequently Asked Questions")

st.subheader("#1: What will I learn from this workshop?")

st.markdown("In this workshop, discover how to quickly and efficiently transform your data into interactive web applications using Streamlit, a powerful tool designed for data scientists and analysts. Whether you're looking to create stunning data visualizations, build rapid prototypes, or share insights with your team in real-time, this workshop is suitable for both beginners and seasoned professionals looking to build their own personal or industry-level projects.")

st.subheader("#2: Is this workshop open to NUS students only?")

st.markdown("As this workshop will only be on Zoom, we also welcome students from other universities to sign up for our workshop! Do fill in your respective faculty/major (e.g NTU Business or SMU Law) accordingly in our sign up form.")

st.subheader("#3: Will this virtual workshop be recorded?")

st.markdown("As we understand that students may want to review this workshop at their own time, this workshop will be recorded. The recording, however, will only be accessible to those who sign up for this workshop as this will only be disseminated via email.")

st.subheader("#4: Are there any pre-requisites for this workshop?")

st.markdown("It would be good if participants have prior basic knowledge in Python, version control with Git as well as using code editors such as Visual Studio Code. Otherwise, our team will cover these in a pre-workshop guide which will be emailed to all participants before the workshop. For late signups, we will also be disseminating this guide during the workshop itself.")

st.subheader("#5: Is this a collaboration with NUS Product Club?")

st.markdown("Although this is an extension of our Product Analytics with Tableau workshop conducted with NUS Product Club earlier in Semester 2, this workshop will be held under the purview of NUS SDS only. This workshop will be slightly more technical with coding involved, but we will try our best to ensure to make this beginner-friendly for students from all backgrounds. ")


