from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    level: str = "Da consolidare"
    notes: str = ""
    next_action: str = ""