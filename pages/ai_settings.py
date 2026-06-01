import streamlit as st

from utils.json_handler import load_json, save_json


def render_ai_settings(ai_settings_path):
    st.title("AI Settings")
    st.caption("Gestisci la modalità AI dell’app e prepara la futura integrazione con API reali.")

    settings = load_json(
        ai_settings_path,
        {
            "use_mock_ai": True,
            "ai_provider": "openai",
            "ai_model": "gpt-4.1-mini",
            "api_status": "not_configured"
        }
    )

    st.header("Configurazione AI")

    with st.container(border=True):
        with st.form("ai_settings_form"):
            use_mock_ai_input = st.checkbox(
                "Usa mock AI",
                value=settings.get("use_mock_ai", True)
            )

            ai_provider_input = st.selectbox(
                "Provider AI",
                ["openai", "anthropic", "local", "other"],
                index=["openai", "anthropic", "local", "other"].index(
                    settings.get("ai_provider", "openai")
                )
            )

            ai_model_input = st.text_input(
                "Modello AI",
                value=settings.get("ai_model", "gpt-4.1-mini")
            )

            api_status_input = st.selectbox(
                "Stato API",
                ["not_configured", "configured", "disabled"],
                index=["not_configured", "configured", "disabled"].index(
                    settings.get("api_status", "not_configured")
                )
            )

            submitted_settings = st.form_submit_button("Salva impostazioni AI")

    if submitted_settings:
        updated_settings = {
            "use_mock_ai": use_mock_ai_input,
            "ai_provider": ai_provider_input,
            "ai_model": ai_model_input,
            "api_status": api_status_input
        }

        save_json(ai_settings_path, updated_settings)
        st.success("Impostazioni AI salvate correttamente.")

    current_settings = load_json(ai_settings_path, {})

    st.header("Stato attuale")

    with st.container(border=True):
        st.write(f"Mock AI attivo: {current_settings.get('use_mock_ai', True)}")
        st.write(f"Provider AI: {current_settings.get('ai_provider', 'Non impostato')}")
        st.write(f"Modello AI: {current_settings.get('ai_model', 'Non impostato')}")
        st.write(f"Stato API: {current_settings.get('api_status', 'Non impostato')}")

    st.header("Come funziona")

    with st.container(border=True):
        st.write(
            "Per ora l’app usa la modalità mock AI. "
            "Questo significa che i suggerimenti vengono simulati senza chiamare API esterne."
        )

        st.write(
            "Quando aggiungerai una chiave API reale, questa pagina potrà controllare "
            "se usare mock mode o API mode."
        )

        st.write("Il file `.env` reale non deve essere caricato su GitHub.")