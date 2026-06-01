import streamlit as st

from utils.json_handler import load_json, save_json


def render_checklist(weekly_plans_path, checklists_path):
    st.title("Checklist")
    st.caption("Trasforma l’ultimo piano settimanale in task completabili e salva l’avanzamento.")

    weekly_plans = load_json(weekly_plans_path, [])
    saved_checklists = load_json(checklists_path, [])

    st.header("Checklist ultimo piano")

    with st.container(border=True):
        if not weekly_plans:
            st.info("Genera prima un piano settimanale.")
        else:
            last_plan = weekly_plans[-1]
            checklist_items = last_plan.get("checklist", [])

            st.write(f"Focus: {last_plan.get('focus', 'Non impostato')}")
            st.write(f"Obiettivo: {last_plan.get('goal', 'Non impostato')}")

            completed_items = []

            for index, item in enumerate(checklist_items):
                is_checked = st.checkbox(item, key=f"checklist_item_{index}")

                if is_checked:
                    completed_items.append(item)

            notes_input = st.text_area(
                "Note sulla checklist",
                value=""
            )

            if st.button("Salva checklist"):
                checklist_entry = {
                    "focus": last_plan.get("focus", "Non impostato"),
                    "goal": last_plan.get("goal", "Non impostato"),
                    "completed_items": completed_items,
                    "total_items": len(checklist_items),
                    "completion_count": len(completed_items),
                    "notes": notes_input
                }

                saved_checklists.append(checklist_entry)
                save_json(checklists_path, saved_checklists)

                st.success("Checklist salvata correttamente.")
                st.write(f"Task completati: {len(completed_items)} su {len(checklist_items)}")

    saved_checklists = load_json(checklists_path, [])

    st.header("Ultima checklist salvata")

    with st.container(border=True):
        if saved_checklists:
            last_checklist = saved_checklists[-1]
            st.write(f"Focus: {last_checklist.get('focus', 'Non impostato')}")
            st.write(f"Obiettivo: {last_checklist.get('goal', 'Non impostato')}")
            st.write(
                f"Completamento: {last_checklist.get('completion_count', 0)} "
                f"su {last_checklist.get('total_items', 0)}"
            )

            st.write("Task completati:")
            for item in last_checklist.get("completed_items", []):
                st.write(f"- {item}")

            st.write(f"Note: {last_checklist.get('notes', '')}")
        else:
            st.info("Non hai ancora salvato checklist.")

    st.header("Storico checklist")

    if saved_checklists:
        for index, checklist in enumerate(reversed(saved_checklists), start=1):
            with st.expander(f"Checklist {index} - {checklist.get('focus', 'Focus non impostato')}"):
                st.write(f"Obiettivo: {checklist.get('goal', 'Non impostato')}")
                st.write(
                    f"Completamento: {checklist.get('completion_count', 0)} "
                    f"su {checklist.get('total_items', 0)}"
                )

                st.write("Task completati:")
                for item in checklist.get("completed_items", []):
                    st.write(f"- {item}")

                st.write(f"Note: {checklist.get('notes', '')}")
    else:
        st.info("Non hai ancora salvato checklist.")

    st.header("Gestione checklist")

    with st.container(border=True):
        checklists_to_manage = load_json(checklists_path, [])

        if checklists_to_manage:
            if st.button("Elimina ultima checklist salvata"):
                removed_checklist = checklists_to_manage.pop()
                save_json(checklists_path, checklists_to_manage)

                st.warning("Ultima checklist eliminata.")
                st.write(f"Checklist eliminata: {removed_checklist.get('focus', 'Focus non impostato')}")
        else:
            st.info("Non ci sono checklist da eliminare.")