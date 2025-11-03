# === Python Packages ===
import streamlit as st
import requests

# === Utils ===
from src.utils import init_sess, get_sess_id

# === Backend URL ===
API_URL = "http://127.0.0.1:8000"

# === Main UI function ===
def main() -> None:
    """
    Streamlit based UI
    """
    ## === Initialising the sessions ===
    init_sess()

    if st.session_state["session_id"] is None:
        st.session_state["session_id"] = get_sess_id

    st.header("🧮 Math Adventures: AI-Powered Adaptive Learning")
    st.subheader("Practice fun math problems that adapt to your skill level!")

    with st.sidebar:
        ## === Getting the name ===
        st.session_state["name"] = st.text_input("👤 Your name")

        ## === Getting the age between 5 to 10 years ===
        st.session_state["age"] = st.number_input(
            "🎂 Age",
            min_value = 5,
            max_value = 10,
            step = 1
        )

        ## === Getting the initial level for the quuiz ===
        st.session_state["level"] = st.selectbox(
            "📊 Starting Level",
            ["Easy", "Medium", "Hard"]
        )

        if st.button(
            label = "Start Quiz",
            key = "starting_quiz"
        ):
            if (
                bool(st.session_state["name"]) and
                bool(st.session_state["age"]) and
                bool(st.session_state["level"])
            ):
                ## === Data to pass from frontend to backend ===
                payload = {
                    "name": st.session_state["name"],
                    "age": st.session_state["age"],
                    "level": st.session_state["level"],
                }

                ## === Connecting to the backend ===
                try:
                    response = requests.post(
                        f"{API_URL}/start",
                        json = payload
                    )

                    if response.status_code == 200:
                        data = response.json()

                        # === Save returned values in session_state ===
                        st.session_state["session_id"] = data["session_id"]
                        st.session_state["current_question"] = data["question"]
                        st.session_state["correct_answer"] = data["correct_answer"]

                        st.info(f"**Question:** {data['question']}")
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")

                except requests.exceptions.ConnectionError as e:
                    st.error("⚠️ Unable to connect to the backend. Please ensure FastAPI is running.")

                st.success("Proceeding to the Quiz.")

            else:
                st.error("Please enter all the values")

if __name__ == "__main__":
    main()