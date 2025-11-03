# === Python Modules ===
from fastapi import FastAPI, HTTPException

# === Utils ===
from src.utils import get_sess_id

# === Custom Modules ===
from src.puzzle_generator import generate_question
from src.tracker import PerformanceTracker

# === Models ===
from src.request_models import (
    StartSession
)
from src.response_model import (
    StartSessionResponseModel
)

# === FastAPI APP ===
app = FastAPI(
    title = "Math Adventures API"
)

# === Global dictionary to hold active sessions ===
SESSIONS = {}

@app.post("/start", response_model = StartSessionResponseModel)
def start_session(
    data: StartSession
):
    """
    Initialize a new adaptive math session for the user.

    - Generates a unique session ID.
    - Creates a PerformanceTracker instance to log progress.
    - Stores the tracker in memory for ongoing interaction.
    - Returns the first math question and its correct answer.
    """
    session_id = get_sess_id()
    tracker = PerformanceTracker(
        session_id = session_id,
        name = data.name,
        age = data.age,
        level = data.level
    )
    SESSIONS[session_id] = tracker

    # === Generate 1st Question answer pair ===
    question, answer = generate_question(
        data.age,
        data.level
    )

    return StartSessionResponseModel(
        session_id = session_id,
        question = question,
        correct_answer = str(answer),
        message = f"Session started for {data.name} (level: {data.level})"
    )