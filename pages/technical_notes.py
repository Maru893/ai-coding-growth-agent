import streamlit as st

from utils.json_handler import load_json, save_json


def render_technical_notes(technical_notes_path):
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

        existing_notes = load_json(technical_notes_path, [])
        existing_notes.append(note_entry)
        save_json(technical_notes_path, existing_notes)

        st.success("Nota tecnica salvata correttamente.")

    saved_notes = load_json(technical_notes_path, [])

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
        notes_to_manage = load_json(technical_notes_path, [])

        if notes_to_manage:
            if st.button("Elimina ultima nota salvata"):
                removed_note = notes_to_manage.pop()
                save_json(technical_notes_path, notes_to_manage)

                st.warning("Ultima nota eliminata.")
                st.write(f"Nota eliminata: {removed_note.get('title', 'Titolo non impostato')}")
        else:
            st.info("Non ci sono note da eliminare.")