# === Python Packages ===
import streamlit as st

# === Utils ===
from src.utils import init_sess, get_sess_id

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
                st.success("Proceeding to the Quiz.")

            else:
                st.error("Please enter all the values")

if __name__ == "__main__":
    main()