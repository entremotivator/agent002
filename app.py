import streamlit as st
from .st_pages import (
    home, model_management, ai_chatbot, rag_chat, dashboard, content_agents, 
    agent_headquarters, llm_agents, voice_agent, agent_command, format_agents, 
    visual_agent_flow, agent_projects, ai_agent_roster, agent_generator, 
    active_agents, llm_library, agent_tool_library, forms
)

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

# Set page configuration
st.set_page_config(page_title="TalkNexus - Ollama Chatbot Multi-Model Interface", layout="wide", page_icon="🤖")

# Function to load custom CSS
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Error loading CSS file: {e}")

# Load custom CSS
load_css('styles.css')

# Initialize session state for the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Header Section
st.markdown("""
<div class="header">
    <div class="animated-bg"></div>
    <div class="header-content">
        <h1 class="header-title">Ollama Chatbot Multi-Model Interface</h1> 
        <p class="header-subtitle">Advanced Language Models & Intelligent Conversations</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Define pages and their metadata
PAGES = {
    "Home": {"icon": "house-door", "func": home, "description": "Guidelines & Overview", "badge": "Informative", "color": "var(--primary-color)"},
    "Language Models Management": {"icon": "gear", "func": model_management, "description": "Download Models", "badge": "Configurations", "color": "var(--secondary-color)"},
    "AI Conversation": {"icon": "chat-dots", "func": ai_chatbot, "description": "Interactive AI Chat", "badge": "Application", "color": "var(--highlight-color)"},
    "RAG Conversation": {"icon": "chat-dots", "func": rag_chat, "description": "PDF AI Chat Assistant", "badge": "Application", "color": "var(--highlight-color)"},
    "Dashboard": {"icon": "bar-chart", "func": dashboard, "description": "Overview of all systems", "badge": "Analytics", "color": "var(--primary-color)"},
    "Content Agents": {"icon": "file-earmark-text", "func": content_agents, "description": "Manage Content Agents", "badge": "Management", "color": "var(--secondary-color)"},
    "Agent Headquarters": {"icon": "building", "func": agent_headquarters, "description": "Centralized Agent Management", "badge": "Operations", "color": "var(--primary-color)"},
    "LLM Agents": {"icon": "robot", "func": llm_agents, "description": "Language Model Agents", "badge": "Agents", "color": "var(--highlight-color)"},
    "Voice Agent": {"icon": "mic", "func": voice_agent, "description": "Voice-Activated Agents", "badge": "AI", "color": "var(--secondary-color)"},
    "Agent Command": {"icon": "command", "func": agent_command, "description": "Command & Control Interface", "badge": "Control", "color": "var(--primary-color)"},
    "Format Agents": {"icon": "pencil", "func": format_agents, "description": "Text Formatting Agents", "badge": "Text", "color": "var(--secondary-color)"},
    "Visual Agent Flow": {"icon": "flow-chart", "func": visual_agent_flow, "description": "Visualize Agent Flows", "badge": "Visualization", "color": "var(--highlight-color)"},
    "Agent Projects": {"icon": "folder", "func": agent_projects, "description": "Manage Agent Projects", "badge": "Projects", "color": "var(--primary-color)"},
    "AI Agent Roster": {"icon": "list-ul", "func": ai_agent_roster, "description": "Roster of Active Agents", "badge": "Roster", "color": "var(--secondary-color)"},
    "Agent Generator": {"icon": "plus-circle", "func": agent_generator, "description": "Generate New Agents", "badge": "Creation", "color": "var(--highlight-color)"},
    "Active Agents": {"icon": "users", "func": active_agents, "description": "Monitor Active Agents", "badge": "Status", "color": "var(--primary-color)"},
    "LLM Library": {"icon": "book", "func": llm_library, "description": "Access Language Models", "badge": "Library", "color": "var(--secondary-color)"},
    "Agent Tool Library": {"icon": "tools", "func": agent_tool_library, "description": "Tools for Agent Management", "badge": "Tools", "color": "var(--highlight-color)"},
    "Forms": {"icon": "file-earmark", "func": forms, "description": "Forms and Submissions", "badge": "Forms", "color": "var(--primary-color)"}
}

# Add Bootstrap icons
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# Sidebar navigation
def navigate():
    with st.sidebar:
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

        for page, info in PAGES.items():
            selected = st.session_state.current_page == page
            if st.button(f"{page}", key=f"nav_{page}", use_container_width=True, type="primary" if not selected else "secondary"):
                st.session_state.current_page = page
                st.experimental_rerun()

            st.markdown(f"""
                <div class="menu-item {'selected' if selected else ''}">
                    <div class="menu-icon">
                        <i class="bi bi-{info['icon']}"></i>
                    </div>
                    <div class="menu-content">
                        <div class="menu-title">{page}</div>
                        <div class="menu-description">{info['description']}</div>
                    </div>
                    <div class="menu-badge">{info['badge']}</div>
                </div>
            """, unsafe_allow_html=True)
        return st.session_state.current_page

# Execute the selected page
try:
    selected_page = navigate()
    PAGES[selected_page]["func"]()
except Exception as e:
    st.error(f"Error loading page: {e}")
    home()

# Footer Section
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <p>© 2024 Powered by <a href="https://github.com/TsLu1s" target="_blank">TalkNexus Team</a></p>
    </div>
</div>
""", unsafe_allow_html=True)

