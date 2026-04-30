import streamlit as st

st.set_page_config(page_title="My portfolio", page_icon="🌐")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🌐 Welcome To My Portfolio 🌐")

st.markdown ("""Hi, I'm Hasle!
            This is my **Multipage Streamlit Web App** where you can explore:
            -👧 About me ,
            -👩‍💻 My Projects ,
            -🛠️ My Skills ,
            -📞 Contact Information. 
             Use the sidebar to navigate between pages.  """ )

st.divider()
st.subheader("Quick Survey")

name = st.text_input("Enter you Name:")
favorite = st.selectbox("What do you like most?", ["Coding", "Designing", "Learning", "Gaming"])

if st.button("Submit"):
    st.success(f"Thanks {name}! You like {favorite}")

st.divider()
st.info("This app is built using Streamlit with multiple pages and interactive UI")