import streamlit as st

from utils.json_handler import load_json, save_json
from utils.planner_rules import generate_weekly_plan
from utils.markdown_exporter import export_weekly_plan_to_markdown


def render_weekly_plan(
    weekly_plans_path,
    skills_path,
    weekly_focus_path
):
    st.title("Piano settimanale")
    st.caption("Genera un piano pratico basato su tempo, energia, focus, skill e obiettivo della settimana.")

    st.header("Nuovo piano")

    with st.container(border=True):
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
        skills = load_json(skills_path, [])
        weekly_focus = load_json(weekly_focus_path, [])

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

        existing_plans = load_json(weekly_plans_path, [])
        existing_plans.append(weekly_plan)
        save_json(weekly_plans_path, existing_plans)

        st.success("Piano settimanale generato e salvato.")

    saved_plans = load_json(weekly_plans_path, [])

    st.header("Ultimo piano salvato")

    with st.container(border=True):
        if saved_plans:
            last_plan = saved_plans[-1]

            st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
            st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")
            st.write(f"Progetto attuale: {last_plan.get('current_project', 'Non impostato')}")

            st.markdown("#### Distribuzione tempo")
            st.write(f"Studio: {last_plan.get('plan', {}).get('study', 'Non impostato')}")
            st.write(f"Pratica: {last_plan.get('plan', {}).get('practice', 'Non impostato')}")
            st.write(f"Documentazione: {last_plan.get('plan', {}).get('documentation', 'Non impostato')}")

            st.markdown("#### Task tecnico")
            st.write(last_plan.get("plan", {}).get("technical_task", "Non impostato"))

            st.markdown("#### Checklist")
            for item in last_plan.get("checklist", []):
                st.write(f"- {item}")

            st.markdown("#### Output GitHub")
            st.write(last_plan.get("github_output", "Non impostato"))

            st.markdown("#### Possibile uso monetizzabile")
            st.write(last_plan.get("money_path", "Non impostato"))

            st.markdown("#### Raccomandazione skill")
            st.write(last_plan.get("skill_recommendation", "Non impostata"))

            st.markdown("#### Focus settimanale collegato")
            st.write(last_plan.get("weekly_focus_recommendation", "Non impostato"))
        else:
            st.info("Non hai ancora generato piani settimanali.")

    st.header("Storico piani settimanali")

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

    st.header("Gestione piani")

    with st.container(border=True):
        plans_to_manage = load_json(weekly_plans_path, [])

        if plans_to_manage:
            if st.button("Elimina ultimo piano salvato"):
                removed_plan = plans_to_manage.pop()
                save_json(weekly_plans_path, plans_to_manage)

                st.warning("Ultimo piano eliminato.")
                st.write(f"Piano eliminato: {removed_plan.get('focus', 'Focus non impostato')}")
        else:
            st.info("Non ci sono piani da eliminare.")

    st.header("Export")

    with st.container(border=True):
        saved_plans_for_export = load_json(weekly_plans_path, [])

        if saved_plans_for_export:
            if st.button("Esporta ultimo piano in Markdown"):
                last_plan = saved_plans_for_export[-1]
                exported_file = export_weekly_plan_to_markdown(last_plan)
                st.success(f"Piano esportato in: {exported_file}")
        else:
            st.info("Genera almeno un piano prima di esportare.")