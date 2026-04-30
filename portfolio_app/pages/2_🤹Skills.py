import streamlit as st
 
st.title("Skills")
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)


skills = {
    "Python": 80,
    "Streamlit": 85,
    "HTML/CSS": 75,
    "Problem Solving": 90
}

for skill, level in skills.items():
    st.progress(level, text=f"{skill} ({level}%)") 
