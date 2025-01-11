import ollama
import streamlit as st

def get_models():
    try:
        models_info = ollama.list()
        if "models" in models_info:
            return [model["name"] for model in models_info["models"]]
        else:
            st.warning("No models found. Please install some models first.")
            return []
    except Exception as e:
        st.error(f"Error connecting to Ollama: {str(e)}")
        return []

# In your main code
if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

models = get_models()
if models:
    st.session_state.selected_model = st.selectbox("Active model:", models)
else:
    st.warning("No models available. Please check your Ollama installation and model list.")
