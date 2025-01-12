
import streamlit as st

def dashboard():
    st.title("Dashboard")
    st.markdown("""
    Analyze system performance and agent activities.
    """)
    st.metric("Active Agents", 15)
    st.metric("Completed Chats", 120)
    st.line_chart([1, 3, 2, 4])
