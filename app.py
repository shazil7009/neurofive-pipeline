import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load local environment variables if .env exists
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Agentic Pipeline | Neurofive",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS for Dark Green Header, Black Theme, and Highly Prominent Highlighted Tabs
st.markdown(
    """
    <style>
    /* Global App Dark Background */
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    
    /* Custom Dark Green Header Banner */
    .header-container {
        background-color: #0f291e;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        border: 1px solid #164e33;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    /* Neon Green Neurofive Badge */
    .header-badge {
        color: #39ff14; /* Neon Green */
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.75rem;
    }

    .header-title {
        color: #ffffff;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .header-desc {
        color: #f3f4f6;
        font-size: 1.1rem;
        font-weight: 400;
        line-height: 1.5;
    }

    /* Text input label styling (prominent white text above bar) */
    .stTextInput label {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* Text input styling for dark theme and white text */
    .stTextInput input {
        background-color: #121826;
        color: #ffffff !important;
        border: 1px solid #374151;
    }
    
    /* Placeholder text styling */
    .stTextInput input::placeholder {
        color: #9ca3af !important;
        opacity: 1;
    }
    
    /* Action Button styling */
    .stButton button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
    }

    /* Highly Prominent Tabs Container & Styling */
    div[data-testid="stTabs"] {
        background-color: #121826;
        padding: 0.75rem;
        border-radius: 12px;
        border: 1px solid #374151;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    }

    div[data-testid="stTabs"] button {
        background-color: #1a2234 !important;
        border: 1px solid #4b5563 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        margin-right: 8px !important;
    }
    
    div[data-testid="stTabs"] button p {
        color: #ff4d4d !important; /* Prominent red text */
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }

    /* Active Tab Styling - Strong Red Highlight & Glow */
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #2d1515 !important;
        border: 2px solid #ff3333 !important;
    }
    
    div[data-testid="stTabs"] button[aria-selected="true"] p {
        color: #ff1a1a !important; /* Brighter active red */
        text-shadow: 0 0 8px rgba(255, 51, 51, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Groq Client safely
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key and "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
    if not api_key:
        st.error("Groq API Key not found! Please check your .env or Streamlit secrets.")
        st.stop()
    return Groq(api_key=api_key)

client = get_groq_client()
MODEL_NAME = "llama-3.3-70b-versatile"

# Custom Dark Green Header Section with Neon Green Neurofive Tag
st.markdown(
    """
    <div class="header-container">
        <div class="header-badge">⚡ NEUROFIVE INTERNSHIP · DUAL AGENT PIPELINE</div>
        <div class="header-title">Two Agents, One Pipeline</div>
        <div class="header-desc">
            Agent 1 (Writer) drafts. Agent 2 (Editor/Critic) reviews and refines it. Agent 1's output becomes Agent 2's input — no human in between.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Topic Input Section
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "Enter a topic for the agents to work on:",
        placeholder="e.g., Why remote work is here to stay",
    )

with col2:
    st.write("")
    st.write("")
    run_btn = st.button("Run Pipeline", use_container_width=True)

# Agent Functions
def run_writer(topic_text):
    system_prompt = (
        "You are an expert technical researcher and content writer. "
        "Write a clear, detailed, and structured initial draft on the given topic."
    )
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write a comprehensive draft about: {topic_text}"}
        ],
        temperature=0.7,
        max_tokens=800,
    )
    return response.choices[0].message.content

def run_editor(topic_text, draft_text):
    system_prompt = (
        "You are a strict, professional Senior Technical Editor. "
        "Review the provided draft, fix structural flaws, enhance tone and clarity, "
        "and provide a publication-ready version."
    )
    user_prompt = f"Topic: {topic_text}\n\nDraft:\n{draft_text}\n\nProvide the refined text."
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=900,
    )
    return response.choices[0].message.content

# Execution Logic
if run_btn:
    if not topic.strip():
        st.warning("Please enter a valid topic first!")
    else:
        with st.status("🔄 Multi-Agent Pipeline in progress...", expanded=True) as status:
            st.write("agent 1 [Writer] is crafting the initial draft...")
            raw_draft = run_writer(topic)
            
            st.write("agent 2 [Editor/Critic] is reviewing and polishing the draft...")
            final_output = run_editor(topic, raw_draft)
            
            status.update(label="Pipeline execution completed successfully!", state="complete", expanded=False)

        # Display Results in Clean Tabs with prominent highlighted red container styling
        tab1, tab2, tab3 = st.tabs(["📝 Agent 1 Draft (Raw)", "✨ Agent 2 Final (Polished)", "🔍 What Changed"])
        
        with tab1:
            st.subheader("Initial Writer Output")
            st.write(raw_draft)
            
        with tab2:
            st.subheader("Final Refined Output")
            st.write(final_output)
            
        with tab3:
            st.subheader("Editor's Overview")
            st.markdown(
                """
                <div style="background-color: #121826; border: 1px solid #374151; padding: 1.2rem; border-radius: 8px; color: #ffffff; font-size: 1.05rem; line-height: 1.6;">
                    <b>Overview:</b> The Editor agent optimized the flow, removed redundancies, elevated the professional tone, and structured the final output for high readability.
                </div>
                """,
                unsafe_allow_html=True
            )