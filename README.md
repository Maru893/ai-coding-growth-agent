# AI Coding Growth Agent

AI Coding Growth Agent è una mini app personale costruita con Python e Streamlit.

L'obiettivo è aiutarmi a pianificare il mio percorso nel Coding AI, partendo dal mio livello attuale, dal tempo disponibile ogni settimana e dai progressi reali.

## Stack

- Python
- Streamlit
- JSON

## Funzionalità attuali

- Dashboard riepilogativa
- Profilo personale modificabile
- Salvataggio dati in JSON
- Generatore piano settimanale
- Piano settimanale leggibile
- Progress tracker
- Storico progressi leggibile
- Sezione progetti
- Storico progetti leggibile
- Roadmap 3 mesi
- Navigazione tramite sidebar
- Codice organizzato in moduli
- Export del piano settimanale in Markdown
- Sezione checklist
- Storico checklist leggibile
- Eliminazione ultimo piano salvato
- Eliminazione ultima checklist salvata
- Eliminazione ultimo progresso salvato
- Eliminazione ultimo progetto salvato

## Struttura progetto

aiCoding-growth-agent/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── profile.json
│   ├── weekly_plans.json
│   ├── checklists.json
│   ├── progress.json
│   ├── projects.json
│   └── roadmap.json
├── exports/
├── utils/
│   ├── json_handler.py
│   ├── planner_rules.py
│   └── markdown_exporter.py
└── venv/


## Roadmap

### V1 completata

- Dashboard
- Profilo personale
- Piano settimanale
- Checklist
- Progress tracker
- Progetti
- Roadmap 3 mesi
- Export Markdown
- Salvataggio JSON
- Sidebar di navigazione
- Storici leggibili
- Eliminazione ultimo record salvato

### V2

- Miglioramento regole del planner
- Sezione “Focus della settimana”
- Sezione “Skill tracker”
- Migliore gestione dello storico
- Possibilità di modificare record salvati
- Prima preparazione per API LLM

### V3

- Integrazione API LLM
- Generazione piani più personalizzati
- Analisi automatica dei progressi
- Suggerimenti automatici sui prossimi task
- Supporto alla monetizzazione dei mini progetti