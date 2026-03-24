import streamlit as st
import uuid

# --- PAGE CONFIG & CUSTOM CSS ---
st.set_page_config(page_title="Offline To-Do List", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f3f4f6; }
    .stCheckbox label { color: #f3f4f6 !important; }
    .completed-task { text-decoration: line-through; opacity: 0.6; color: #9ca3af; }
    div.stButton > button {
        width: 100%; border-radius: 8px; font-weight: bold;
    }
    .task-container {
        background-color: #1f2937; padding: 10px; border-radius: 10px; 
        border: 1px solid #374151; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'sessions' not in st.session_state:
    st.session_state.sessions = {"Default": []}
if 'current_session' not in st.session_state:
    st.session_state.current_session = "Default"
if 'bin' not in st.session_state:
    st.session_state.bin = []

# --- APP HEADER ---
st.title("📝 Offline To-Do List")

# --- SESSION MANAGEMENT ---
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    session_list = list(st.session_state.sessions.keys())
    selected = st.selectbox("Select Session", session_list, index=session_list.index(st.session_state.current_session))
    st.session_state.current_session = selected

with col2:
    if st.button("+ New Session"):
        new_name = f"Session {len(st.session_state.sessions) + 1}"
        st.session_state.sessions[new_name] = []
        st.rerun()

with col3:
    if st.button("🗑️ Delete"):
        if st.session_state.current_session != "Default":
            del st.session_state.sessions[st.session_state.current_session]
            st.session_state.current_session = "Default"
            st.rerun()

st.caption(f"Active Session: {st.session_state.current_session}")

# --- INPUT FORM ---
with st.form("todo_form", clear_on_submit=True):
    new_task = st.text_input("Add a new task...", placeholder="What needs to be done?")
    submit = st.form_submit_button("Add Task")
    
    if submit and new_task:
        task_obj = {"id": str(uuid.uuid4()), "text": new_task, "done": False}
        st.session_state.sessions[st.session_state.current_session].append(task_obj)
        st.rerun()

# --- TASKS LIST ---
st.subheader("Tasks")
current_tasks = st.session_state.sessions[st.session_state.current_session]

if not current_tasks:
    st.info("No tasks yet.")
else:
    for idx, task in enumerate(current_tasks):
        cols = st.columns([0.1, 0.7, 0.2])
        # Checkbox for completion
        completed = cols[0].checkbox("", value=task['done'], key=f"check_{task['id']}")
        st.session_state.sessions[st.session_state.current_session][idx]['done'] = completed
        
        # Task Text
        display_text = f"~~{task['text']}~~" if completed else task['text']
        cols[1].markdown(f"**{display_text}**")
        
        # Move to Bin
        if cols[2].button("🗑️", key=f"del_{task['id']}"):
            st.session_state.bin.append(current_tasks.pop(idx))
            st.rerun()

# --- RECYCLING BIN ---
st.divider()
st.subheader("♻️ Recycling Bin")

if not st.session_state.bin:
    st.text("Bin is empty.")
else:
    for idx, b_task in enumerate(st.session_state.bin):
        b_cols = st.columns([0.8, 0.1, 0.1])
        b_cols[0].text(b_task['text'])
        
        if b_cols[1].button("⏪", key=f"res_{b_task['id']}", help="Restore"):
            st.session_state.sessions[st.session_state.current_session].append(st.session_state.bin.pop(idx))
            st.rerun()
            
        if b_cols[2].button("❌", key=f"perm_{b_task['id']}", help="Permanent Delete"):
            st.session_state.bin.pop(idx)
            st.rerun()

if st.button("Empty Bin"):
    st.session_state.bin = []
    st.rerun()
