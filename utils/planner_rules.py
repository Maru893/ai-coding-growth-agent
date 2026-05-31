def generate_weekly_plan(hours, energy, focus, goal, current_project):
    if hours == "1-2":
        study_time = "30 minuti"
        practice_time = "1 ora"
        documentation_time = "30 minuti"
        difficulty = "molto semplice"
    elif hours == "3-5":
        study_time = "1 ora"
        practice_time = "2-3 ore"
        documentation_time = "1 ora"
        difficulty = "semplice"
    elif hours == "6-8":
        study_time = "2 ore"
        practice_time = "4-5 ore"
        documentation_time = "1 ora"
        difficulty = "intermedio"
    else:
        study_time = "2-3 ore"
        practice_time = "6+ ore"
        documentation_time = "1-2 ore"
        difficulty = "più avanzato"

    if energy <= 2:
        task_type = "revisione, documentazione o piccolo miglioramento"
    elif energy == 3:
        task_type = "task tecnico mirato"
    else:
        task_type = "nuova feature o mini modulo"

    focus_tasks = {
        "Python": "crea o migliora una funzione Python con input, output e gestione errori",
        "Streamlit": "aggiungi una sezione all’interfaccia e collega i dati al file JSON",
        "JSON": "leggi, aggiorna e salva dati in modo ordinato",
        "AI Logic": "simula il comportamento di un agente usando regole e template",
        "GitHub": "migliora README, struttura del progetto e storico dei progressi"
    }

    technical_task = focus_tasks.get(
        focus,
        "scegli un task piccolo e completabile collegato al progetto"
    )

    plan = {
        "hours": hours,
        "energy": energy,
        "focus": focus,
        "goal": goal,
        "current_project": current_project,
        "plan": {
            "study": study_time,
            "practice": practice_time,
            "documentation": documentation_time,
            "difficulty": difficulty,
            "task_type": task_type,
            "technical_task": technical_task
        },
        "checklist": [
            "Capire il concetto principale della settimana",
            "Completare un task tecnico piccolo",
            "Salvare il codice funzionante",
            "Aggiornare il README o aggiungere una nota",
            "Scrivere cosa hai imparato"
        ],
        "github_output": f"Aggiorna il repository con un miglioramento legato a {focus}.",
        "money_path": f"Questo lavoro può diventare una base per offrire una mini automazione o dashboard collegata a {focus}."
    }

    return plan