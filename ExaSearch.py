import streamlit as st
from exa_py import Exa
import requests

def display_content(title, url):
    ai.markdown(f"""
    <div style='padding: 2rem;'>
        <h3> Title of the Search: {title} </h2>
        <h4> URL to look for more: <a href="{url}" target = "_blank">Click here</a> </h3>
    </div>
    """,
    unsafe_allow_html=True
    )

def get_wikipedia_page_content(title):
    base_url = "https://en.wikipedia.org/w/api.php"


container = st.container()
container.header("Search from #Wikipedia #Google")
prompt = container.chat_message("user")
prompt.write("Enter something")
exa = Exa('a1906239-50ab-4ff0-8f18-a4a3f5fde925')
try:
    response = exa.search(
        container.chat_input('Enter your search prompt here'),
        num_results=1,
        type='keyword',
        include_domains=['https://www.wikipedia.org']
    )

    if response:
        ai = container.chat_message("ai")
        for result in response.results:
            display_content(result.title, result.url)
            ai.write(" ")

except Exception:
    container.write("")
