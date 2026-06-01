import streamlit as st

from utils.json_handler import load_json


def render_roadmap(roadmap_path):
    st.title("Roadmap")
    st.caption("Visualizza la direzione dei prossimi mesi, con focus, obiettivi, skill da allenare e progetti principali.")

    roadmap = load_json(roadmap_path, [])

    if roadmap:
        for item in roadmap:
            with st.expander(
                f"{item.get('month', 'Mese non impostato')} - {item.get('focus', 'Focus non impostato')}"
            ):
                st.write(f"Obiettivo: {item.get('goal', 'Non impostato')}")
                st.write(f"Progetto principale: {item.get('project', 'Non impostato')}")

                st.write("Skill da allenare:")
                for skill in item.get("skills", []):
                    st.write(f"- {skill}")
    else:
        st.info("Roadmap non ancora configurata.")