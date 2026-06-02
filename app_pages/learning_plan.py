import streamlit as st

from utils.json_handler import load_json, save_json
from utils.ai_client import generate_ai_response


def generate_learning_plan(skill, current_level, available_time, learning_goal):
    if available_time == "30 minuti":
        study_block = "10 minuti teoria"
        practice_block = "15 minuti pratica"
        recap_block = "5 minuti note"
    elif available_time == "60 minuti":
        study_block = "20 minuti teoria"
        practice_block = "30 minuti pratica"
        recap_block = "10 minuti note"
    elif available_time == "90 minuti":
        study_block = "30 minuti teoria"
        practice_block = "45 minuti pratica"
        recap_block = "15 minuti note"
    else:
        study_block = "45 minuti teoria"
        practice_block = "60 minuti pratica"
        recap_block = "15 minuti note e refactor"

    if current_level == "zero":
        difficulty = "base"
        suggested_action = f"Studia le fondamenta di {skill} e fai un esercizio guidato."
    elif current_level == "base":
        difficulty = "semplice"
        suggested_action = f"Applica {skill} a una piccola parte del tuo progetto."
    elif current_level == "intermedio":
        difficulty = "intermedio"
        suggested_action = f"Usa {skill} per migliorare struttura, qualità o automazione del progetto."
    else:
        difficulty = "avanzato"
        suggested_action = f"Crea una mini feature usando {skill} e documenta le decisioni tecniche."

    return {
        "skill": skill,
        "current_level": current_level,
        "available_time": available_time,
        "learning_goal": learning_goal,
        "difficulty": difficulty,
        "study_block": study_block,
        "practice_block": practice_block,
        "recap_block": recap_block,
        "suggested_action": suggested_action,
        "checklist": [
            "Capire il concetto principale",
            "Fare un esempio pratico",
            "Applicare il concetto al progetto",
            "Scrivere una nota tecnica",
            "Definire il prossimo passo"
        ]
    }


def render_learning_plan(learning_plans_path, ai_settings_path):
    st.title("Learning Plan")
    st.caption("Crea piccoli piani di apprendimento collegati alle skill che ti servono nel Coding AI.")

    st.header("Nuovo piano di apprendimento")

    with st.container(border=True):
        with st.form("learning_plan_form"):
            skill_input = st.selectbox(
                "Skill da studiare",
                [
                    "Python",
                    "Streamlit",
                    "JSON",
                    "Git",
                    "GitHub",
                    "FastAPI",
                    "API",
                    "Prompt Engineering",
                    "LLM API",
                    "RAG",
                    "Agentic AI",
                    "Testing",
                    "Deployment"
                ]
            )

            current_level_input = st.selectbox(
                "Livello attuale",
                ["zero", "base", "intermedio", "avanzato"]
            )

            available_time_input = st.selectbox(
                "Tempo disponibile",
                ["30 minuti", "60 minuti", "90 minuti", "2+ ore"]
            )

            learning_goal_input = st.text_input(
                "Obiettivo di apprendimento",
                value="Capire il concetto e applicarlo al progetto."
            )

            submitted_learning_plan = st.form_submit_button("Genera learning plan")

    if submitted_learning_plan:
        learning_plan = generate_learning_plan(
            skill_input,
            current_level_input,
            available_time_input,
            learning_goal_input
        )

        existing_plans = load_json(learning_plans_path, [])
        existing_plans.append(learning_plan)
        save_json(learning_plans_path, existing_plans)

        st.success("Learning plan generato e salvato.")

        ai_prompt = f"""
        Skill da studiare: {skill_input}
        Livello attuale: {current_level_input}
        Tempo disponibile: {available_time_input}
        Obiettivo di apprendimento: {learning_goal_input}
        """

        ai_settings = load_json(ai_settings_path, {"use_mock_ai": True})

        try:
            ai_suggestion = generate_ai_response(
                ai_prompt,
                mode="skill",
                use_mock=ai_settings.get("use_mock_ai", True)
            )

            st.header("Suggerimento AI simulato")

            with st.container(border=True):
                st.subheader(ai_suggestion.get("title", "Suggerimento AI"))
                st.write(ai_suggestion.get("summary", ""))

                st.write("Suggerimenti:")
                for suggestion in ai_suggestion.get("suggestions", []):
                    st.write(f"- {suggestion}")

        except (NotImplementedError, ValueError) as error:
            st.warning(str(error))
            st.info(
                "Puoi riattivare mock AI da AI Settings oppure configurare una API key valida nel file .env."
            )

    saved_learning_plans = load_json(learning_plans_path, [])

    st.header("Ultimo learning plan salvato")

    with st.container(border=True):
        if saved_learning_plans:
            last_plan = saved_learning_plans[-1]

            st.write(f"Skill: {last_plan.get('skill', 'Non impostata')}")
            st.write(f"Livello attuale: {last_plan.get('current_level', 'Non impostato')}")
            st.write(f"Tempo disponibile: {last_plan.get('available_time', 'Non impostato')}")
            st.write(f"Obiettivo: {last_plan.get('learning_goal', 'Non impostato')}")
            st.write(f"Difficoltà: {last_plan.get('difficulty', 'Non impostata')}")

            st.markdown("#### Piano")
            st.write(f"Studio: {last_plan.get('study_block', 'Non impostato')}")
            st.write(f"Pratica: {last_plan.get('practice_block', 'Non impostato')}")
            st.write(f"Recap: {last_plan.get('recap_block', 'Non impostato')}")

            st.markdown("#### Azione suggerita")
            st.write(last_plan.get("suggested_action", "Non impostata"))

            st.markdown("#### Checklist")
            for item in last_plan.get("checklist", []):
                st.write(f"- {item}")
        else:
            st.info("Non hai ancora salvato learning plan.")

    st.header("Storico learning plan")

    if saved_learning_plans:
        for index, plan in enumerate(reversed(saved_learning_plans), start=1):
            with st.expander(f"Learning plan {index} - {plan.get('skill', 'Skill non impostata')}"):
                st.write(f"Livello: {plan.get('current_level', 'Non impostato')}")
                st.write(f"Tempo disponibile: {plan.get('available_time', 'Non impostato')}")
                st.write(f"Obiettivo: {plan.get('learning_goal', 'Non impostato')}")
                st.write(f"Azione suggerita: {plan.get('suggested_action', 'Non impostata')}")
    else:
        st.info("Non hai ancora salvato learning plan.")

    st.header("Gestione learning plan")

    with st.container(border=True):
        plans_to_manage = load_json(learning_plans_path, [])

        if plans_to_manage:
            if st.button("Elimina ultimo learning plan salvato"):
                removed_plan = plans_to_manage.pop()
                save_json(learning_plans_path, plans_to_manage)

                st.warning("Ultimo learning plan eliminato.")
                st.write(f"Learning plan eliminato: {removed_plan.get('skill', 'Skill non impostata')}")
        else:
            st.info("Non ci sono learning plan da eliminare.")