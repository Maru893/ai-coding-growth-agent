import streamlit as st

from utils.json_handler import load_json, save_json


def render_skill_tracker(skills_path):
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

        existing_skills = load_json(skills_path, [])
        existing_skills.append(skill_entry)
        save_json(skills_path, existing_skills)

        st.success("Skill salvata correttamente.")

    saved_skills = load_json(skills_path, [])

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
        skills_to_manage = load_json(skills_path, [])

        if skills_to_manage:
            if st.button("Elimina ultima skill salvata"):
                removed_skill = skills_to_manage.pop()
                save_json(skills_path, skills_to_manage)

                st.warning("Ultima skill eliminata.")
                st.write(f"Skill eliminata: {removed_skill.get('skill', 'Skill non impostata')}")
        else:
            st.info("Non ci sono skill da eliminare.")