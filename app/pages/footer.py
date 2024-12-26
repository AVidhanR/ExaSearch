import streamlit as st  # type: ignore

def footer():
    st.html('''
    <footer style="
    text-align: center;
    padding: 10px;
    font-size: 12px;
    width: 100%;
    clear: both;">
        <p style="margin-bottom: 5px;">Created by <a href="https://www.linkedin.com/in/AVidhanR/" target="_blank" style="color: #66d9ef;">A Vidhan Reddy</a></p>
        <p style="margin-bottom: 5px;">View on <a href="https://github.com/AVidhanR/ExaSearch" target="_blank" style="color: #66d9ef;">GitHub</a></p>
    </footer>
    ''')