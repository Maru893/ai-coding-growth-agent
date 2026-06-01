from pathlib import Path

import streamlit as st

from utils.json_handler import load_json, save_json
from utils.planner_rules import generate_weekly_plan
from utils.markdown_exporter import export_weekly_plan_to_markdown
from pages.dashboard import render_dashboard
from pages.roadmap import render_roadmap
from pages.profile import render_profile
from pages.skill_tracker import render_skill_tracker
from pages.weekly_focus import render_weekly_focus
from pages.daily_goal import render_daily_goal
from pages.projects import render_projects
from pages.technical_notes import render_technical_notes
from pages.progress_tracker import render_progress_tracker
from pages.checklist import render_checklist
from pages.weekly_plan import render_weekly_plan

DATA_DIR = Path("data")
PROFILE_PATH = DATA_DIR / "profile.json"
WEEKLY_PLANS_PATH = DATA_DIR / "weekly_plans.json"
PROGRESS_PATH = DATA_DIR / "progress.json"
PROJECTS_PATH = DATA_DIR / "projects.json"
ROADMAP_PATH = DATA_DIR / "roadmap.json"
CHECKLISTS_PATH = DATA_DIR / "checklists.json"
SKILLS_PATH = DATA_DIR / "skills.json"
WEEKLY_FOCUS_PATH = DATA_DIR / "weekly_focus.json"
DAILY_GOALS_PATH = DATA_DIR / "daily_goals.json"
TECHNICAL_NOTES_PATH = DATA_DIR / "technical_notes.json"


st.set_page_config(
    page_title="AI Coding Growth Agent",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
        .main {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        h1 {
            color: #0F172A;
            font-weight: 800;
            letter-spacing: -0.03em;
        }

        h2, h3 {
            color: #1E293B;
            font-weight: 700;
        }

        p, label, span {
            font-size: 0.98rem;
        }

        .stButton > button {
            width: 100%;
            border-radius: 10px;
            height: 3rem;
            font-weight: 600;
            border: 1px solid #CBD5E1;
        }

        .stButton > button:hover {
            border: 1px solid #0F172A;
        }

        .stTextInput > div > div > input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] > div {
            border-radius: 10px;
        }

        section[data-testid="stSidebar"] {
            background-color: #F8FAFC;
            border-right: 1px solid #E2E8F0;
        }
            
        section[data-testid="stSidebar"] * {
            color: #0F172A !important;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] span {
            color: #0F172A !important;
        }

        section[data-testid="stSidebar"] h1 {
            font-size: 1.2rem;
            font-weight: 800;
        }
            
        section[data-testid="stSidebar"] [role="radiogroup"] label {
            color: #0F172A !important;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] span {
            color: #0F172A !important;
        }

        .stExpander {
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }

        .metric-card {
            background-color: #F8FAFC;
            padding: 1rem;
            border-radius: 14px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            text-align: center;
            margin-bottom: 0.8rem;
        }

        .metric-label {
            color: #64748B;
            font-size: 0.85rem;
            margin-bottom: 0.3rem;
        }

        .metric-value {
            color: #0F172A;
            font-size: 1.7rem;
            font-weight: 800;
        }

        .info-card {
            background-color: #FFFFFF;
            padding: 1.2rem;
            border-radius: 14px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            margin-bottom: 1rem;
        }

        .page-caption {
            color: #64748B;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

def render_metric_card(title, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def open_info_card():
    st.markdown('<div class="info-card">', unsafe_allow_html=True)


def close_info_card():
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.title("Navigazione")

page = st.sidebar.radio(
    "Vai a",
    [
        "Dashboard",
        "Profilo",
        "Piano settimanale",
        "Checklist",
        "Obiettivo del giorno",
        "Focus settimana",
        "Progress Tracker",
        "Progetti",
        "Roadmap",
        "Skill Tracker",
        "Note Tecniche"
    ]
)

if page == "Dashboard":
    render_dashboard(
        PROFILE_PATH,
        WEEKLY_PLANS_PATH,
        PROGRESS_PATH,
        PROJECTS_PATH,
        CHECKLISTS_PATH,
        SKILLS_PATH,
        WEEKLY_FOCUS_PATH,
        DAILY_GOALS_PATH,
        TECHNICAL_NOTES_PATH
    )



# logica Profilo

elif page == "Profilo":
    render_profile(PROFILE_PATH)

# logica Piano Settimanale


elif page == "Piano settimanale":
    render_weekly_plan(
        WEEKLY_PLANS_PATH,
        SKILLS_PATH,
        WEEKLY_FOCUS_PATH
    )

# logica Checklist

elif page == "Checklist":
    render_checklist(WEEKLY_PLANS_PATH, CHECKLISTS_PATH)

# logica Progress Tracker

elif page == "Progress Tracker":
    render_progress_tracker(PROGRESS_PATH)

# logica Progetti

elif page == "Progetti":
    render_projects(PROJECTS_PATH)

# Logica Roadmap

elif page == "Roadmap":
    render_roadmap(ROADMAP_PATH)

# Logica Skill Tracker

elif page == "Skill Tracker":
    render_skill_tracker(SKILLS_PATH)   

# Logica Focus Settimana

elif page == "Focus settimana":
    render_weekly_focus(WEEKLY_FOCUS_PATH)


# Logica Obiettivo del giorno

elif page == "Obiettivo del giorno":
    render_daily_goal(DAILY_GOALS_PATH)

# Logica Note Tecniche 

elif page == "Note Tecniche":
    render_technical_notes(TECHNICAL_NOTES_PATH)