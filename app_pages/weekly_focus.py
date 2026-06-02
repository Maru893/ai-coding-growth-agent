import streamlit as st

from utils.json_handler import load_json, save_json


def render_weekly_focus(weekly_focus_path):
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

        existing_focus = load_json(weekly_focus_path, [])
        existing_focus.append(focus_entry)
        save_json(weekly_focus_path, existing_focus)

        st.success("Focus settimanale salvato correttamente.")

    saved_focus = load_json(weekly_focus_path, [])

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
        focus_to_manage = load_json(weekly_focus_path, [])

        if focus_to_manage:
            if st.button("Elimina ultimo focus salvato"):
                removed_focus = focus_to_manage.pop()
                save_json(weekly_focus_path, focus_to_manage)

                st.warning("Ultimo focus eliminato.")
                st.write(f"Focus eliminato: {removed_focus.get('skill_focus', 'Skill non impostata')}")
        else:
            st.info("Non ci sono focus da eliminare.")