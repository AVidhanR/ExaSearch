import streamlit as st # type: ignore

st.set_page_config(page_icon="🔍")

st.navigation({
    "Home": [
        st.Page("pages/exa_search.py", title="Exa Search")
    ],
    "About": [
        st.Page("pages/about.py", title="About Exa Search")
    ],
}).run()