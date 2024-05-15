import streamlit as st

container = st.container()
container.title("Search Anything!")
container.write("Type in and search for something...")
chat_input = container.chat_input("Enter your search prompt here")

