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

st.header("Background")

st.markdown("_In this section, discover the key aspects that drive the motivation behind our upcoming workshop._")

selected_options = ["Overview", "Product Analytics with Tableau Workshop", "Streamlit for Prototyping Article", "Some Samples"]
selected = st.selectbox("Which section would you like to read?", options = selected_options)
st.write("Current selection:", selected)
if selected == "Overview":
    st.subheader("Overview")
    st.write("""
    
    As an extension of our Product Analytics with Tableau workshop, this workshop explores the more techincal side of things - utilising Streamlit, one of the most well-used libraries in Python when dashboarding on building prototypes for web applications.

    For this workshop, we have assembled a makeshift team of data enthusiasts, including a full-time Machine Learning Engineer to conduct this workshop, hopefully spreading the word on how this easy-to-use framework can be used in a wide variety of technical projects.
    
    The other sections within this page have been set up to provide more context, hopefully allowing the reader to be more well-versed with the framework and methodologies required before attending our workshop.

    """)
elif selected == "Product Analytics with Tableau Workshop":
    st.subheader("Event Recap: Product Analytics with Tableau")
    st.write("21 May 2024 | [Article](https://www.nusproductclub.com/blog/product-analytics-with-tableau) by Lim Jing Yun")
    st.markdown("""
        In late February this year, we collaborated with NUS Statistics and Data Science Society to host a workshop on Product Analytics. During the workshop, we covered the what’s, why’s and how’s of analytics, and the basics of Tableau. This is what went down.
        
        **Introduction to Product Analytics**""")
    st.image("1.png")

    st.markdown("""
        We started off by introducing the participants to the basics of product management and analytics. Concepts such as the product life cycle, optimisation and user experience were introduced. With case studies such as Spotify and Netflix, we also briefly explained how these companies made use of product analytics to improve and grow their businesses.

        **Key Concepts and Techniques**

        Next, we went over some key techniques used in the analytics process, with a particular focus on the AARRR framework - acquisition, activation, retention, revenue and referral. Also covered in PM1101E, these “pirate or funnel metrics” are widely used by PMs, marketers and growth hackers alike to further understand the user behaviour of digital products such as mobile and web applications.

        With regards to the AARRR framework, we also discussed some real life case studies like Grammarly, so that participants can better understand the significance of product analytics. For instance, Grammarly uses trends, badges and personal records to engage their existing customers, ensuring the retention metric is well-met when it comes to using the AARRR funnel to optimise their user base and sales.""")

    st.image("2.png")

    st.markdown("""
        **Overview of Analytics Tools**
        
        We then introduced the participants to some of the most common industry tools for analytics, such as Python, Google Analytics and Power BI.

        In terms of programming languages, many product managers and analysts alike would stick to your typical tools including R, Python and SQL. The latter two in particular, are widely used in the industry, with Python offering easy-to-use libraries such as Pandas for data wrangling, as well as Matplotlib or Seaborn for data visualisation. SQL is also an essential tool for querying a database, especially when required to filter out the data you need for your use case from a huge data lake or data warehouse.

        External tools such as Google Analytics and Mixpanel are also used widely as no-code complementary tools, especially when there is a need to track specific metrics such as page views and individual user tracking.

        **Creating Dashboards with Tableau**
        
        Lastly, we had a hands-on session with Tableau. Following the live demo by Nicholas from SDS and with the facilitation of Henry and Harry from Product Club, our participants made use of the provided dataset to create a dashboard.""")

    st.image("3.png")

    st.markdown("""
        In addition, as part of the analytics process, they learnt to plot various visualisations - including treemaps and area charts as an alternative to your typical bar and line charts, geographical maps as well as cohort analysis to measure the gradual retention rates by specific time periods - either by quarter or month. Below is the end result of the dashboard created consisting of the above-mentioned charts after compiling them together!""")

    st.image("4.png")    

    st.markdown("""
        Thank you to NUS SDS for working with us to conduct this product analytics workshop! If you’re keen to attend future workshops and events on product management-related topics, be sure to keep up with our [Instagram](https://instagram.com/nusproductclub) and [Telegram channel](https://t.me/nuspc).""")

    st.image("5.png")

    st.markdown("""
        _Enjoyed our article on our Product Analytics with Tableau workshop? As an extension of this workshop, NUS SDS will be organising a similar Streamlit for Prototyping workshop - led by Harry. Sign up here today: https://bit.ly/nussds-streamlit_
        """)
elif selected == "Streamlit for Prototyping Article":
    st.subheader("Article: Streamlit for Prototyping")
    st.write("4 April 2024 | [Article](https://www.nusproductclub.com/blog/streamlit-for-prototyping) by Harry Chang")
    st.markdown("""
    _Primarily used for data science and analytics, the Streamlit framework based in Python has seen a recent surge in its usage by product analysts, data scientists and even webpage enthusiasts alike. Harry shares more about its growing popularity, particularly as a baseline prototyping tool before building a full-stack product, as well as his personal experiences with it through his past hackathons._

    **Introduction: What is Streamlit?**

    Streamlit is a versatile Python library widely used in the fields of data science and analytics, akin to R's Shiny and Python's Plotly, Dash, or Flask. It stands out for its ability to swiftly create user-friendly dashboards for web applications. Beyond its primary application, Streamlit's adaptability makes it an excellent tool for hackathon participants seeking to rapidly prototype low-fidelity versions of full-stack web products, including those based on technologies like React and Next.js. An added benefit is its seamless integration with the OpenAI API, making it a popular choice for incorporating ChatGPT into web applications to test product concepts.

    **So, how exactly is Streamlit used for prototyping?**

    Streamlit is particularly suited for prototyping due to its unique blend of simplicity, flexibility, and rapid development capabilities. Here's how Streamlit facilitates the prototyping process:

    - Ease of Use: With a simple API, Streamlit allows developers to turn data scripts into shareable web apps with minimal code.

    - Interactive Widgets: Without the need for a callback, interactive widgets like sliders, buttons, and text inputs can be easily integrated.

    - Custom Components: Extend functionality with custom components, or integrate existing React components to create rich, interactive applications.

    - Hot-Reloading: Streamlit's development server automatically detects changes in the script and refreshes the app, making iterative development fast and responsive.

    - Seamless Data Integration: Connect easily to databases, cloud services, and APIs, including the OpenAI API for incorporating AI and machine learning models.

    Streamlit's combination of ease of use, interactivity without complexity, real-time updates, ease of sharing, versatility, and the ability to incorporate custom components makes it an ideal tool for prototyping web applications. It allows teams to quickly move from idea to prototype, enabling fast iteration based on user feedback and significantly shortening the development cycle.

    To learn more about Streamlit's suite of features, widgets and extensions, click [here](https://docs.streamlit.io/develop/api-reference) to find out more!

    **Streamlit and its Alternatives**

    Streamlit has carved a niche for itself as a preferred tool for data scientists and developers looking to deploy interactive data applications quickly. While it shines in ease of use and rapid prototyping, there are several alternatives worth considering, each with its own strengths.

    Shiny: A web application framework for R, Shiny is highly favoured for statistical and analytical applications, offering deep integrations with R's extensive package ecosystem.

    Plotly Dash: Dash is a Python framework for building analytical web applications. It is particularly known for its rich interactive visualisations, leveraging Plotly's powerful charting capabilities.

    Flask: While not specifically designed for data applications, Flask is a lightweight Python web framework that offers flexibility and control, making it suitable for building custom web applications from scratch.

    Voilà: For those working in the Jupyter ecosystem, Voilà can turn Jupyter notebooks into standalone web applications, bridging the gap between data analysis and web deployment.

    Gradio: Emerging as a compelling choice for machine learning practitioners, Gradio simplifies the process of creating interactive GUIs for models. Its ease of use for building and sharing complex model interfaces—such as those requiring image, audio, or text inputs—makes it invaluable for quick demonstrations and feedback. Gradio's built-in functionality for sharing models via a link facilitates collaborative testing and iteration, emphasising its role in the rapid prototyping of AI and machine learning applications.

    Each of these alternatives has its context where it might be the better choice, depending on the specific requirements of the project, such as the need for complex visualisations (Dash), deep statistical analysis (Shiny), or custom web functionality (Flask).

    **Use Cases for Streamlit**

    Streamlit's simplicity and efficiency make it suitable for a broad range of applications:

    Data Visualization Dashboards: Quickly bring data to life with interactive charts and maps to share insights in an engaging way.

    Machine Learning Model Demos: Showcase machine learning models interactively, allowing users to adjust parameters and see results in real time.

    Data Wrangling Tools: Build tools to clean and transform data, making preprocessing steps more accessible and understandable.

    Prototyping Web Applications: Rapidly prototype web apps to validate ideas or demonstrate concepts, especially useful in hackathons or startup MVPs.

    Over the past year or two, I was fortunate to pick up this framework through my coursemates, and was blown away with the potential it had to offer. As one who used to participate actively in hackathons, it is enlightening to see that many of my peers utilise this on top of their school assignments as well, particularly given its ease of usage when working under time constraints. 

    **Conclusion**

    In summary, Streamlit is a powerful tool for data scientists and developers looking to quickly build and deploy data-driven web applications. Its simplicity, combined with a wide range of features, makes it a versatile choice for various use cases, from visualization dashboards to machine learning demos. While alternatives like Shiny, Dash, and Flask offer their own unique advantages, Streamlit's focus on rapid development and ease of use sets it apart in the landscape of data application frameworks.

    _As part of his summer plans, Harry will be collaborating with his former club - NUS Statistics and Data Science Society - once again to organise another technical workshop, focusing on the practicality of Streamlit in the world of data science and analytics. If you enjoyed the content of this article, do keep a look out for this workshop! UPDATE: sign-ups now open! https://bit.ly/nussds-streamlit_
    """)
elif selected == "Some Samples":
    st.subheader("Dashboard")
    st.video("https://www.youtube.com/watch?v=xyKkX_Ch4KQ")
    st.subheader("Generative AI")
    st.video("https://www.youtube.com/watch?v=qV82uyvujaY")
