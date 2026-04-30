import streamlit as st

st.title("Contact Me")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Feel free to reach out!")

Name = st.text_input("Your Name")
Email = st.text_input("Your Email")
Message = st.text_area("Your Message")

if st.button("Send Message"):
    if Name and Email and Message:
        st.success("✅ Message sent successfully!")
    else:
        st.error("⚠️ Please fill in all fields.")

st.divider()

st.subheader("My Info")

st.write("📧 Email: daohasle9@gmail.com")
st.write("📱 Phone: 09123456789")
st.write("📍 Location: Philippines")

