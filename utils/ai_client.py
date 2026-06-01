def generate_mock_ai_response(prompt, mode="weekly_plan"):
    """
    Simula una risposta AI senza usare API esterne.
    Serve per preparare la struttura futura dell'integrazione LLM.
    """

    if mode == "weekly_plan":
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

    if mode == "daily_goal":
        return {
            "title": "Suggerimento AI simulato per l'obiettivo del giorno",
            "summary": "Usa il tempo disponibile per completare un micro task.",
            "suggestions": [
                "Evita di iniziare troppe cose insieme.",
                "Scegli un task che puoi finire oggi.",
                "Scrivi una nota tecnica se incontri un errore."
            ]
        }

    if mode == "skill":
        return {
            "title": "Suggerimento AI simulato per la skill",
            "summary": "Rafforza la skill con pratica diretta nel progetto.",
            "suggestions": [
                "Fai un esercizio piccolo.",
                "Collega l'esercizio a una feature reale.",
                "Misura il livello di sicurezza dopo averlo completato."
            ]
        }

    return {
        "title": "Suggerimento AI simulato",
        "summary": "Risposta mock generata correttamente.",
        "suggestions": [
            "Definisci un obiettivo chiaro.",
            "Lavora su un task piccolo.",
            "Salva il risultato."
        ]
    }


def generate_ai_response(prompt, mode="weekly_plan", use_mock=True):
    """
    Punto unico di ingresso per generare risposte AI.

    Per ora usa solo il mock.
    In futuro potrà usare OpenAI API, Anthropic, modelli locali o altri provider.
    """

    if use_mock:
        return generate_mock_ai_response(prompt, mode)

    raise NotImplementedError("La modalità API reale non è ancora implementata.")