
import streamlit as st

def agent_command():
    st.title("Agent Command")
    st.markdown("""
    Issue commands to agents for specific actions.
    """)
    command = st.text_input("Enter command:")
    if st.button("Execute"):
        st.success(f"Command '{command}' executed successfully!")
