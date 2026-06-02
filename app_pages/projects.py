import streamlit as st

from utils.json_handler import load_json, save_json


def render_projects(projects_path):
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

        existing_projects = load_json(projects_path, [])
        existing_projects.append(project_entry)
        save_json(projects_path, existing_projects)

        st.success("Progetto salvato correttamente.")

    saved_projects = load_json(projects_path, [])

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
        projects_to_manage = load_json(projects_path, [])

        if projects_to_manage:
            if st.button("Elimina ultimo progetto salvato"):
                removed_project = projects_to_manage.pop()
                save_json(projects_path, projects_to_manage)

                st.warning("Ultimo progetto eliminato.")
                st.write(f"Progetto eliminato: {removed_project.get('name', 'Nome non impostato')}")
        else:
            st.info("Non ci sono progetti da eliminare.")