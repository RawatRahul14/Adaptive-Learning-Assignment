# === Python Modules ===
from pydantic import BaseModel

# === Repsonse Models ===
class StartSessionResponseModel(BaseModel):
    session_id: str
    question: str
    correct_answer: str
    message: str