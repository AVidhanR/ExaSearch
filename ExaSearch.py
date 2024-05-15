import streamlit as st
from exa_py import Exa


def display_content(title, url):
    ai.markdown(f"""
    <div style='padding: 2rem;'>
        <h3> Title of the Search: {title} </h2>
        <h4> URL to look for more: <a href="{url}" target = "_blank">Click here</a> </h3>
    </div>
    """,
                unsafe_allow_html=True
                )

container = st.container()
container.header("Search from #Wikipedia #Google")
prompt = container.chat_message("user")
prompt.write("Enter something")
input = container.chat_input('Enter your search prompt here')
exa = Exa('a1906239-50ab-4ff0-8f18-a4a3f5fde925')
try:
    exa_response = exa.search(
        input,
        num_results=1,
        type='keyword',
        include_domains=['https://www.wikipedia.org']
    )

    if exa_response:
        ai = container.chat_message("ai")
        for result in exa_response.results:
            display_content(result.title, result.url)
            ai.write(" ")
except Exception:
    container.write("")
