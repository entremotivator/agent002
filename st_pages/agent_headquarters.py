
import streamlit as st

def agent_headquarters():
    st.title("Agent Headquarters")
    st.markdown("""
    Centralized hub to manage all active and inactive agents.
    """)
    st.checkbox("Show Active Agents Only")
    st.write("Agent 1: Active")
    st.write("Agent 2: Inactive")
