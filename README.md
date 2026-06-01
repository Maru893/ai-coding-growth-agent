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
- Skill Tracker
- Focus settimana
- Contatore skill nella Dashboard
- Contatore focus nella Dashboard
- Visualizzazione ultima skill salvata nella Dashboard
- Visualizzazione focus settimanale nella Dashboard
- Planner migliorato con contesto da Skill Tracker
- Planner migliorato con contesto da Focus settimana
- Raccomandazione skill nel piano settimanale
- Focus settimanale collegato al piano
- Export Markdown aggiornato con raccomandazioni
- Obiettivo del giorno
- Storico obiettivi del giorno
- Eliminazione ultimo obiettivo salvato
- Visualizzazione ultimo obiettivo del giorno nella Dashboard
- Contatore obiettivi giornalieri nella Dashboard
- Note tecniche
- Storico note tecniche
- Eliminazione ultima nota tecnica
- Visualizzazione ultima nota tecnica nella Dashboard
- Contatore note tecniche nella Dashboard
- UI migliorata con CSS personalizzato
- Dashboard organizzata in card
- Metriche Dashboard su card personalizzate
- Form uniformati nelle sezioni principali
- Layout a card per Piano settimanale
- Layout a card per Progress Tracker
- Layout a card per Skill Tracker
- Layout a card per Focus settimana
- Layout a card per Obiettivo del giorno
- Layout a card per Progetti
- Layout a card per Note Tecniche
- Gestione sicura della modalità AI disattivata
- Warning UI quando API reale non è ancora implementata
- AI Settings collegato a Piano settimanale e Obiettivo del giorno


## AI mock mode

Il progetto include una prima struttura per l’integrazione AI tramite `utils/ai_client.py`.

Per ora non vengono usate API esterne. Il sistema usa una modalità mock per simulare suggerimenti AI nelle sezioni:

- Piano settimanale
- Obiettivo del giorno

Questa scelta permette di sviluppare e testare la logica dell’app senza costi, senza chiavi API e senza dipendere da servizi esterni.



## Configurazione futura API

Il file `.env.example` mostra le variabili previste per una futura integrazione:

```text
AI_PROVIDER=openai
AI_MODEL=gpt-4.1-mini
OPENAI_API_KEY=your_api_key_here
USE_MOCK_AI=true
```


## Struttura progetto

aiCoding-growth-agent/
├── app.py
├── pages/
│   ├── dashboard.py
│   ├── profile.py
│   ├── weekly_plan.py
│   ├── checklist.py
│   ├── daily_goal.py
│   ├── weekly_focus.py
│   ├── progress_tracker.py
│   ├── projects.py
│   ├── roadmap.py
│   ├── skill_tracker.py
│   └── technical_notes.py
├── utils/
│   ├── json_handler.py
│   ├── planner_rules.py
│   └── markdown_exporter.py
│   └── ai_clients.py
├── data/
├── exports/
├── README.md
├── requirements.txt
└── .gitignore


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

### V2 in sviluppo

- Skill Tracker
- Focus settimana
- Obiettivo del giorno
- Note tecniche
- Dashboard più operativa
- Contatori aggiornati
- Visualizzazione ultima skill
- Visualizzazione focus settimanale
- Visualizzazione ultimo obiettivo del giorno
- Visualizzazione ultima nota tecnica
- Planner contestuale basato su skill e focus
- Export Markdown migliorato
- UI migliorata con CSS personalizzato
- Layout a card nelle sezioni principali
- Form uniformati

### Prossimi step V2

- Miglioramento regole del planner
- Sezione “Obiettivo del giorno”
- Migliore gestione dello storico
- Possibilità di modificare record salvati
- Prima preparazione per API LLM

### V3

- Integrazione API LLM
- Generazione piani più personalizzati
- Analisi automatica dei progressi
- Suggerimenti automatici sui prossimi task
- Supporto alla monetizzazione dei mini progetti

## Stato progetto

- V1 completata
- V2 in sviluppo
- UI migliorata
- Refactor completato con pagine separate
- Pubblicato su GitHub personale