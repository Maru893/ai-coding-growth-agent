
import os

from dotenv import load_dotenv
load_dotenv()

def get_weekly_plan_mock_response():
    return {
        "title": "Suggerimento AI simulato per il piano settimanale",
        "summary": "Concentrati su un task piccolo, misurabile e collegato al tuo progetto principale.",
        "suggestions": [
            "Scegli una sola skill da migliorare questa settimana.",
            "Costruisci una feature piccola ma funzionante.",
            "Aggiorna README o note tecniche dopo il lavoro.",
            "Salva un progresso a fine sessione."
        ]
    }


def get_daily_goal_mock_response():
    return {
        "title": "Suggerimento AI simulato per l'obiettivo del giorno",
        "summary": "Usa il tempo disponibile per completare un micro task.",
        "suggestions": [
            "Evita di iniziare troppe cose insieme.",
            "Scegli un task che puoi finire oggi.",
            "Scrivi una nota tecnica se incontri un errore."
        ]
    }


def get_skill_mock_response():
    return {
        "title": "Suggerimento AI simulato per la skill",
        "summary": "Rafforza la skill con pratica diretta nel progetto.",
        "suggestions": [
            "Fai un esercizio piccolo.",
            "Collega l'esercizio a una feature reale.",
            "Misura il livello di sicurezza dopo averlo completato."
        ]
    }


def get_default_mock_response():
    return {
        "title": "Suggerimento AI simulato",
        "summary": "Risposta mock generata correttamente.",
        "suggestions": [
            "Definisci un obiettivo chiaro.",
            "Lavora su un task piccolo.",
            "Salva il risultato."
        ]
    }

def detect_prompt_keywords(prompt):
    """
    Analizza il prompt e restituisce suggerimenti extra
    in base alle parole chiave trovate.
    """

    prompt_lower = prompt.lower()

    keyword_suggestions = []

    if "python" in prompt_lower:
        keyword_suggestions.append(
            "Dedica attenzione a funzioni, input, output e gestione errori in Python."
        )

    if "streamlit" in prompt_lower:
        keyword_suggestions.append(
            "Verifica che la UI sia chiara e che form, bottoni e sidebar funzionino correttamente."
        )

    if "json" in prompt_lower:
        keyword_suggestions.append(
            "Controlla che lettura, scrittura e struttura dei file JSON siano coerenti."
        )

    if "github" in prompt_lower:
        keyword_suggestions.append(
            "Aggiorna README e fai un commit chiaro dopo aver completato il task."
        )

    if "debug" in prompt_lower or "errore" in prompt_lower:
        keyword_suggestions.append(
            "Isola l’errore, leggi il traceback e salva la soluzione nelle Note Tecniche."
        )

    if "readme" in prompt_lower:
        keyword_suggestions.append(
            "Aggiorna la documentazione per spiegare cosa hai cambiato e perché."
        )

    if "api" in prompt_lower:
        keyword_suggestions.append(
            "Gestisci errori, chiavi ambiente e casi in cui la API non è configurata."
        )

    return keyword_suggestions


def generate_mock_ai_response(prompt, mode="weekly_plan"):
    """
    Simula una risposta AI senza usare API esterne.
    Usa alcune parole chiave del prompt per aggiungere suggerimenti più specifici.
    """

    mock_responses = {
        "weekly_plan": get_weekly_plan_mock_response,
        "daily_goal": get_daily_goal_mock_response,
        "skill": get_skill_mock_response
    }

    response_function = mock_responses.get(mode, get_default_mock_response)
    response = response_function()

    extra_suggestions = detect_prompt_keywords(prompt)

    if extra_suggestions:
        response["suggestions"] = response.get("suggestions", []) + extra_suggestions

    return response

def get_ai_environment_status():
    """
    Legge lo stato della configurazione AI dal file .env.
    Non effettua chiamate API.
    """

    provider = os.getenv("AI_PROVIDER", "openai")
    model = os.getenv("AI_MODEL", "gpt-4.1-mini")
    api_key = os.getenv("OPENAI_API_KEY", "")
    use_mock_ai = os.getenv("USE_MOCK_AI", "true").lower() == "true"

    return {
        "provider": provider,
        "model": model,
        "has_api_key": bool(api_key),
        "use_mock_ai": use_mock_ai
    }

def generate_ai_response(prompt, mode="weekly_plan", use_mock=True):
    """
    Punto unico di ingresso per generare risposte AI.

    Per ora usa solo il mock.
    In futuro potrà usare OpenAI API, Anthropic, modelli locali o altri provider.
    """

    if use_mock:
        return generate_mock_ai_response(prompt, mode)

    env_status = get_ai_environment_status()

    if not env_status["has_api_key"]:
        raise ValueError(
            "API key mancante. Aggiungi OPENAI_API_KEY nel file .env oppure riattiva mock AI."
        )

    raise NotImplementedError("La modalità API reale non è ancora implementata.")