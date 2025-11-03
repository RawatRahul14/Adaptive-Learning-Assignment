# === Python Modules ===
import os
import json
import time
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

# === Class for the data tracker of the user ===
class PerformanceTracker:
    """
    Tracks performance and auto-updates a JSON file after every answer.
    """
    def __init__(
            self,
            session_id: str,
            name: str,
            age: int,
            level: str
    ):
        self.session_id = session_id
        self.name = name
        self.age = age
        self.level = level
        self.filepath = Path(f"data/{session_id}.json")
        os.makedirs(
            "data",
            exist_ok = True
        )

        ## === Initialising the file if new session ===
        if not os.path.exists(
            self.filepath
        ):
            """
            Create a new JSON file for this session and
            initialise it with session info, empty question list,
            and placeholder summary.
            """
            session_data: Dict[str, Any] = {
                "session_info": {
                    "session_id": self.session_id,
                    "name": self.name,
                    "age": self.age,
                    "initial_level": self.level,
                    "start_time": datetime.now().isoformat()
                },
                "questions": [],
                "user_answers": [],
                "actual_answers": [],
                "correct": [],
                "levels": [],
                "response_time": []
            }

            with open(
                self.filepath,
                "w"
            ) as f:
                """
                Write the initial session data structure to disk
                so future answers can be appended incrementally.
                """
                json.dump(
                    session_data,
                    f,
                    indent = 4
                )

    def start_time(
            self
    ):
        self.start = time.time()

    def record_result(
            self,
            question: str,
            user_answer: str,
            actual_answer: str,
            level: str
    ):
        """
        
        """
        end = time.time()
        time_taken = round(end - self.start, 2)
        is_correct = str(user_answer).strip() == str(actual_answer)

        ## === Updating the existing file ===
        with open(
            self.filepath,
            "r"
        ) as f:
            """
            Read the existing session file to load
            all previously saved question and answer data.
            """
            session_data = json.load(f)

        session_data["questions"].append(question)
        session_data["user_answers"].append(user_answer)
        session_data["actual_answers"].append(actual_answer)
        session_data["correct"].append(is_correct)
        session_data["levels"].append(level)
        session_data["response_time"].append(time_taken)

        ## === Replacing the file ===
        with open(
            self.filepath,
            "w"
        ) as f:
            """
            Overwrite the JSON file with the updated
            session data including the new response.
            """
            json.dump(
                session_data,
                f,
                indent = 4
            )