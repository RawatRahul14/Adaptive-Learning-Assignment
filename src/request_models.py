# === Python Module ===
from pydantic import BaseModel

# === Models ===
class StartSession(BaseModel):
    name: str
    age: int
    level: str