import streamlit as st
from exa_py import Exa


def display_content(title, url):
    container.markdown(f"""
    <div style='margin: 1em;'>
        <h3> Title of the Search: <i>{title}</i> </h2>
        <!-- <h4> URL to look for more: <a href="{url}" target = "_blank">Click here</a> </h3> -->
        <h5>check out the content from below,</h5>
        <iframe src = "{url}" style="width: 100%; height: 100vh; border: none;"></iframe>
    </div>
    """, unsafe_allow_html=True)

container = st.container()
container.header("Search from #Wikipedia")
prompt = container.chat_message("ai")
prompt.write("What do you want to search for ?")
user_input = container.chat_input('Enter your search query here')
exa = Exa('a1906239-50ab-4ff0-8f18-a4a3f5fde925')
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
    container.write("")
