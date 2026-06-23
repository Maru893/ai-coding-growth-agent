from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    level: str = "Da consolidare"
    notes: str = ""
    next_action: str = ""

class DailyGoal(BaseModel):
    available_time: str
    energy: int
    activity_type: str
    current_focus: str
    daily_goal: str
    suggested_task: str
    next_action: str

class Project(BaseModel):
    name: str
    goal: str
    skill: str
    status: str
    monetization: str = ""
    next_action: str = ""


class LearningPlan(BaseModel):
    skill: str
    current_level: str
    available_time: str
    learning_goal: str
    difficulty: str
    study_block: str
    practice_block: str
    recap_block: str
    suggested_action: str
    checklist: list[str]