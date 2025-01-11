import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

# Set up the page configuration for the Streamlit app
st.set_page_config(layout="wide")

# Function to generate workflow elements (nodes and edges) for an agent
def generate_agent_workflow(agent_name):
    # Define sample nodes and edges for the workflow of an agent
    elements = {
        "nodes": [
            {"data": {"id": 1, "label": "AGENT", "name": f"{agent_name} Start", "type": "Start"}},
            {"data": {"id": 2, "label": "AGENT", "name": f"{agent_name} Receive Input", "type": "Input"}},
            {"data": {"id": 3, "label": "AGENT", "name": f"{agent_name} Analyze Input", "type": "Process"}},
            {"data": {"id": 4, "label": "AGENT", "name": f"{agent_name} Generate Response", "type": "Process"}},
            {"data": {"id": 5, "label": "AGENT", "name": f"{agent_name} Send Reply", "type": "Output"}},
            {"data": {"id": 6, "label": "AGENT", "name": f"{agent_name} End", "type": "End"}},
        ],
        "edges": [
            {"data": {"id": 7, "label": "INITIATES", "source": 1, "target": 2}},
            {"data": {"id": 8, "label": "PROCESSES", "source": 2, "target": 3}},
            {"data": {"id": 9, "label": "GENERATES", "source": 3, "target": 4}},
            {"data": {"id": 10, "label": "SENDS", "source": 4, "target": 5}},
            {"data": {"id": 11, "label": "COMPLETES", "source": 5, "target": 6}},
        ],
    }
    
    return elements

# Define custom styles for the nodes and edges
node_styles = [
    NodeStyle("AGENT", "#3498db", "name", "agent_step"),  # All nodes are styled with a blue color
]

edge_styles = [
    EdgeStyle("INITIATES", caption='label', directed=True),  # Directed edges with captions
    EdgeStyle("PROCESSES", caption='label', directed=True),
    EdgeStyle("GENERATES", caption='label', directed=True),
    EdgeStyle("SENDS", caption='label', directed=True),
    EdgeStyle("COMPLETES", caption='label', directed=True),
]

# Display a header for the Streamlit app
st.markdown("### n8n Chatbot Workflow with Editable Agents")

# Create tabs for different agents
tabs = st.radio("Select an Agent", ["Agent 1", "Agent 2", "Agent 3"])

# Check if session state is initialized
if "agent_elements" not in st.session_state:
    st.session_state["agent_elements"] = {}

# Load or initialize workflow elements for the selected agent
if tabs == "Agent 1":
    if "Agent 1" not in st.session_state["agent_elements"]:
        st.session_state["agent_elements"]["Agent 1"] = generate_agent_workflow("Agent 1")
    agent_elements = st.session_state["agent_elements"]["Agent 1"]
elif tabs == "Agent 2":
    if "Agent 2" not in st.session_state["agent_elements"]:
        st.session_state["agent_elements"]["Agent 2"] = generate_agent_workflow("Agent 2")
    agent_elements = st.session_state["agent_elements"]["Agent 2"]
else:
    if "Agent 3" not in st.session_state["agent_elements"]:
        st.session_state["agent_elements"]["Agent 3"] = generate_agent_workflow("Agent 3")
    agent_elements = st.session_state["agent_elements"]["Agent 3"]

# Display the workflow of the selected agent
st.markdown(f"#### {tabs} Workflow")
st_link_analysis(agent_elements, "cose", node_styles, edge_styles)

# Section for editing nodes and edges
st.markdown(f"### Edit {tabs} Workflow")

# Add/Edit Nodes Section
with st.expander("Add/Edit Node"):
    node_action = st.radio("Choose Action", ["Add Node", "Edit Node", "Delete Node"])
    if node_action == "Add Node":
        new_node_name = st.text_input("Node Name")
        new_node_type = st.selectbox("Node Type", ["Start", "Input", "Process", "Output", "End"])
        new_node_label = st.selectbox("Node Label", ["AGENT", "PROCESS", "INPUT", "OUTPUT"])
        if st.button("Add Node"):
            if new_node_name:
                new_node_id = len(agent_elements['nodes']) + 1
                new_node = {"data": {"id": new_node_id, "label": new_node_label, "name": new_node_name, "type": new_node_type}}
                agent_elements['nodes'].append(new_node)
                st.success(f"Node '{new_node_name}' added successfully!")
                st.session_state["agent_elements"][tabs] = agent_elements
            else:
                st.error("Please enter a valid node name.")

    elif node_action == "Edit Node":
        node_to_edit = st.selectbox("Select Node to Edit", [node['data']['name'] for node in agent_elements['nodes']])
        new_name = st.text_input("New Node Name", value=node_to_edit)
        new_type = st.selectbox("Node Type", ["Start", "Input", "Process", "Output", "End"])
        new_label = st.selectbox("Node Label", ["AGENT", "PROCESS", "INPUT", "OUTPUT"])
        if st.button("Save Node Edits"):
            for node in agent_elements['nodes']:
                if node['data']['name'] == node_to_edit:
                    node['data']['name'] = new_name
                    node['data']['type'] = new_type
                    node['data']['label'] = new_label
                    st.success(f"Node '{new_name}' updated successfully!")
                    st.session_state["agent_elements"][tabs] = agent_elements
                    break

    elif node_action == "Delete Node":
        node_to_delete = st.selectbox("Select Node to Delete", [node['data']['name'] for node in agent_elements['nodes']])
        if st.button(f"Delete Node '{node_to_delete}'"):
            agent_elements['nodes'] = [node for node in agent_elements['nodes'] if node['data']['name'] != node_to_delete]
            st.success(f"Node '{node_to_delete}' deleted successfully!")
            st.session_state["agent_elements"][tabs] = agent_elements

# Add/Edit Edges Section
with st.expander("Add/Edit Edge"):
    edge_action = st.radio("Choose Edge Action", ["Add Edge", "Edit Edge", "Delete Edge"])
    if edge_action == "Add Edge":
        source_node = st.selectbox("Select Source Node", [node['data']['name'] for node in agent_elements['nodes']])
        target_node = st.selectbox("Select Target Node", [node['data']['name'] for node in agent_elements['nodes']])
        edge_label = st.text_input("Edge Label (e.g., PROCESSES, INITIATES)")
        if st.button("Add Edge"):
            if source_node and target_node and edge_label:
                new_edge = {"data": {"id": len(agent_elements['edges']) + 1, "label": edge_label, "source": source_node, "target": target_node}}
                agent_elements['edges'].append(new_edge)
                st.success(f"Edge from '{source_node}' to '{target_node}' added successfully!")
                st.session_state["agent_elements"][tabs] = agent_elements
            else:
                st.error("Please provide valid source, target, and label for the edge.")

    elif edge_action == "Edit Edge":
        edge_to_edit = st.selectbox("Select Edge to Edit", [f"{edge['data']['source']} -> {edge['data']['target']}" for edge in agent_elements['edges']])
        new_edge_label = st.text_input("New Edge Label", value=edge_to_edit.split("->")[0].strip())
        if st.button("Save Edge Edits"):
            for edge in agent_elements['edges']:
                if f"{edge['data']['source']} -> {edge['data']['target']}" == edge_to_edit:
                    edge['data']['label'] = new_edge_label
                    st.success(f"Edge label updated to '{new_edge_label}'!")
                    st.session_state["agent_elements"][tabs] = agent_elements
                    break

    elif edge_action == "Delete Edge":
        edge_to_delete = st.selectbox("Select Edge to Delete", [f"{edge['data']['source']} -> {edge['data']['target']}" for edge in agent_elements['edges']])
        if st.button(f"Delete Edge '{edge_to_delete}'"):
            agent_elements['edges'] = [edge for edge in agent_elements['edges'] if f"{edge['data']['source']} -> {edge['data']['target']}" != edge_to_delete]
            st.success(f"Edge '{edge_to_delete}' deleted successfully!")
            st.session_state["agent_elements"][tabs] = agent_elements

# Display updated workflow after edits
st.markdown("### Updated Workflow Visualization")
st_link_analysis(agent_elements, "cose", node_styles, edge_styles)

