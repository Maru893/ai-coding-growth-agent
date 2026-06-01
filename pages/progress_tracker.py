import streamlit as st

from utils.json_handler import load_json, save_json


def render_progress_tracker(progress_path):
    st.title("Progress Tracker")
    st.caption("Registra cosa hai completato, dove ti sei bloccato, cosa hai imparato e qual è la prossima azione.")

    st.header("Nuovo progresso")

    with st.container(border=True):
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

        existing_progress = load_json(progress_path, [])
        existing_progress.append(progress_entry)
        save_json(progress_path, existing_progress)

        st.success("Progresso salvato correttamente.")

    saved_progress = load_json(progress_path, [])

    st.header("Ultimo progresso salvato")

    with st.container(border=True):
        if saved_progress:
            last_progress = saved_progress[-1]
            st.write(f"Settimana: {last_progress.get('week', 'Settimana non impostata')}")
            st.write(f"Task completati: {last_progress.get('completed_tasks', 'Non impostato')}")
            st.write(f"Blocco: {last_progress.get('blocked', 'Nessun blocco indicato')}")
            st.write(f"Cosa ho imparato: {last_progress.get('learned', 'Non impostato')}")
            st.write(f"Prossima azione: {last_progress.get('next_action', 'Non impostata')}")
        else:
            st.info("Non hai ancora salvato progressi.")

    st.header("Storico progressi")

    if saved_progress:
        for index, progress in enumerate(reversed(saved_progress), start=1):
            with st.expander(f"Progresso {index} - {progress.get('week', 'Settimana non impostata')}"):
                st.write(f"Task completati: {progress.get('completed_tasks', 'Non impostato')}")
                st.write(f"Blocco: {progress.get('blocked', 'Nessun blocco indicato')}")
                st.write(f"Cosa ho imparato: {progress.get('learned', 'Non impostato')}")
                st.write(f"Prossima azione: {progress.get('next_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato progressi.")

    st.header("Gestione progressi")

    with st.container(border=True):
        progress_to_manage = load_json(progress_path, [])

        if progress_to_manage:
            if st.button("Elimina ultimo progresso salvato"):
                removed_progress = progress_to_manage.pop()
                save_json(progress_path, progress_to_manage)

                st.warning("Ultimo progresso eliminato.")
                st.write(f"Progresso eliminato: {removed_progress.get('week', 'Settimana non impostata')}")
        else:
            st.info("Non ci sono progressi da eliminare.")