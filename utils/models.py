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