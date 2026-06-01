from pathlib import Path

import streamlit as st

from utils.json_handler import load_json, save_json
from utils.planner_rules import generate_weekly_plan
from utils.markdown_exporter import export_weekly_plan_to_markdown


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
    st.title("Dashboard")
    st.caption("Controlla il riepilogo del tuo percorso, il focus attuale e le ultime attività salvate.")

    profile = load_json(PROFILE_PATH, {})
    weekly_plans = load_json(WEEKLY_PLANS_PATH, [])
    progress_entries = load_json(PROGRESS_PATH, [])
    projects = load_json(PROJECTS_PATH, [])
    checklists = load_json(CHECKLISTS_PATH, [])
    skills = load_json(SKILLS_PATH, [])
    weekly_focus = load_json(WEEKLY_FOCUS_PATH, [])
    daily_goals = load_json(DAILY_GOALS_PATH, [])
    technical_notes = load_json(TECHNICAL_NOTES_PATH, [])

    st.header("Riepilogo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card("Piani", len(weekly_plans))

    with col2:
        render_metric_card("Progressi", len(progress_entries))

    with col3:
        render_metric_card("Progetti", len(projects))

    with col4:
        render_metric_card("Checklist", len(checklists))

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        render_metric_card("Skill", len(skills))

    with col6:
        render_metric_card("Focus", len(weekly_focus))

    with col7:
        render_metric_card("Obiettivi", len(daily_goals))

    with col8:
        render_metric_card("Note", len(technical_notes))

    st.header("Focus operativo")

    focus_col, goal_col = st.columns(2)

    with focus_col:
        with st.container(border=True):
            st.subheader("Focus della settimana")

            if weekly_focus:
                last_focus = weekly_focus[-1]
                st.write(f"Skill focus: {last_focus.get('skill_focus', 'Non impostata')}")
                st.write(f"Progetto focus: {last_focus.get('project_focus', 'Non impostato')}")
                st.write(f"Obiettivo: {last_focus.get('weekly_goal', 'Non impostato')}")
                st.write(f"Priorità: {last_focus.get('priority', 'Non impostata')}")
            else:
                st.info("Non hai ancora impostato un focus settimanale.")

    with goal_col:
        with st.container(border=True):
            st.subheader("Ultimo obiettivo del giorno")

            if daily_goals:
                last_daily_goal = daily_goals[-1]
                st.write(f"Tempo disponibile: {last_daily_goal.get('available_time', 'Non impostato')}")
                st.write(f"Energia: {last_daily_goal.get('energy', 'Non impostata')}")
                st.write(f"Tipo attività: {last_daily_goal.get('activity_type', 'Non impostato')}")
                st.write(f"Obiettivo: {last_daily_goal.get('daily_goal', 'Non impostato')}")
                st.write(f"Prossima azione: {last_daily_goal.get('next_action', 'Non impostata')}")
            else:
                st.info("Non hai ancora salvato obiettivi del giorno.")

    st.header("Ultime attività")

    plan_col, project_col = st.columns(2)

    with plan_col:
        with st.container(border=True):
            st.subheader("Ultimo piano settimanale")

            if weekly_plans:
                last_plan = weekly_plans[-1]
                st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
                st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")
                st.write(f"Task tecnico: {last_plan.get('plan', {}).get('technical_task', 'Non impostato')}")
                st.write(f"Output GitHub: {last_plan.get('github_output', 'Non impostato')}")
            else:
                st.info("Non hai ancora generato piani settimanali.")

    with project_col:
        with st.container(border=True):
            st.subheader("Ultimo progetto")

            if projects:
                last_project = projects[-1]
                st.write(f"Nome: {last_project.get('name', 'Non impostato')}")
                st.write(f"Stato: {last_project.get('status', 'Non impostato')}")
                st.write(f"Prossima azione: {last_project.get('next_action', 'Non impostato')}")
            else:
                st.info("Non hai ancora salvato progetti.")

    skill_col, note_col = st.columns(2)

    with skill_col:
        with st.container(border=True):
            st.subheader("Ultima skill salvata")

            if skills:
                last_skill = skills[-1]
                st.write(f"Skill: {last_skill.get('skill', 'Non impostata')}")
                st.write(f"Livello: {last_skill.get('level', 'Non impostato')} su 5")
                st.write(f"Sicurezza: {last_skill.get('confidence', 'Non impostata')} su 5")
                st.write(f"Prossima azione: {last_skill.get('next_action', 'Non impostata')}")
            else:
                st.info("Non hai ancora salvato skill.")

    with note_col:
        with st.container(border=True):
            st.subheader("Ultima nota tecnica")

            if technical_notes:
                last_note = technical_notes[-1]
                st.write(f"Categoria: {last_note.get('category', 'Non impostata')}")
                st.write(f"Titolo: {last_note.get('title', 'Non impostato')}")
                st.write(f"Cosa ho imparato: {last_note.get('lesson', 'Non impostato')}")
            else:
                st.info("Non hai ancora salvato note tecniche.")

    st.header("Percorso tecnico")

    with st.container(border=True):
        st.subheader("Profilo")

        st.write(f"Nome: {profile.get('name', 'Non impostato')}")
        st.write(f"Livello Python: {profile.get('python_level', 'Non impostato')}")
        st.write(f"Ore settimanali: {profile.get('weekly_hours', 'Non impostato')}")
        st.write(f"Focus principale: {profile.get('main_focus', 'Non impostato')}")

# logica Profilo


elif page == "Profilo":
    st.title("AI Coding Growth Agent")
    st.caption("Gestisci le informazioni di base del tuo percorso nel Coding AI.")
    st.write("Il tuo planner personale per crescere nel Coding AI.")

    profile = load_json(PROFILE_PATH, {})

    st.header("Profilo")

    name = st.text_input("Nome", value=profile.get("name", "Marouane"))

    current_stack_text = st.text_input(
        "Stack attuale, separato da virgole",
        value=", ".join(profile.get("current_stack", ["Laravel", "PHP", "JavaScript"]))
    )

    python_level_options = ["zero", "base", "intermedio"]

    python_level = st.selectbox(
        "Livello Python",
        python_level_options,
        index=python_level_options.index(profile.get("python_level", "base"))
    )

    weekly_hours_options = ["1-2", "3-5", "6-8", "9+"]

    weekly_hours = st.selectbox(
        "Ore disponibili a settimana",
        weekly_hours_options,
        index=weekly_hours_options.index(profile.get("weekly_hours", "3-5"))
    )

    goal_3_months = st.text_area(
        "Obiettivo nei prossimi 3 mesi",
        value=profile.get(
            "goal_3_months",
            "iniziare a guadagnare qualcosa nel settore Coding AI"
        )
    )

    if st.button("Salva profilo"):
        updated_profile = {
            "name": name,
            "current_stack": [
                item.strip()
                for item in current_stack_text.split(",")
                if item.strip()
            ],
            "python_level": python_level,
            "weekly_hours": weekly_hours,
            "goal_3_months": goal_3_months,
            "preferred_interface": "Streamlit",
            "storage": "JSON",
            "api_keys_available": False,
            "project_type": "personale",
            "main_focus": "Coding AI"
        }

        save_json(PROFILE_PATH, updated_profile)
        st.success("Profilo salvato correttamente.")

    st.subheader("Profilo attuale")
    st.json(load_json(PROFILE_PATH, {}))

# logica Piano Settimanale


elif page == "Piano settimanale":
    st.title("Piano settimanale")
    st.caption("Genera un piano pratico basato su tempo, energia, focus, skill e obiettivo della settimana.")

    with st.form("weekly_plan_form"):
        weekly_hours_input = st.selectbox(
            "Ore disponibili questa settimana",
            ["1-2", "3-5", "6-8", "9+"],
            index=1
        )

        energy_input = st.slider(
            "Energia mentale",
            min_value=1,
            max_value=5,
            value=3
        )

        focus_input = st.selectbox(
            "Focus della settimana",
            ["Python", "Streamlit", "JSON", "AI Logic", "GitHub"]
        )

        goal_input = st.text_input(
            "Obiettivo pratico della settimana",
            value="migliorare il mio AI Coding Growth Agent"
        )

        current_project_input = st.text_input(
            "Progetto attuale",
            value="AI Coding Growth Agent"
        )

        submitted_weekly_plan = st.form_submit_button("Genera piano settimanale")

    if submitted_weekly_plan:
        skills = load_json(SKILLS_PATH, [])
        weekly_focus = load_json(WEEKLY_FOCUS_PATH, [])

        last_skill = skills[-1] if skills else None
        last_weekly_focus = weekly_focus[-1] if weekly_focus else None

        weekly_plan = generate_weekly_plan(
            weekly_hours_input,
            energy_input,
            focus_input,
            goal_input,
            current_project_input,
            last_skill,
            last_weekly_focus
)

        existing_plans = load_json(WEEKLY_PLANS_PATH, [])
        existing_plans.append(weekly_plan)
        save_json(WEEKLY_PLANS_PATH, existing_plans)

        st.success("Piano settimanale generato e salvato.")
        

        st.subheader("Piano generato")

        st.write(f"Focus: {weekly_plan['focus']}")
        st.write(f"Obiettivo: {weekly_plan['goal']}")
        st.write(f"Progetto attuale: {weekly_plan['current_project']}")

        st.markdown("### Distribuzione tempo")
        st.write(f"Studio: {weekly_plan['plan']['study']}")
        st.write(f"Pratica: {weekly_plan['plan']['practice']}")
        st.write(f"Documentazione: {weekly_plan['plan']['documentation']}")

        st.markdown("### Task tecnico")
        st.write(weekly_plan["plan"]["technical_task"])

        st.markdown("### Checklist")
        for item in weekly_plan["checklist"]:
            st.checkbox(item, value=False)

        st.markdown("### Output GitHub")
        st.write(weekly_plan["github_output"])

        st.markdown("### Possibile uso monetizzabile")
        st.write(weekly_plan["money_path"])

        st.markdown("### Raccomandazione skill")
        st.write(weekly_plan["skill_recommendation"])

        st.markdown("### Focus settimanale collegato")
        st.write(weekly_plan["weekly_focus_recommendation"])
    

    st.subheader("Storico piani settimanali")

    saved_plans = load_json(WEEKLY_PLANS_PATH, [])


    if saved_plans:
        for index, plan in enumerate(reversed(saved_plans), start=1):
            with st.expander(f"Piano {index} - {plan.get('focus', 'Focus non impostato')}"):
                st.write(f"Ore: {plan.get('hours', 'Non impostato')}")
                st.write(f"Energia: {plan.get('energy', 'Non impostata')}")
                st.write(f"Obiettivo: {plan.get('goal', 'Non impostato')}")
                st.write(f"Task: {plan.get('plan', {}).get('technical_task', 'Non impostato')}")
                st.write(f"Output GitHub: {plan.get('github_output', 'Non impostato')}")
                st.write(f"Raccomandazione skill: {plan.get('skill_recommendation', 'Non impostata')}")
                st.write(f"Focus collegato: {plan.get('weekly_focus_recommendation', 'Non impostato')}")
    else:
        st.info("Non hai ancora salvato piani settimanali.")

    st.subheader("Gestione piani")

    plans_to_manage = load_json(WEEKLY_PLANS_PATH, [])

    if plans_to_manage:
        if st.button("Elimina ultimo piano salvato"):
            removed_plan = plans_to_manage.pop()
            save_json(WEEKLY_PLANS_PATH, plans_to_manage)

            st.warning("Ultimo piano eliminato.")
            st.write(f"Piano eliminato: {removed_plan.get('focus', 'Focus non impostato')}")
    else:
        st.info("Non ci sono piani da eliminare.")    

    st.subheader("Export ultimo piano")

    saved_plans_for_export = load_json(WEEKLY_PLANS_PATH, [])

    if saved_plans_for_export:
            if st.button("Esporta ultimo piano in Markdown"):
                last_plan = saved_plans_for_export[-1]
                exported_file = export_weekly_plan_to_markdown(last_plan)
                st.success(f"Piano esportato in: {exported_file}")
    else:
            st.info("Genera almeno un piano prima di esportare.")

# logica Checklist

elif page == "Checklist":
    st.title("Checklist")
    st.caption("Trasforma l’ultimo piano settimanale in task completabili e salva l’avanzamento.")

    weekly_plans = load_json(WEEKLY_PLANS_PATH, [])
    saved_checklists = load_json(CHECKLISTS_PATH, [])

    if not weekly_plans:
        st.info("Genera prima un piano settimanale.")
    else:
        last_plan = weekly_plans[-1]
        checklist_items = last_plan.get("checklist", [])

        st.subheader("Checklist dell'ultimo piano")
        st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
        st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")

        completed_items = []

        for index, item in enumerate(checklist_items):
            is_checked = st.checkbox(item, key=f"checklist_item_{index}")

            if is_checked:
                completed_items.append(item)

        notes_input = st.text_area(
            "Note sulla checklist",
            value=""
        )

        if st.button("Salva checklist"):
            checklist_entry = {
                "focus": last_plan.get("focus", "Non impostato"),
                "goal": last_plan.get("goal", "Non impostato"),
                "completed_items": completed_items,
                "total_items": len(checklist_items),
                "completion_count": len(completed_items),
                "notes": notes_input
            }

            saved_checklists.append(checklist_entry)
            save_json(CHECKLISTS_PATH, saved_checklists)

            st.success("Checklist salvata correttamente.")

            st.write(f"Task completati: {len(completed_items)} su {len(checklist_items)}")

        st.subheader("Storico checklist")

        if saved_checklists:
            for index, checklist in enumerate(reversed(saved_checklists), start=1):
                with st.expander(f"Checklist {index} - {checklist.get('focus', 'Focus non impostato')}"):
                    st.write(f"Obiettivo: {checklist.get('goal', 'Non impostato')}")
                    st.write(
                        f"Completamento: {checklist.get('completion_count', 0)} "
                        f"su {checklist.get('total_items', 0)}"
                    )

                    st.write("Task completati:")
                    for item in checklist.get("completed_items", []):
                        st.write(f"- {item}")

                    st.write(f"Note: {checklist.get('notes', '')}")
        else:
            st.info("Non hai ancora salvato checklist.")

        st.subheader("Gestione checklist")

        checklists_to_manage = load_json(CHECKLISTS_PATH, [])

        if checklists_to_manage:
            if st.button("Elimina ultima checklist salvata"):
                removed_checklist = checklists_to_manage.pop()
                save_json(CHECKLISTS_PATH, checklists_to_manage)

                st.warning("Ultima checklist eliminata.")
                st.write(f"Checklist eliminata: {removed_checklist.get('focus', 'Focus non impostato')}")
        else:
            st.info("Non ci sono checklist da eliminare.")

# logica Progress Tracker

elif page == "Progress Tracker":
    st.title("Progress Tracker")
    st.caption("Registra cosa hai completato, dove ti sei bloccato, cosa hai imparato e qual è la prossima azione.")


    with st.form("progress_form"):
        week_input = st.text_input(
            "Settimana di riferimento",
            value="Settimana 1"
        )

        completed_tasks_input = st.text_area(
            "Task completati",
            value="Ho creato il profilo e il generatore di piano settimanale."
        )

        blocked_input = st.text_area(
            "Dove mi sono bloccato?",
            value=""
        )

        learned_input = st.text_area(
            "Cosa ho imparato?",
            value=""
        )

        next_action_input = st.text_input(
            "Prossima azione",
            value="Migliorare la struttura del codice."
        )

        submitted_progress = st.form_submit_button("Salva progresso")

    if submitted_progress:
        progress_entry = {
            "week": week_input,
            "completed_tasks": completed_tasks_input,
            "blocked": blocked_input,
            "learned": learned_input,
            "next_action": next_action_input
        }

        existing_progress = load_json(PROGRESS_PATH, [])
        existing_progress.append(progress_entry)
        save_json(PROGRESS_PATH, existing_progress)

        st.success("Progresso salvato correttamente.")

        st.subheader("Progresso appena salvato")
        st.write(f"Settimana: {progress_entry['week']}")
        st.write(f"Task completati: {progress_entry['completed_tasks']}")
        st.write(f"Blocco: {progress_entry['blocked']}")
        st.write(f"Cosa ho imparato: {progress_entry['learned']}")
        st.write(f"Prossima azione: {progress_entry['next_action']}")

        st.subheader("Storico progressi")

        saved_progress = load_json(PROGRESS_PATH, [])

        if saved_progress:
            for index, progress in enumerate(reversed(saved_progress), start=1):
                with st.expander(f"Progresso {index} - {progress.get('week', 'Settimana non impostata')}"):
                    st.write(f"Task completati: {progress.get('completed_tasks', 'Non impostato')}")
                    st.write(f"Blocco: {progress.get('blocked', 'Nessun blocco indicato')}")
                    st.write(f"Cosa ho imparato: {progress.get('learned', 'Non impostato')}")
                    st.write(f"Prossima azione: {progress.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato progressi.")

        st.subheader("Gestione progressi")

        progress_to_manage = load_json(PROGRESS_PATH, [])

        if progress_to_manage:
            if st.button("Elimina ultimo progresso salvato"):
                removed_progress = progress_to_manage.pop()
                save_json(PROGRESS_PATH, progress_to_manage)

                st.warning("Ultimo progresso eliminato.")
                st.write(f"Progresso eliminato: {removed_progress.get('week', 'Settimana non impostata')}")
            else:
                st.info("Non ci sono progressi da eliminare.")

# logica Progetti

elif page == "Progetti":
    st.title("Progetti")
    st.caption("Organizza i mini progetti del tuo percorso, collegandoli a skill, stato, problema risolto e possibile uso monetizzabile.")

    st.header("Nuovo progetto")

    with st.container(border=True):
        with st.form("project_form"):
            project_name_input = st.text_input(
                "Nome progetto",
                value="AI Coding Growth Agent"
            )

            project_goal_input = st.text_area(
                "Problema che risolve",
                value="Aiutarmi a pianificare studio, pratica e progressi nel Coding AI."
            )

            skill_input = st.selectbox(
                "Skill principale allenata",
                ["Python", "Streamlit", "JSON", "AI Logic", "GitHub", "FastAPI", "LLM API", "RAG"]
            )

            project_status_input = st.selectbox(
                "Stato progetto",
                ["Idea", "In sviluppo", "MVP funzionante", "Da migliorare", "Completato"]
            )

            monetization_input = st.text_area(
                "Possibile uso monetizzabile",
                value="Potrebbe diventare una dashboard personalizzata per studenti, junior developer o freelance."
            )

            next_action_input = st.text_input(
                "Prossima azione sul progetto",
                value="Migliorare la struttura e aggiungere una nuova feature."
            )

            submitted_project = st.form_submit_button("Salva progetto")

    if submitted_project:
        project_entry = {
            "name": project_name_input,
            "problem_solved": project_goal_input,
            "main_skill": skill_input,
            "status": project_status_input,
            "monetization": monetization_input,
            "next_action": next_action_input
        }

        existing_projects = load_json(PROJECTS_PATH, [])
        existing_projects.append(project_entry)
        save_json(PROJECTS_PATH, existing_projects)

        st.success("Progetto salvato correttamente.")

    saved_projects = load_json(PROJECTS_PATH, [])

    st.header("Ultimo progetto salvato")

    with st.container(border=True):
        if saved_projects:
            last_project = saved_projects[-1]
            st.write(f"Nome: {last_project.get('name', 'Non impostato')}")
            st.write(f"Problema che risolve: {last_project.get('problem_solved', 'Non impostato')}")
            st.write(f"Skill principale: {last_project.get('main_skill', 'Non impostata')}")
            st.write(f"Stato: {last_project.get('status', 'Non impostato')}")
            st.write(f"Possibile uso monetizzabile: {last_project.get('monetization', 'Non impostato')}")
            st.write(f"Prossima azione: {last_project.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato progetti.")

    st.header("Storico progetti")

    if saved_projects:
        for index, project in enumerate(reversed(saved_projects), start=1):
            with st.expander(f"Progetto {index} - {project.get('name', 'Nome non impostato')}"):
                st.write(f"Problema che risolve: {project.get('problem_solved', 'Non impostato')}")
                st.write(f"Skill principale: {project.get('main_skill', 'Non impostata')}")
                st.write(f"Stato: {project.get('status', 'Non impostato')}")
                st.write(f"Possibile uso monetizzabile: {project.get('monetization', 'Non impostato')}")
                st.write(f"Prossima azione: {project.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato progetti.")

    st.header("Gestione progetti")

    with st.container(border=True):
        projects_to_manage = load_json(PROJECTS_PATH, [])

        if projects_to_manage:
            if st.button("Elimina ultimo progetto salvato"):
                removed_project = projects_to_manage.pop()
                save_json(PROJECTS_PATH, projects_to_manage)

                st.warning("Ultimo progetto eliminato.")
                st.write(f"Progetto eliminato: {removed_project.get('name', 'Nome non impostato')}")
        else:
            st.info("Non ci sono progetti da eliminare.")

# Logica Roadmap

elif page == "Roadmap":

    st.title("Roadmap")
    st.caption("Visualizza la direzione dei prossimi mesi, con focus, obiettivi, skill da allenare e progetti principali.")

    roadmap = load_json(ROADMAP_PATH, [])

    if roadmap:
        for item in roadmap:
            with st.expander(f"{item.get('month', 'Mese non impostato')} - {item.get('focus', 'Focus non impostato')}"):
                st.write(f"Obiettivo: {item.get('goal', 'Non impostato')}")
                st.write(f"Progetto principale: {item.get('project', 'Non impostato')}")

                st.write("Skill da allenare:")
                for skill in item.get("skills", []):
                    st.write(f"- {skill}")
    else:
        st.info("Roadmap non ancora configurata.")

# Logica Skill Tracker

elif page == "Skill Tracker":
    st.title("Skill Tracker")
    st.caption("Monitora le competenze che stai costruendo nel tuo percorso di Coding AI.")

    st.header("Nuova skill")

    with st.container(border=True):
        with st.form("skill_form"):
            skill_name_input = st.selectbox(
                "Skill",
                [
                    "Python",
                    "Streamlit",
                    "JSON",
                    "Git",
                    "GitHub",
                    "FastAPI",
                    "LLM API",
                    "Prompt Engineering",
                    "RAG",
                    "Agentic AI",
                    "Testing",
                    "Deployment"
                ]
            )

            skill_level_input = st.slider(
                "Livello attuale",
                min_value=1,
                max_value=5,
                value=1
            )

            confidence_input = st.slider(
                "Sicurezza personale su questa skill",
                min_value=1,
                max_value=5,
                value=1
            )

            notes_input = st.text_area(
                "Note",
                value=""
            )

            next_action_input = st.text_input(
                "Prossima azione",
                value="Fare un piccolo esercizio pratico."
            )

            submitted_skill = st.form_submit_button("Salva skill")

    if submitted_skill:
        skill_entry = {
            "skill": skill_name_input,
            "level": skill_level_input,
            "confidence": confidence_input,
            "notes": notes_input,
            "next_action": next_action_input
        }

        existing_skills = load_json(SKILLS_PATH, [])
        existing_skills.append(skill_entry)
        save_json(SKILLS_PATH, existing_skills)

        st.success("Skill salvata correttamente.")

    saved_skills = load_json(SKILLS_PATH, [])

    st.header("Ultima skill salvata")

    with st.container(border=True):
        if saved_skills:
            last_skill = saved_skills[-1]
            st.write(f"Skill: {last_skill.get('skill', 'Non impostata')}")
            st.write(f"Livello: {last_skill.get('level', 'Non impostato')} su 5")
            st.write(f"Sicurezza: {last_skill.get('confidence', 'Non impostata')} su 5")
            st.write(f"Note: {last_skill.get('notes', '')}")
            st.write(f"Prossima azione: {last_skill.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato skill.")

    st.header("Storico skill")

    if saved_skills:
        for index, skill in enumerate(reversed(saved_skills), start=1):
            with st.expander(f"Skill {index} - {skill.get('skill', 'Skill non impostata')}"):
                st.write(f"Livello: {skill.get('level', 'Non impostato')} su 5")
                st.write(f"Sicurezza: {skill.get('confidence', 'Non impostata')} su 5")
                st.write(f"Note: {skill.get('notes', '')}")
                st.write(f"Prossima azione: {skill.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato skill.")

    st.header("Gestione skill")

    with st.container(border=True):
        skills_to_manage = load_json(SKILLS_PATH, [])

        if skills_to_manage:
            if st.button("Elimina ultima skill salvata"):
                removed_skill = skills_to_manage.pop()
                save_json(SKILLS_PATH, skills_to_manage)

                st.warning("Ultima skill eliminata.")
                st.write(f"Skill eliminata: {removed_skill.get('skill', 'Skill non impostata')}")
        else:
            st.info("Non ci sono skill da eliminare.")

    st.header("Focus operativo")    

# Logica Focus Settimana

elif page == "Focus settimana":
    st.title("Focus settimana")
    st.caption("Definisci la skill, il progetto e la priorità principale della settimana.")

    st.header("Nuovo focus")

    with st.container(border=True):
        with st.form("weekly_focus_form"):
            skill_focus_input = st.selectbox(
                "Skill focus",
                [
                    "Python",
                    "Streamlit",
                    "JSON",
                    "Git",
                    "GitHub",
                    "FastAPI",
                    "LLM API",
                    "Prompt Engineering",
                    "RAG",
                    "Agentic AI",
                    "Testing",
                    "Deployment"
                ]
            )

            project_focus_input = st.text_input(
                "Progetto focus",
                value="AI Coding Growth Agent"
            )

            weekly_goal_input = st.text_area(
                "Obiettivo della settimana",
                value="Migliorare il progetto con una feature piccola e utile."
            )

            priority_input = st.selectbox(
                "Priorità",
                ["Bassa", "Media", "Alta"]
            )

            submitted_focus = st.form_submit_button("Salva focus settimanale")

    if submitted_focus:
        focus_entry = {
            "skill_focus": skill_focus_input,
            "project_focus": project_focus_input,
            "weekly_goal": weekly_goal_input,
            "priority": priority_input
        }

        existing_focus = load_json(WEEKLY_FOCUS_PATH, [])
        existing_focus.append(focus_entry)
        save_json(WEEKLY_FOCUS_PATH, existing_focus)

        st.success("Focus settimanale salvato correttamente.")

    saved_focus = load_json(WEEKLY_FOCUS_PATH, [])

    st.header("Ultimo focus salvato")

    with st.container(border=True):
        if saved_focus:
            last_focus = saved_focus[-1]
            st.write(f"Skill focus: {last_focus.get('skill_focus', 'Non impostata')}")
            st.write(f"Progetto focus: {last_focus.get('project_focus', 'Non impostato')}")
            st.write(f"Obiettivo: {last_focus.get('weekly_goal', 'Non impostato')}")
            st.write(f"Priorità: {last_focus.get('priority', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato focus settimanali.")

    st.header("Storico focus settimanali")

    if saved_focus:
        for index, focus in enumerate(reversed(saved_focus), start=1):
            with st.expander(f"Focus {index} - {focus.get('skill_focus', 'Skill non impostata')}"):
                st.write(f"Progetto: {focus.get('project_focus', 'Non impostato')}")
                st.write(f"Obiettivo: {focus.get('weekly_goal', 'Non impostato')}")
                st.write(f"Priorità: {focus.get('priority', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato focus settimanali.")

    st.header("Gestione focus")

    with st.container(border=True):
        focus_to_manage = load_json(WEEKLY_FOCUS_PATH, [])

        if focus_to_manage:
            if st.button("Elimina ultimo focus salvato"):
                removed_focus = focus_to_manage.pop()
                save_json(WEEKLY_FOCUS_PATH, focus_to_manage)

                st.warning("Ultimo focus eliminato.")
                st.write(f"Focus eliminato: {removed_focus.get('skill_focus', 'Skill non impostata')}")
        else:
            st.info("Non ci sono focus da eliminare.")


# Logica Obiettivo del giorno

elif page == "Obiettivo del giorno":
    st.title("Obiettivo del giorno")
    st.caption("Genera un micro obiettivo giornaliero in base al tempo e all’energia disponibili.")

    st.header("Nuovo obiettivo")

    with st.container(border=True):
        with st.form("daily_goal_form"):
            available_time_input = st.selectbox(
                "Tempo disponibile oggi",
                ["30 minuti", "60 minuti", "90 minuti", "2 ore", "3+ ore"]
            )

            energy_input = st.slider(
                "Energia di oggi",
                min_value=1,
                max_value=5,
                value=3
            )

            activity_type_input = st.selectbox(
                "Tipo attività",
                ["Studio", "Codice", "Debug", "Documentazione", "Refactor"]
            )

            current_focus_input = st.text_input(
                "Focus attuale",
                value="AI Coding Growth Agent"
            )

            submitted_daily_goal = st.form_submit_button("Genera obiettivo del giorno")

    if submitted_daily_goal:
        if available_time_input == "30 minuti":
            daily_goal = "Completa un micro task molto piccolo e chiaro."
        elif available_time_input == "60 minuti":
            daily_goal = "Studia un concetto e applicalo subito con un esercizio pratico."
        elif available_time_input == "90 minuti":
            daily_goal = "Costruisci o migliora una piccola feature del progetto."
        elif available_time_input == "2 ore":
            daily_goal = "Completa una feature semplice, testala e aggiorna le note."
        else:
            daily_goal = "Lavora su una feature più completa e documenta il risultato."

        if energy_input <= 2:
            next_action = "Fai un task leggero: rileggi codice, aggiorna README o sistema un file JSON."
        elif energy_input == 3:
            next_action = "Fai un task tecnico mirato senza aggiungere troppe cose nuove."
        else:
            next_action = "Costruisci una nuova feature o migliora una parte importante del progetto."

        if activity_type_input == "Studio":
            suggested_task = "Studia un concetto e scrivi 3 note pratiche."
        elif activity_type_input == "Codice":
            suggested_task = "Scrivi o migliora una funzione collegata al progetto."
        elif activity_type_input == "Debug":
            suggested_task = "Trova un errore, capisci la causa e annota la soluzione."
        elif activity_type_input == "Documentazione":
            suggested_task = "Aggiorna README o aggiungi spiegazioni al progetto."
        else:
            suggested_task = "Rendi il codice più leggibile senza cambiare il comportamento."

        daily_goal_entry = {
            "available_time": available_time_input,
            "energy": energy_input,
            "activity_type": activity_type_input,
            "current_focus": current_focus_input,
            "daily_goal": daily_goal,
            "suggested_task": suggested_task,
            "next_action": next_action
        }

        existing_daily_goals = load_json(DAILY_GOALS_PATH, [])
        existing_daily_goals.append(daily_goal_entry)
        save_json(DAILY_GOALS_PATH, existing_daily_goals)

        st.success("Obiettivo del giorno generato e salvato.")

    saved_daily_goals = load_json(DAILY_GOALS_PATH, [])

    st.header("Ultimo obiettivo salvato")

    with st.container(border=True):
        if saved_daily_goals:
            last_daily_goal = saved_daily_goals[-1]
            st.write(f"Tempo disponibile: {last_daily_goal.get('available_time', 'Non impostato')}")
            st.write(f"Energia: {last_daily_goal.get('energy', 'Non impostata')}")
            st.write(f"Tipo attività: {last_daily_goal.get('activity_type', 'Non impostato')}")
            st.write(f"Focus attuale: {last_daily_goal.get('current_focus', 'Non impostato')}")
            st.write(f"Obiettivo: {last_daily_goal.get('daily_goal', 'Non impostato')}")
            st.write(f"Task suggerito: {last_daily_goal.get('suggested_task', 'Non impostato')}")
            st.write(f"Prossima azione: {last_daily_goal.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato obiettivi del giorno.")

    st.header("Storico obiettivi del giorno")

    if saved_daily_goals:
        for index, goal in enumerate(reversed(saved_daily_goals), start=1):
            with st.expander(f"Obiettivo {index} - {goal.get('activity_type', 'Tipo non impostato')}"):
                st.write(f"Tempo disponibile: {goal.get('available_time', 'Non impostato')}")
                st.write(f"Energia: {goal.get('energy', 'Non impostata')}")
                st.write(f"Focus: {goal.get('current_focus', 'Non impostato')}")
                st.write(f"Obiettivo: {goal.get('daily_goal', 'Non impostato')}")
                st.write(f"Task suggerito: {goal.get('suggested_task', 'Non impostato')}")
                st.write(f"Prossima azione: {goal.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato obiettivi del giorno.")

    st.header("Gestione obiettivi")

    with st.container(border=True):
        goals_to_manage = load_json(DAILY_GOALS_PATH, [])

        if goals_to_manage:
            if st.button("Elimina ultimo obiettivo salvato"):
                removed_goal = goals_to_manage.pop()
                save_json(DAILY_GOALS_PATH, goals_to_manage)

                st.warning("Ultimo obiettivo eliminato.")
                st.write(f"Obiettivo eliminato: {removed_goal.get('activity_type', 'Tipo non impostato')}")
        else:
            st.info("Non ci sono obiettivi da eliminare.")

# Logica Note Tecniche 

elif page == "Note Tecniche":
    st.title("Note Tecniche")
    st.caption("Salva errori, soluzioni e concetti tecnici utili emersi durante lo sviluppo.")

    st.header("Nuova nota tecnica")

    with st.container(border=True):
        with st.form("technical_note_form"):
            category_input = st.selectbox(
                "Categoria",
                [
                    "Python",
                    "Streamlit",
                    "JSON",
                    "Git",
                    "GitHub",
                    "Errore",
                    "Debug",
                    "Architettura",
                    "AI Logic",
                    "Altro"
                ]
            )

            title_input = st.text_input(
                "Titolo nota",
                value=""
            )

            problem_input = st.text_area(
                "Problema o concetto",
                value=""
            )

            solution_input = st.text_area(
                "Soluzione o spiegazione",
                value=""
            )

            lesson_input = st.text_area(
                "Cosa ho imparato",
                value=""
            )

            next_action_input = st.text_input(
                "Prossima azione",
                value="Applicare questa nota nel progetto."
            )

            submitted_note = st.form_submit_button("Salva nota tecnica")

    if submitted_note:
        note_entry = {
            "category": category_input,
            "title": title_input,
            "problem": problem_input,
            "solution": solution_input,
            "lesson": lesson_input,
            "next_action": next_action_input
        }

        existing_notes = load_json(TECHNICAL_NOTES_PATH, [])
        existing_notes.append(note_entry)
        save_json(TECHNICAL_NOTES_PATH, existing_notes)

        st.success("Nota tecnica salvata correttamente.")

    saved_notes = load_json(TECHNICAL_NOTES_PATH, [])

    st.header("Ultima nota salvata")

    with st.container(border=True):
        if saved_notes:
            last_note = saved_notes[-1]
            st.write(f"Categoria: {last_note.get('category', 'Non impostata')}")
            st.write(f"Titolo: {last_note.get('title', 'Non impostato')}")
            st.write(f"Problema o concetto: {last_note.get('problem', 'Non impostato')}")
            st.write(f"Soluzione: {last_note.get('solution', 'Non impostata')}")
            st.write(f"Cosa ho imparato: {last_note.get('lesson', 'Non impostato')}")
            st.write(f"Prossima azione: {last_note.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato note tecniche.")

    st.header("Storico note tecniche")

    if saved_notes:
        for index, note in enumerate(reversed(saved_notes), start=1):
            with st.expander(f"Nota {index} - {note.get('title', 'Titolo non impostato')}"):
                st.write(f"Categoria: {note.get('category', 'Non impostata')}")
                st.write(f"Problema o concetto: {note.get('problem', 'Non impostato')}")
                st.write(f"Soluzione: {note.get('solution', 'Non impostata')}")
                st.write(f"Cosa ho imparato: {note.get('lesson', 'Non impostato')}")
                st.write(f"Prossima azione: {note.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato note tecniche.")

    st.header("Gestione note tecniche")

    with st.container(border=True):
        notes_to_manage = load_json(TECHNICAL_NOTES_PATH, [])

        if notes_to_manage:
            if st.button("Elimina ultima nota salvata"):
                removed_note = notes_to_manage.pop()
                save_json(TECHNICAL_NOTES_PATH, notes_to_manage)

                st.warning("Ultima nota eliminata.")
                st.write(f"Nota eliminata: {removed_note.get('title', 'Titolo non impostato')}")
        else:
            st.info("Non ci sono note da eliminare.")