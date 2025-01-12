
import streamlit as st

def content_agents():
    st.title("Content Agents")
    st.markdown("""
    Manage agents responsible for content creation and formatting.
    """)
    st.text_area("Agent Tasks:")
    st.button("Submit")
