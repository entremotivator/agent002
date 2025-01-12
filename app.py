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
    "Home": {
        "icon": "house-door",
        "func": st_pages.home,
        "description": "Guidelines & Overview",
        "badge": "Informative",
        "color": "var(--primary-color)",
        "tooltip": "Get started with an overview of the platform's features and guidelines for navigating the system.",
        "order": 1,  # Can define a sorting order for the pages
        "permissions": ["admin", "user"],  # Permissions required to access this page
        "visibility": True  # If False, the page won't be shown in the navigation
    },
    "Language Models Management": {
        "icon": "gear",
        "func": st_pages.model_management,
        "description": "Download and configure language models for various tasks.",
        "badge": "Configurations",
        "color": "var(--secondary-color)",
        "tooltip": "Manage and configure the models that power the AI agents in the system.",
        "order": 2,
        "permissions": ["admin"],
        "visibility": True
    },
    "AI Conversation": {
        "icon": "chat-dots",
        "func": st_pages.ai_chatbot,
        "description": "Interact with the AI chatbot for engaging conversations.",
        "badge": "Application",
        "color": "var(--highlight-color)",
        "tooltip": "Engage in natural language conversations powered by AI models.",
        "order": 3,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "RAG Conversation": {
        "icon": "chat-dots",
        "func": st_pages.rag_chat,
        "description": "PDF AI Chat Assistant for interactive document-based conversations.",
        "badge": "Application",
        "color": "var(--highlight-color)",
        "tooltip": "Have AI-assisted conversations based on the content of PDFs.",
        "order": 4,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Dashboard": {
        "icon": "bar-chart",
        "func": st_pages.dashboard,
        "description": "Overview of all systems, tracking and analyzing performance.",
        "badge": "Analytics",
        "color": "var(--primary-color)",
        "tooltip": "Visualize and analyze the performance of all your AI models and agents in one place.",
        "order": 5,
        "permissions": ["admin"],
        "visibility": True
    },
    "Content Agents": {
        "icon": "file-earmark-text",
        "func": st_pages.content_agents,
        "description": "Manage content creation agents for automated writing and content generation.",
        "badge": "Management",
        "color": "var(--secondary-color)",
        "tooltip": "Create, manage, and optimize content agents designed for automated content generation.",
        "order": 6,
        "permissions": ["admin", "editor"],
        "visibility": True
    },
    "Agent Headquarters": {
        "icon": "building",
        "func": st_pages.agent_headquarters,
        "description": "Centralized management hub for overseeing all agents in the system.",
        "badge": "Operations",
        "color": "var(--primary-color)",
        "tooltip": "Monitor and manage all your agents from a single location.",
        "order": 7,
        "permissions": ["admin"],
        "visibility": True
    },
    "LLM Agents": {
        "icon": "robot",
        "func": st_pages.llm_agents,
        "description": "Manage and deploy language model agents to handle specific tasks.",
        "badge": "Agents",
        "color": "var(--highlight-color)",
        "tooltip": "View, create, and deploy language model agents tailored to your needs.",
        "order": 8,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Voice Agent": {
        "icon": "mic",
        "func": st_pages.voice_agent,
        "description": "Manage voice-activated AI agents for speech-driven applications.",
        "badge": "AI",
        "color": "var(--secondary-color)",
        "tooltip": "Interact with and manage voice-activated AI agents for speech-based interfaces.",
        "order": 9,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Agent Command": {
        "icon": "command",
        "func": st_pages.agent_command,
        "description": "Command and control interface for managing agent actions.",
        "badge": "Control",
        "color": "var(--primary-color)",
        "tooltip": "Directly control the actions and operations of your agents from this interface.",
        "order": 10,
        "permissions": ["admin"],
        "visibility": True
    },
    "Format Agents": {
        "icon": "pencil",
        "func": st_pages.format_agents,
        "description": "Text formatting agents to help with transforming content into various styles.",
        "badge": "Text",
        "color": "var(--secondary-color)",
        "tooltip": "Apply different formatting styles to your content through automated text formatting agents.",
        "order": 11,
        "permissions": ["admin", "editor"],
        "visibility": True
    },
    "Visual Agent Flow": {
        "icon": "flow-chart",
        "func": st_pages.visual_agent_flow,
        "description": "Visualize agent workflows to understand how agents interact and perform tasks.",
        "badge": "Visualization",
        "color": "var(--highlight-color)",
        "tooltip": "Graphically represent and optimize your agents' workflows and interactions.",
        "order": 12,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Agent Projects": {
        "icon": "folder",
        "func": st_pages.agent_projects,
        "description": "Manage and track projects involving AI agents.",
        "badge": "Projects",
        "color": "var(--primary-color)",
        "tooltip": "Organize and track the progress of various AI agent projects from start to finish.",
        "order": 13,
        "permissions": ["admin", "project_manager"],
        "visibility": True
    },
    "AI Agent Roster": {
        "icon": "list-ul",
        "func": st_pages.ai_agent_roster,
        "description": "View and manage a roster of active AI agents.",
        "badge": "Roster",
        "color": "var(--secondary-color)",
        "tooltip": "Get a complete list of active agents and their statuses.",
        "order": 14,
        "permissions": ["admin"],
        "visibility": True
    },
    "Agent Generator": {
        "icon": "plus-circle",
        "func": st_pages.agent_generator,
        "description": "Generate new AI agents for various tasks and roles.",
        "badge": "Creation",
        "color": "var(--highlight-color)",
        "tooltip": "Create new agents quickly using templates or custom configurations.",
        "order": 15,
        "permissions": ["admin"],
        "visibility": True
    },
    "Active Agents": {
        "icon": "users",
        "func": st_pages.active_agents,
        "description": "Monitor the real-time status and performance of active agents.",
        "badge": "Status",
        "color": "var(--primary-color)",
        "tooltip": "Track and manage the performance of all currently active agents in the system.",
        "order": 16,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "LLM Library": {
        "icon": "book",
        "func": st_pages.llm_library,
        "description": "Access and browse a library of pre-configured language models.",
        "badge": "Library",
        "color": "var(--secondary-color)",
        "tooltip": "Explore and use a collection of powerful language models to enhance your agents.",
        "order": 17,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Agent Tool Library": {
        "icon": "tools",
        "func": st_pages.agent_tool_library,
        "description": "Tools and utilities to support the management and operation of agents.",
        "badge": "Tools",
        "color": "var(--highlight-color)",
        "tooltip": "Access a variety of tools to help manage, optimize, and troubleshoot your agents.",
        "order": 18,
        "permissions": ["admin", "user"],
        "visibility": True
    },
    "Forms": {
        "icon": "file-earmark",
        "func": st_pages.forms,
        "description": "Forms and submissions management for collecting and processing data.",
        "badge": "Forms",
        "color": "var(--primary-color)",
        "tooltip": "Manage and process form submissions for data collection and workflows.",
        "order": 19,
        "permissions": ["admin", "user"],
        "visibility": True
    }
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


