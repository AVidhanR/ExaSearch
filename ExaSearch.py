import streamlit as st
import exa_py as Exa

container = st.container()
container.header("Search Anything!")
container.chat_message("user")
chat_input = container.chat_input("Enter your search prompt here")

epy = Exa.api('a1906239-50ab-4ff0-8f18-a4a3f5fde925')
response = epy.search(
    chat_input,
    num_results=5,
    type='keyword',
    include_domains=['https://www.wikipedia.org/', 'https://www.google.com']
)

for result in response.results:
    container.write_stream(f'Title: {result.title}')
    container.write_stream(f'URL: {result.url}')
    container.write_stream()
