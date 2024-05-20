import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Input from the user
user_input = st.text_input("Enter some text:")

# Display the user input
if user_input:
    st.write("You entered:", user_input)

# Button to clear the input
if st.button("Clear"):
    user_input = ""
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Streamlit Enthusiast")
