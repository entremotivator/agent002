
import streamlit as st

def home():
    st.title("Welcome to TalkNexus!")
    st.markdown("""
    This platform serves as a multi-model interface for advanced AI chatbot interactions. 
    Here’s what you can explore:
    - Manage and download AI models.
    - Engage in intelligent conversations with multiple AI agents.
    - Access analytical dashboards for agent performance.
    Use the sidebar to navigate through various functionalities.
    """)
    st.info("Get started by selecting an option from the menu on the left.")
