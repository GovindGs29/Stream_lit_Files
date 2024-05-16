import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Function to get response from GPT-3
def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.set_page_config(page_title="ChatGPT App", page_icon="💬")

st.title("💬 ChatGPT App")
st.write("This is a simple ChatGPT app built with Streamlit.")

# Sidebar layout
st.sidebar.title("Settings")
with st.sidebar.expander("About"):
    st.write("""
        This app uses OpenAI's GPT-3 model to generate responses.
        Enter a prompt in the input box below and click 'Submit' to get a response.
    """)

# Input prompt from the user
prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Submit"):
    if prompt:
        with st.spinner("Generating response..."):
            response = get_gpt_response(prompt)
            st.write("### Response:")
            st.write(response)
    else:
        st.warning("Please enter a prompt.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by [Your Name](https://your-linkedin-profile)")
