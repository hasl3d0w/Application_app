import streamlit as st

st.title("Projects")
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Here are some of my sample projects:")

# Project 1
st.subheader("🧮Calculator App🧮")
st.write("A simple calculator with multiple functions.")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    st.success(f"Result: {result}")

                                                       
