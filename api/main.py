from pathlib import Path

from fastapi import FastAPI

from utils.json_handler import load_json
from utils.rag.pdf_reader import load_all_pdf_pages
from utils.rag.simple_search import search_pages

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"
SKILLS_PATH = DATA_DIR / "skills.json"
PROJECTS_PATH = DATA_DIR / "projects.json"
DAILY_GOALS_PATH = DATA_DIR / "daily_goals.json"
LEARNING_PLANS_PATH = DATA_DIR / "learning_plans.json"



app = FastAPI(
    title="AI Coding Growth Agent API",
    version="1.1.0",
    description="Mini backend FastAPI per leggere i dati JSON del progetto."
)


@app.get("/")
def root():
    return {
        "message": "AI Coding Growth Agent API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/skills")
def get_skills():
    return load_json(SKILLS_PATH, [])


@app.get("/projects")
def get_projects():
    return load_json(PROJECTS_PATH, [])


@app.get("/daily-goals")
def get_daily_goals():
    return load_json(DAILY_GOALS_PATH, [])


@app.get("/learning-plans")
def get_learning_plans():
    return load_json(LEARNING_PLANS_PATH, [])

@app.get("/knowledge/search")
def search_knowledge(query: str):
    pages = load_all_pdf_pages(KNOWLEDGE_BASE_DIR)
    results = search_pages(pages, query)

    return {
        "query": query,
        "results": results
    }