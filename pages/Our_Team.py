import streamlit as st
from PIL import Image

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

st.header("Our Team")

st.markdown("Introducing our presenters for the workshop!")

harry = Image.open("harry.jpeg")
ky = Image.open("kwangyang.jpeg")
kaushik = Image.open("kaushik.jpg")
kaiser = Image.open("kaiser.png")
gordon = Image.open("gordon.png")
roydon = Image.open("roydon.jpg")

profiles = [
    {
        "name": "Harry Chang",
        "year": "Year 4, Data Science and Analytics",
        "experience": [
            "Data Analyst Intern, Decathlon",
            "Data Science Intern, Groundup.ai",
            "Co-Founder & President, NUS Product Club",
            "President & Marketing Director, NUS SDS"
        ],
        "image": harry
    },
    {
        "name": "Chia Kwang Yang",
        "year": "Year 2, Data Science and Analytics",
        "experience": [
            "Software Engineer Intern, AgentScale AI",
            "Software Engineer Intern, Applied Angstrom Technology",
            "Workshops Director, NUS SDS",
            "Student Lead, NUS Raffles Hall Developers"
        ],
        "image": ky
    },
    {
        "name": "Kaushik Rangaraj",
        "year": "Year 4, Information Systems",
        "experience": [
            "Data Science Intern, Univers",
            "Data Analyst Intern, TES",
            "Business Intelligence Analyst Intern, Shopee",
            "Sports Director, NUS Students' Computing Club"
        ],
        "image": kaushik
    },
    {
        "name": "Kaiser Cheng",
        "year": "Year 2, Data Science and Analytics",
        "experience": [
            "Product Intern, AgentScale AI",
            "Product Intern, Streaminc",
            "Event Director, AIESEC in NUS"
        ],
        "image": kaiser
    },
    {
        "name": "Gordon Tham",
        "year": "Graduate, Data Science and Analytics",
        "experience": [
            "Machine Learning Engineer, Singtel",
            "Regional Analyst Intern, Sephora",
            "Data Science Intern, Grab",
            "Data Science Intern, ESGenie"
        ],
        "image": gordon
    },
    {
        "name": "Roydon Tay",
        "year": "Year 1, Data Science and Analytics",
        "experience": [
            "Data Science Intern, PSA BDP",
            "Research Intern, A*STAR",
            "Workshops Executive, NUS SDS"
        ],
        "image": roydon
    }
]

for profile in profiles:
    with st.container():
        image_column, blank_column, text_column = st.columns((1.5, 0.3, 5))
        with image_column:
            st.image(profile["image"])
        with blank_column:
            st.empty()
        with text_column:
            st.subheader(profile["name"])
            st.write(f"*{profile['year']}*")
            st.markdown("\n".join([f"- {exp}" for exp in profile["experience"]]))