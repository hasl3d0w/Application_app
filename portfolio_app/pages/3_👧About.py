import streamlit as st

st.title("About Me")
st.image("portfolio_app/images", width=200)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""Hi I'm  **Hasle**, a student passionate about:
            - 💻Programming💻,
            - 🎨UI/UX Design🎨,
            - 🌐Web Development🌐
             """)

st.divider()


st.subheader("Fun Fact Generator")

facts = [
    "I love building apps!",
    "I enjoy solving coding problems.",
    "I like learning new technologies.",
    "I want to become a developer someday."
]

if st.button("Show Fun Fact"):
    import random
    st.success(random.choice(facts))
