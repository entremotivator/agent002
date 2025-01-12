import streamlit as st
# Import run functions for each page
from .st_pages.home import run as home
from .st_pages.model_management import run as model_management
from .st_pages.ai_chatbot import run as ai_chatbot
from .st_pages.rag_chat import run as rag_chat
from .st_pages.dashboard import run as dashboard
from .st_pages.content_agents import run as content_agents
from .st_pages.agent_headquarters import run as agent_headquarters
from .st_pages.llm_agents import run as llm_agents
from .st_pages.voice_agent import run as voice_agent
from .st_pages.agent_command import run as agent_command
from .st_pages.format_agents import run as format_agents
from .st_pages.visual_agent_flow import run as visual_agent_flow
from .st_pages.agent_projects import run as agent_projects
from .st_pages.ai_agent_roster import run as ai_agent_roster
from .st_pages.agent_generator import run as agent_generator
from .st_pages.active_agents import run as active_agents
from .st_pages.llm_library import run as llm_library
from .st_pages.agent_tool_library import run as agent_tool_library
from .st_pages.forms import run as forms

# Page Configuration
st.set_page_config(
    page_title="TalkNexus - Ollama Chatbot Multi-Model Interface",
    layout="wide",
    page_icon="🤖"
)

# Function to load custom CSS styles from a file
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file '{file_name}' not found.")
    except Exception as e:
        st.warning(f"Error loading CSS file: {e}")

# Load custom CSS (if available)
load_css('styles.css')

# Initialize session state for the current page if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Header Section with Styling and Branding
st.markdown("""
<div class="header">
    <div class="animated-bg"></div>
    <div class="header-content">
        <h1 class="header-title">Ollama Chatbot Multi-Model Interface</h1> 
        <p class="header-subtitle">Advanced Language Models & Intelligent Conversations</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Define Pages and Their Metadata for Navigation
PAGES = {
    "Home": {"icon": "house-door", "func": home, "description": "Guidelines & Overview", "badge": "Informative", "color": "var(--primary-color)"},
    "Language Models Management": {"icon": "gear", "func": model_management, "description": "Download Models", "badge": "Configurations", "color": "var(--secondary-color)"},
    "AI Conversation": {"icon": "chat-dots", "func": ai_chatbot, "description": "Interactive AI Chat", "badge": "Application", "color": "var(--highlight-color)"},
    # Add other pages similarly...
}

# Add Bootstrap Icons for Better Visuals in Navigation Sidebar
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# Sidebar Navigation Functionality
def navigate():
    with st.sidebar:
        # Branding Section with Link to GitHub or Homepage
        st.markdown("""
        <a href="https://github.com/TsLu1s/talknexus" target="_blank" style="text-decoration: none; color: inherit; display: block;">
            <div class="header-container" style="cursor: pointer;">
                <div class="profile-section">
                    <div class="profile-info">
                        <h1 style="font-size: 32px;">TalkNexus</h1>
                        <span class="active-badge" style="font-size: 16px;">AI Chatbot Multi-Model Application</span>
                    </div>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

        st.markdown('---')

        # Page Selection Buttons in Sidebar Navigation Menu
        for page, info in PAGES.items():
            selected = st.session_state.current_page == page

            if st.button(f"{page}", key=f"nav_{page}", use_container_width=True):
                st.session_state.current_page = page  # Update current page in session state
                st.experimental_rerun()  # Rerun the app to load the selected page

            # Optional: Add additional styling for selected pages (e.g., highlighting)
            st.markdown(f"""
                <div class="menu-item {'selected' if selected else ''}">
                    <i class="bi bi-{info['icon']}"></i> {page}
                </div>
            """, unsafe_allow_html=True)
    
    return st.session_state.current_page

# Execute the Selected Page's Functionality Dynamically
try:
    selected_page = navigate()
    PAGES[selected_page]["func"]()  # Run the function associated with the selected page
except Exception as e:
    st.error(f"Error loading page: {e}")
    home()  # Fallback to Home Page in Case of Errors

# Footer Section with Attribution or Links to Resources/Documentation
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <p>© 2025 Powered by <a href="https://github.com/TsLu1s" target="_blank">TalkNexus Team</a></p>
    </div>
</div>
""", unsafe_allow_html=True)


