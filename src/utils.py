# === Python Packages ===
from typing import Dict, Optional
import streamlit as st
import uuid 

# === Function to initialise state_session ===
def init_sess():
    """
    Initialises important keys for state sessions
    """
    ## === Required State Sessions ===
    sessions: Dict[str, Optional[str]] = {
        "session_id": None,
        "name": None,
        "age": None,
        "level": None
    }

    ## === Initialising using the for loop ===
    for key, value in sessions.items():
        if key not in st.session_state:
            st.session_state[key] = value

# === Function to create a unique session id ===
def get_sess_id():
    """
    Creates a unique session id for the user
    """
    session_id: str = str(uuid.uuid4())

    return session_id