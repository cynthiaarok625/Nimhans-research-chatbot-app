import streamlit as st
from gemini import getresponse
from supabase_db import insert_participant

# print("Create table if doesnt exists")
# create_table()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "research_submitted" not in st.session_state:
    st.session_state["research_submitted"] = False
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False



st.set_page_config(
    page_title="Nimhans Research Program",
    page_icon="🏥",
    layout="wide"
)

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f9ff;
}

.hero-container {
    background: linear-gradient(135deg, #d6ecff, #f4f9ff);
    padding: 60px;
    border-radius: 20px;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 2rem;
    font-weight: 700;
    color: #0b3d91;
}

.hero-text {
     font-size: 1rem;
     font-weight: 400;
     color: #0b3d91;
     opacity: 0.85;
     margin-top: 12px;
     max-width: 700px;
     line-height: 1.7;
}

.section-container {
    background: white;
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0px 2px 15px rgba(0,0,0,0.08);
}

.section-title {
    font-size: 2rem;
    font-weight: bold;
    color: #0b3d91;
    margin-bottom: 20px;
}

.feature-card {
    background-color: #f7fbff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #0b3d91;
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    padding: 20px;
    color: #777;
    font-size: 14px;
}

.stButton>button {
    background-color: #0b3d91;
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    border: none;
}

.stButton>button:hover {
    background-color: #154fb5;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# HERO SECTION
# --------------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
     <div class="hero-container">
     <div class="hero-title">
        Protecting Your Family's Future Through Groundbreaking Medical Research
     </div>

     <div class="hero-text">
        Join our research initiatives aimed at understanding, preventing, and treating long-term illnesses so future generations can enjoy healthier lives.
     </div>
     </div>
      """, unsafe_allow_html=True)

    # Initialize session state
    if "show_chatbot" not in st.session_state:
        st.session_state.show_chatbot = False
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Button to show chatbot
    if not st.session_state.show_chatbot:
        if st.button("Chat with Us"):
            st.session_state.show_chatbot = True
            st.rerun()

    # --------------------------
    # CHATBOT CODE
    # --------------------------
    # if st.session_state.show_chatbot:
    #     st.subheader("Research Assistant")

    #     # Display previous messages
    #     for message in st.session_state.messages:
    #         with st.chat_message(message["role"]):
    #             st.markdown(message["content"])

    #     # User input
    #     user_question = st.chat_input("Ask a question about our research program...")

    #     if user_question:
    #         # Show user message
    #         st.session_state.messages.append(
    #             {"role": "user", "content": user_question}
    #         )

    #         # Replace this with Gemini/OpenAI/Hugging Face call
    #         answer = getresponse(user_question)

    #         # Save assistant response
    #         st.session_state.messages.append(
    #             {"role": "assistant", "content": answer}
    #         )

    #         st.rerun()

   

with col2:
    st.markdown("""
     <img src="https://images.unsplash.com/photo-1584515933487-779824d29309"
        style="width:100%;
            height:366px;
            object-fit:cover;
            border-radius:20px;">
       """, unsafe_allow_html=True)

col1, col2= st.columns([1, 2]) 

with col1:
    
     # --------------------------
    # CHATBOT CODE
    # --------------------------
    if st.session_state.show_chatbot:
        st.subheader("Research Assistant")

        # Display previous messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input
        user_question = st.chat_input("Ask a question about our research program...")

        if user_question:
            # Show user message
            st.session_state.messages.append(
                {"role": "user", "content": user_question}
            )

            # Replace this with Gemini/OpenAI/Hugging Face call
            answer = getresponse(user_question)

            # Save assistant response
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

            st.rerun()
        

# --------------------------
# TRUST METRICS
# --------------------------
st.markdown("<br>", unsafe_allow_html=True)

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Years of Experience", "25+")

with metric2:
    st.metric("Patients Served", "100,000+")

with metric3:
    st.metric("Medical Specialists", "150+")

# --------------------------
# RESEARCH PROGRAM
# --------------------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2= st.columns(2)
with col1:
    st.markdown("""
    <div class="section-container">
        <div class="section-title">
            Advancing Healthcare Through Research
        </div>
        <div class="hero-text">
                <p>
        Our hospital is committed to improving patient outcomes through
        innovative medical research. We collaborate with leading healthcare
        professionals and researchers to develop new treatments and improve
        standards of care.
        </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
    width= 500
        )


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>Clinical Studies</h4>
        <p>Participate in groundbreaking medical studies.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>Patient-Centered Research</h4>
        <p>Helping shape better treatments through real-world experiences.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>Innovation & Discovery</h4>
        <p>Supporting advancements in healthcare and medical technology.</p>
    </div>
    """, unsafe_allow_html=True)



# --------------------------
# RESEARCH FORM
# --------------------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
      <div class="section-container">
       <div class="section-title">
           Sign Up for Research Opportunities
       </div>

       <p>
        Interested in contributing to the future of healthcare?
        Complete the form below and our research team will contact you.
        </p>
        </div>
       """, unsafe_allow_html=True)

with st.form("research_form"):

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name",disabled=st.session_state.research_submitted)
        email = st.text_input("Email Address",disabled=st.session_state.research_submitted)
        dob = st.date_input("Date of Birth", disabled=st.session_state.research_submitted)

    with col2:
        phone = st.text_input("Phone Number",disabled=st.session_state.research_submitted)
        gender = st.selectbox(
            "Gender",
            ["Select", "Male", "Female", "Other"],disabled=st.session_state.research_submitted
        )

    interest = st.selectbox(
        "Area of Medical Interest",
        [
            "Cardiology",
            "Neurology",
            "Oncology",
            "Diabetes",
            "Mental Health",
            "General Medicine"
        ],disabled=st.session_state.research_submitted
    )

    conditions = st.text_area(
        "Existing Medical Conditions (Optional)",disabled=st.session_state.research_submitted
    )

    contact_method = st.radio(
        "Preferred Contact Method",
        ["Email", "Phone"],disabled=st.session_state.research_submitted
    )

    consent = st.checkbox(
        "I agree to be contacted regarding research opportunities.",disabled=st.session_state.research_submitted
    )

    submitted = st.form_submit_button(
        "Register Interest",disabled=st.session_state.research_submitted
    )

    if submitted:

        if not consent:
            st.error("Please provide consent before submitting.")
        else:
            insert_participant(full_name,email,phone,dob,gender,interest,conditions,contact_method,consent )
            st.session_state.research_submitted = True
            st.rerun()
            
if st.session_state.research_submitted:

    st.success(
        "Thank you for your interest. A member of our research team will contact you soon."
    )

# --------------------------
# FOOTER
# --------------------------
st.markdown("---")

st.markdown("""
<div class="footer">
    <strong>ABC Hospital</strong>
    <br>
    123 Healthcare Avenue, Medical City
    <br>
    Phone: +91 98765 43210 |
    Email: research@abchospital.com<br><br>

    Privacy Policy | Terms & Conditions
    © 2026 ABC Hospital. All Rights Reserved.
</div>
""", unsafe_allow_html=True)

