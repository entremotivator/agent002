import streamlit as st
import st_pages  # Required module for page routing

# Set page configuration
st.set_page_config(page_title="TalkNexus - Ollama Chatbot Multi-Model Interface", layout="wide", page_icon="🤖")

# Function to load custom CSS from file
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Error loading CSS file: {e}")

# Load custom CSS
load_css('styles.css')

# Initialize session state for tracking the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Header Section with styling
st.markdown("""
<div class="header">
    <div class="animated-bg"></div>
    <div class="header-content">
        <h1 class="header-title">Ollama Chatbot Multi-Model Interface</h1> 
        <p class="header-subtitle">Advanced Language Models & Intelligent Conversations</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Define pages with relevant icons, functions, descriptions, and other info
PAGES = {
    "Home": {
        "icon": "house-door",
        "func": st_pages.home,
        "description": "Guidelines & Overview",
        "badge": "Informative",
        "color": "var(--primary-color)"
    },
    "Language Models Management": {
        "icon": "gear",
        "func": st_pages.model_management,
        "description": "Download Models",
        "badge": "Configurations",
        "color": "var(--secondary-color)"
    },
    "AI Conversation": {
        "icon": "chat-dots",
        "func": st_pages.ai_chatbot,
        "description": "Interactive AI Chat",
        "badge": "Application",
        "color": "var(--highlight-color)"
    },
    "RAG Conversation": {
        "icon": "chat-dots",
        "func": st_pages.rag_chat,
        "description": "PDF AI Chat Assistant",
        "badge": "Application",
        "color": "var(--highlight-color)"
    },
    "Dashboard": {
        "icon": "bar-chart",
        "func": st_pages.dashboard,
        "description": "Overview of all systems",
        "badge": "Analytics",
        "color": "var(--primary-color)"
    },
    "Content Agents": {
        "icon": "file-earmark-text",
        "func": st_pages.content_agents,
        "description": "Manage Content Agents",
        "badge": "Management",
        "color": "var(--secondary-color)"
    },
    "Agent Headquarters": {
        "icon": "building",
        "func": st_pages.agent_headquarters,
        "description": "Centralized Agent Management",
        "badge": "Operations",
        "color": "var(--primary-color)"
    },
    "LLM Agents": {
        "icon": "robot",
        "func": st_pages.llm_agents,
        "description": "Language Model Agents",
        "badge": "Agents",
        "color": "var(--highlight-color)"
    },
    "Voice Agent": {
        "icon": "mic",
        "func": st_pages.voice_agent,
        "description": "Voice-Activated Agents",
        "badge": "AI",
        "color": "var(--secondary-color)"
    },
    "Agent Command": {
        "icon": "command",
        "func": st_pages.agent_command,
        "description": "Command & Control Interface",
        "badge": "Control",
        "color": "var(--primary-color)"
    },
    "Format Agents": {
        "icon": "pencil",
        "func": st_pages.format_agents,
        "description": "Text Formatting Agents",
        "badge": "Text",
        "color": "var(--secondary-color)"
    },
    "Visual Agent Flow": {
        "icon": "flow-chart",
        "func": st_pages.visual_agent_flow,
        "description": "Visualize Agent Flows",
        "badge": "Visualization",
        "color": "var(--highlight-color)"
    },
    "Agent Projects": {
        "icon": "folder",
        "func": st_pages.agent_projects,
        "description": "Manage Agent Projects",
        "badge": "Projects",
        "color": "var(--primary-color)"
    },
    "AI Agent Roster": {
        "icon": "list-ul",
        "func": st_pages.ai_agent_roster,
        "description": "Roster of Active Agents",
        "badge": "Roster",
        "color": "var(--secondary-color)"
    },
    "Agent Generator": {
        "icon": "plus-circle",
        "func": st_pages.agent_generator,
        "description": "Generate New Agents",
        "badge": "Creation",
        "color": "var(--highlight-color)"
    },
    "Active Agents": {
        "icon": "users",
        "func": st_pages.active_agents,
        "description": "Monitor Active Agents",
        "badge": "Status",
        "color": "var(--primary-color)"
    },
    "LLM Library": {
        "icon": "book",
        "func": st_pages.llm_library,
        "description": "Access Language Models",
        "badge": "Library",
        "color": "var(--secondary-color)"
    },
    "Agent Tool Library": {
        "icon": "tools",
        "func": st_pages.agent_tool_library,
        "description": "Tools for Agent Management",
        "badge": "Tools",
        "color": "var(--highlight-color)"
    },
    "Forms": {
        "icon": "file-earmark",
        "func": st_pages.forms,
        "description": "Forms and Submissions",
        "badge": "Forms",
        "color": "var(--primary-color)"
    }
}

# Add Bootstrap icons CDN
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# Function to handle page navigation
def navigate():
    with st.sidebar:
        st.markdown('''
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
        ''', unsafe_allow_html=True)

        st.markdown('---')

        # Generate menu items
        for page, info in PAGES.items():
            selected = st.session_state.current_page == page
            
            # Invisible button to select page
            if st.button(f"{page}", key=f"nav_{page}", use_container_width=True, type="secondary" if selected else "primary"):
                st.session_state.current_page = page
                st.experimental_rerun()

            # Visual representation of the menu item
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

        # End of the sidebar
        st.markdown('</div>', unsafe_allow_html=True)
        
        return st.session_state.current_page

# Execute the selected page
try:
    selected_page = navigate()
    
    # Run the page's corresponding function
    page_function = PAGES[selected_page]["func"]
    page_function()

except Exception as e:
    st.error(f"Error loading page: {e}")
    st_pages.home.run()

# Footer section
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <p>© 2024 Powered by <a href="https://github.com/TsLu1s" target="_blank">TsLu1s </a>. 
        Advanced Language Models & Intelligent Conversations | Project Source: 
        <a href="https://github.com/TsLu1s/talknexus" target="_blank"> TalkNexus</p>
    </div>
</div>
""", unsafe_allow_html=True)

