import streamlit as st

from utils.json_handler import load_json


def render_metric_card(title, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_dashboard(
    profile_path,
    weekly_plans_path,
    progress_path,
    projects_path,
    checklists_path,
    skills_path,
    weekly_focus_path,
    daily_goals_path,
    technical_notes_path
):
    st.title("Dashboard")
    st.caption("Controlla il riepilogo del tuo percorso, il focus attuale e le ultime attività salvate.")

    profile = load_json(profile_path, {})
    weekly_plans = load_json(weekly_plans_path, [])
    progress_entries = load_json(progress_path, [])
    projects = load_json(projects_path, [])
    checklists = load_json(checklists_path, [])
    skills = load_json(skills_path, [])
    weekly_focus = load_json(weekly_focus_path, [])
    daily_goals = load_json(daily_goals_path, [])
    technical_notes = load_json(technical_notes_path, [])

    st.header("Riepilogo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card("Piani", len(weekly_plans))

    with col2:
        render_metric_card("Progressi", len(progress_entries))

    with col3:
        render_metric_card("Progetti", len(projects))

    with col4:
        render_metric_card("Checklist", len(checklists))

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        render_metric_card("Skill", len(skills))

    with col6:
        render_metric_card("Focus", len(weekly_focus))

    with col7:
        render_metric_card("Obiettivi", len(daily_goals))

    with col8:
        render_metric_card("Note", len(technical_notes))

    st.header("Focus operativo")

    focus_col, goal_col = st.columns(2)

    with focus_col:
        with st.container(border=True):
            st.subheader("Focus della settimana")

            if weekly_focus:
                last_focus = weekly_focus[-1]
                st.write(f"Skill focus: {last_focus.get('skill_focus', 'Non impostata')}")
                st.write(f"Progetto focus: {last_focus.get('project_focus', 'Non impostato')}")
                st.write(f"Obiettivo: {last_focus.get('weekly_goal', 'Non impostato')}")
                st.write(f"Priorità: {last_focus.get('priority', 'Non impostata')}")
            else:
                st.info("Non hai ancora impostato un focus settimanale.")

    with goal_col:
        with st.container(border=True):
            st.subheader("Ultimo obiettivo del giorno")

            if daily_goals:
                last_daily_goal = daily_goals[-1]
                st.write(f"Tempo disponibile: {last_daily_goal.get('available_time', 'Non impostato')}")
                st.write(f"Energia: {last_daily_goal.get('energy', 'Non impostata')}")
                st.write(f"Tipo attività: {last_daily_goal.get('activity_type', 'Non impostato')}")
                st.write(f"Obiettivo: {last_daily_goal.get('daily_goal', 'Non impostato')}")
                st.write(f"Prossima azione: {last_daily_goal.get('next_action', 'Non impostata')}")
            else:
                st.info("Non hai ancora salvato obiettivi del giorno.")

    st.header("Ultime attività")

    plan_col, project_col = st.columns(2)

    with plan_col:
        with st.container(border=True):
            st.subheader("Ultimo piano settimanale")

            if weekly_plans:
                last_plan = weekly_plans[-1]
                st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
                st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")
                st.write(f"Task tecnico: {last_plan.get('plan', {}).get('technical_task', 'Non impostato')}")
                st.write(f"Output GitHub: {last_plan.get('github_output', 'Non impostato')}")
            else:
                st.info("Non hai ancora generato piani settimanali.")

    with project_col:
        with st.container(border=True):
            st.subheader("Ultimo progetto")

            if projects:
                last_project = projects[-1]
                st.write(f"Nome: {last_project.get('name', 'Non impostato')}")
                st.write(f"Stato: {last_project.get('status', 'Non impostato')}")
                st.write(f"Prossima azione: {last_project.get('next_action', 'Non impostato')}")
            else:
                st.info("Non hai ancora salvato progetti.")

    skill_col, note_col = st.columns(2)

    with skill_col:
        with st.container(border=True):
            st.subheader("Ultima skill salvata")

            if skills:
                last_skill = skills[-1]
                st.write(f"Skill: {last_skill.get('skill', 'Non impostata')}")
                st.write(f"Livello: {last_skill.get('level', 'Non impostato')} su 5")
                st.write(f"Sicurezza: {last_skill.get('confidence', 'Non impostata')} su 5")
                st.write(f"Prossima azione: {last_skill.get('next_action', 'Non impostata')}")
            else:
                st.info("Non hai ancora salvato skill.")

    with note_col:
        with st.container(border=True):
            st.subheader("Ultima nota tecnica")

            if technical_notes:
                last_note = technical_notes[-1]
                st.write(f"Categoria: {last_note.get('category', 'Non impostata')}")
                st.write(f"Titolo: {last_note.get('title', 'Non impostato')}")
                st.write(f"Cosa ho imparato: {last_note.get('lesson', 'Non impostato')}")
            else:
                st.info("Non hai ancora salvato note tecniche.")

    st.header("Percorso tecnico")

    with st.container(border=True):
        st.subheader("Profilo")

        st.write(f"Nome: {profile.get('name', 'Non impostato')}")
        st.write(f"Livello Python: {profile.get('python_level', 'Non impostato')}")
        st.write(f"Ore settimanali: {profile.get('weekly_hours', 'Non impostato')}")
        st.write(f"Focus principale: {profile.get('main_focus', 'Non impostato')}")