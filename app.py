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


st.set_page_config(
    page_title="AI Coding Growth Agent",
    page_icon="🤖",
    layout="centered"
)

st.sidebar.title("Navigazione")

page = st.sidebar.radio(
    "Vai a",
    [
        "Dashboard",
        "Profilo",
        "Piano settimanale",
        "Checklist",
        "Focus settimana",
        "Progress Tracker",
        "Progetti",
        "Roadmap",
        "Skill Tracker"
    ]
)

if page == "Dashboard":
    st.title("Dashboard")

    profile = load_json(PROFILE_PATH, {})
    weekly_plans = load_json(WEEKLY_PLANS_PATH, [])
    progress_entries = load_json(PROGRESS_PATH, [])
    projects = load_json(PROJECTS_PATH, [])
    checklists = load_json(CHECKLISTS_PATH, [])
    skills = load_json(SKILLS_PATH, [])
    weekly_focus = load_json(WEEKLY_FOCUS_PATH, [])

    st.subheader("Riepilogo percorso")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric("Piani salvati", len(weekly_plans))

    with col2:
        st.metric("Progressi salvati", len(progress_entries))

    with col3:
        st.metric("Progetti salvati", len(projects))
    
    with col4:
        st.metric("Checklist salvate", len(checklists))

    with col5:
        st.metric("Skill salvate", len(skills))

    with col6:
        st.metric("Focus salvati", len(weekly_focus))    

    st.subheader("Profilo")

    st.write(f"Nome: {profile.get('name', 'Non impostato')}")
    st.write(f"Livello Python: {profile.get('python_level', 'Non impostato')}")
    st.write(f"Ore settimanali: {profile.get('weekly_hours', 'Non impostato')}")
    st.write(f"Focus principale: {profile.get('main_focus', 'Non impostato')}")

    st.subheader("Ultimo piano settimanale")

    if weekly_plans:
        last_plan = weekly_plans[-1]
        st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
        st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")
        st.write(f"Task tecnico: {last_plan.get('plan', {}).get('technical_task', 'Non impostato')}")
        st.write(f"Output GitHub: {last_plan.get('github_output', 'Non impostato')}")
    else:
        st.info("Non hai ancora generato piani settimanali.")

    st.subheader("Ultimo progetto")

    if projects:
        last_project = projects[-1]
        st.write(f"Nome: {last_project.get('name', 'Non impostato')}")
        st.write(f"Stato: {last_project.get('status', 'Non impostato')}")
        st.write(f"Prossima azione: {last_project.get('next_action', 'Non impostato')}")
    else:
        st.info("Non hai ancora salvato progetti.")

        
    st.subheader("Ultima skill salvata")

    if skills:
        last_skill = skills[-1]
        st.write(f"Skill: {last_skill.get('skill', 'Non impostata')}")
        st.write(f"Livello: {last_skill.get('level', 'Non impostato')} su 5")
        st.write(f"Sicurezza: {last_skill.get('confidence', 'Non impostata')} su 5")
        st.write(f"Prossima azione: {last_skill.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato skill.")

    
    st.subheader("Focus della settimana")

    if weekly_focus:
        last_focus = weekly_focus[-1]
        st.write(f"Skill focus: {last_focus.get('skill_focus', 'Non impostata')}")
        st.write(f"Progetto focus: {last_focus.get('project_focus', 'Non impostato')}")
        st.write(f"Obiettivo: {last_focus.get('weekly_goal', 'Non impostato')}")
        st.write(f"Priorità: {last_focus.get('priority', 'Non impostata')}")
    else:
        st.info("Non hai ancora impostato un focus settimanale.")

# logica Profilo


elif page == "Profilo":
    st.title("AI Coding Growth Agent")
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

    if st.button("Genera piano settimanale"):
        weekly_plan = generate_weekly_plan(
            weekly_hours_input,
            energy_input,
            focus_input,
            goal_input,
            current_project_input
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

    if st.button("Salva progresso"):
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

    if st.button("Salva progetto"):
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

        st.subheader("Progetto appena salvato")
        st.write(f"Nome: {project_entry['name']}")
        st.write(f"Problema che risolve: {project_entry['problem_solved']}")
        st.write(f"Skill principale: {project_entry['main_skill']}")
        st.write(f"Stato: {project_entry['status']}")
        st.write(f"Possibile uso monetizzabile: {project_entry['monetization']}")
        st.write(f"Prossima azione: {project_entry['next_action']}")

        st.subheader("Storico progetti")

    saved_projects = load_json(PROJECTS_PATH, [])

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

    st.subheader("Gestione progetti")

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

    if st.button("Salva skill"):
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

        st.subheader("Skill appena salvata")
        st.write(f"Skill: {skill_entry['skill']}")
        st.write(f"Livello: {skill_entry['level']} su 5")
        st.write(f"Sicurezza: {skill_entry['confidence']} su 5")
        st.write(f"Note: {skill_entry['notes']}")
        st.write(f"Prossima azione: {skill_entry['next_action']}")

    st.subheader("Storico skill")

    saved_skills = load_json(SKILLS_PATH, [])

    if saved_skills:
        for index, skill in enumerate(reversed(saved_skills), start=1):
            with st.expander(f"Skill {index} - {skill.get('skill', 'Skill non impostata')}"):
                st.write(f"Livello: {skill.get('level', 'Non impostato')} su 5")
                st.write(f"Sicurezza: {skill.get('confidence', 'Non impostata')} su 5")
                st.write(f"Note: {skill.get('notes', '')}")
                st.write(f"Prossima azione: {skill.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato skill.")

    st.subheader("Gestione skill")

    skills_to_manage = load_json(SKILLS_PATH, [])

    if skills_to_manage:
        if st.button("Elimina ultima skill salvata"):
            removed_skill = skills_to_manage.pop()
            save_json(SKILLS_PATH, skills_to_manage)

            st.warning("Ultima skill eliminata.")
            st.write(f"Skill eliminata: {removed_skill.get('skill', 'Skill non impostata')}")
    else:
        st.info("Non ci sono skill da eliminare.")


# Logica Focus Settimana

elif page == "Focus settimana":
    st.title("Focus settimana")

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

    if st.button("Salva focus settimanale"):
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

        st.subheader("Focus appena salvato")
        st.write(f"Skill focus: {focus_entry['skill_focus']}")
        st.write(f"Progetto focus: {focus_entry['project_focus']}")
        st.write(f"Obiettivo: {focus_entry['weekly_goal']}")
        st.write(f"Priorità: {focus_entry['priority']}")

    st.subheader("Storico focus settimanali")

    saved_focus = load_json(WEEKLY_FOCUS_PATH, [])

    if saved_focus:
        for index, focus in enumerate(reversed(saved_focus), start=1):
            with st.expander(f"Focus {index} - {focus.get('skill_focus', 'Skill non impostata')}"):
                st.write(f"Progetto: {focus.get('project_focus', 'Non impostato')}")
                st.write(f"Obiettivo: {focus.get('weekly_goal', 'Non impostato')}")
                st.write(f"Priorità: {focus.get('priority', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato focus settimanali.")

    st.subheader("Gestione focus")

    focus_to_manage = load_json(WEEKLY_FOCUS_PATH, [])

    if focus_to_manage:
        if st.button("Elimina ultimo focus salvato"):
            removed_focus = focus_to_manage.pop()
            save_json(WEEKLY_FOCUS_PATH, focus_to_manage)

            st.warning("Ultimo focus eliminato.")
            st.write(f"Focus eliminato: {removed_focus.get('skill_focus', 'Skill non impostata')}")
    else:
        st.info("Non ci sono focus da eliminare.")
