import streamlit as st

from utils.json_handler import load_json, save_json
from utils.ai_client import generate_ai_response


def render_daily_goal(daily_goals_path):
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

        existing_daily_goals = load_json(daily_goals_path, [])
        existing_daily_goals.append(daily_goal_entry)
        save_json(daily_goals_path, existing_daily_goals)

        st.success("Obiettivo del giorno generato e salvato.")
        
        ai_prompt = f"""
            Tempo disponibile oggi: {available_time_input}
            Energia: {energy_input}
            Tipo attività: {activity_type_input}
            Focus attuale: {current_focus_input}
            Obiettivo generato: {daily_goal}
            Task suggerito: {suggested_task}
            Prossima azione: {next_action}
            """

        ai_suggestion = generate_ai_response(
            ai_prompt,
            mode="daily_goal",
            use_mock=True
                )

        st.header("Suggerimento AI simulato")

        with st.container(border=True):
            st.subheader(ai_suggestion.get("title", "Suggerimento AI"))
            st.write(ai_suggestion.get("summary", ""))

            st.write("Suggerimenti:")
            for suggestion in ai_suggestion.get("suggestions", []):
                st.write(f"- {suggestion}")

    saved_daily_goals = load_json(daily_goals_path, [])

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
        goals_to_manage = load_json(daily_goals_path, [])

        if goals_to_manage:
            if st.button("Elimina ultimo obiettivo salvato"):
                removed_goal = goals_to_manage.pop()
                save_json(daily_goals_path, goals_to_manage)

                st.warning("Ultimo obiettivo eliminato.")
                st.write(f"Obiettivo eliminato: {removed_goal.get('activity_type', 'Tipo non impostato')}")
        else:
            st.info("Non ci sono obiettivi da eliminare.")