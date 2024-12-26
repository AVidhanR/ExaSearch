# type: ignore
import streamlit as st
from exa_py import Exa
from dotenv import load_dotenv, dotenv_values
from pages.footer import footer

# Function to display the content
def display_content(title, url):
    container.markdown(f"""
    <div>
        <h3>Title of the Search: <code>{title}</code></h3>
        <h4>Check out the content from below,</h4>
        <iframe src = "{url}" style="width: 100%; height: 100dvh; border: none; border-radius: 1rem;"></iframe>
    </div>
    """, unsafe_allow_html=True)

# Load the environment variables
load_dotenv()
env_vars = dotenv_values()

# Create a container
container = st.container()
container.header("`Search data from #Wikipedia`")
prompt = container.chat_message("human")
prompt.write("`What do you want to search for ?`")
user_input = container.chat_input('Enter your search query here')

# Search the data from Exa API
exa = Exa(env_vars.get('EXA_API_KEY'))
try:
    exa_response = exa.search(
        user_input,
        num_results=1,
        type='keyword',
        include_domains=['https://www.wikipedia.org']
    )

    if exa_response:
        for result in exa_response.results:
            display_content(result.title, result.url)
            container.write(" ")
except Exception:
    container.write("`Invalid search query. Please try again.`")

# Display the footer
footer()