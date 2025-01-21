import streamlit as st

# Set the initial state for sidebar visibility
if 'sidebar_open' not in st.session_state:
    st.session_state['sidebar_open'] = False

# Automatically open the sidebar after page load
st.sidebar.title("Portfolio Navigation")
sections = ["Home", "Contacts", "Projects", "Education", "Certifications", "Tech Stack"]
selected_section = st.sidebar.radio("Navigate to:", sections)

# Home Section (always visible)
if selected_section == "Home":
    st.title("Welcome to My Portfolio")
    st.write("""
    Hi there! I'm a passionate **Data Engineer** specializing in building robust data pipelines, 
    designing ETL processes, and creating insightful data visualizations.  
    This portfolio highlights my skills, projects, certifications, and more.  
    Feel free to explore using the navigation menu on the left!
    """)

# Contacts Section
elif selected_section == "Contacts":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")
    st.write("""
    - **Email**: dobbym997@gmail.com  
    - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/dobby-m-27a5a621a/)  
    - **GitHub**: [GitHub Profile](https://github.com/Dobby-Mphahlele)
    """)

    st.write("Alternatively, use the form below to send me a message:")

    # Embed HTML Form on the Main Screen
    form_html = """
    <form action="https://formsubmit.co/dobbym997@gmail.com" method="POST" style="display:flex; flex-direction:column; gap:10px;">
        <input type="text" name="name" placeholder="Your Name" required style="padding:10px; font-size:16px;">
        <input type="email" name="email" placeholder="Your Email" required style="padding:10px; font-size:16px;">
        <textarea name="message" placeholder="Your Message" rows="4" required style="padding:10px; font-size:16px;"></textarea>
        <button type="submit" style="padding:10px; font-size:16px; background-color:#4CAF50; color:white; border:none; cursor:pointer;">Send</button>
    </form>
    """
    st.components.v1.html(form_html, height=300)

# Projects Section
elif selected_section == "Projects":
    st.title("My Projects")
    project_selected = st.selectbox(
        "Select a Project",
        [
            "Kafka Real-Time Alerts",
            "SSIS ETL Pipelines",
            "Student Grade Tracker",
            "Mall Parking System Tracker"
        ],
    )
    if project_selected == "Kafka Real-Time Alerts":
        st.write("**:zap: Kafka Real-Time Alerts**: Developed a Kafka-based alert system for job postings and breaking news. [Project Link](https://github.com/Dobby-Mphahlele)")
    elif project_selected == "SSIS ETL Pipelines":
        st.write("**:floppy_disk: SSIS ETL Pipelines**: Created ETL workflows for data loading and visualization in Power BI. [Project Link](https://github.com/Dobby-Mphahlele)")
    elif project_selected == "Student Grade Tracker":
        st.write("**:memo: Student Grade Tracker**: Built a Python-based system to track and analyze student grades. [Project Link](https://github.com/Dobby-Mphahlele)")
    elif project_selected == "Mall Parking System Tracker":
        st.write("**:car: Mall Parking System Tracker**: Designed a system to monitor parking space availability in malls. [Project Link](https://github.com/Dobby-Mphahlele)")

# Education Section
elif selected_section == "Education":
    st.title("Education")
    st.write("""
    - **Bachelor of Science in Computer Science and Geography**  
      North-West University  
      Graduation: 2021  
    """)

# Certifications Section
elif selected_section == "Certifications":
    st.title("Certifications")
    st.write("""
    - **MS-900 Microsoft 365 Fundamentals**
    - **AZ-900 Microsoft Azure Fundamentals**
    - **DP-600: Azure Data Engineer Associate**
    - **SCRUM Fundamentals**
    - **Databricks Lakehouse Fundamentals**
    - **Databricks GenAi Fundamentals**  
    """)

# Tech Stack Section
elif selected_section == "Tech Stack":
    st.title("Technical Skills")
    st.write("""
    ### Programming
    - Python, SQL

    ### Data Engineering
    - Apache Kafka, Spark, SSIS, ETL processes

    ### Visualization
    - Power BI, Streamlit

    ### Cloud Platforms
    - Azure, AWS
    """)

   
