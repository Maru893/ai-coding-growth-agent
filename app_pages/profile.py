import streamlit as st

from utils.json_handler import load_json, save_json


def render_profile(profile_path):
    st.title("AI Coding Growth Agent")
    st.caption("Gestisci le informazioni di base del tuo percorso nel Coding AI.")

    profile = load_json(profile_path, {})

    st.header("Profilo personale")

    with st.container(border=True):
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

            save_json(profile_path, updated_profile)
            st.success("Profilo salvato correttamente.")

    st.header("Profilo attuale")

    with st.container(border=True):
        st.json(load_json(profile_path, {}))