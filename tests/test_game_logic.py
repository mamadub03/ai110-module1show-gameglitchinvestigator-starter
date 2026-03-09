from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting bugs fixed in app.py ---
# Stub out streamlit so app.py can be imported without a running UI.
import sys
from unittest.mock import MagicMock
sys.modules.setdefault("streamlit", MagicMock())
from app import check_guess as app_check_guess

def test_check_guess_direction_bug_too_high():
    # Bug fix: guess > secret was incorrectly returning "Too Low" / "Go HIGHER!"
    # It must now return "Too High" with a "LOWER" hint.
    outcome, message = app_check_guess(60, 50)
    assert outcome == "Too High", f"Expected 'Too High' but got '{outcome}'"
    assert "LOWER" in message

def test_check_guess_direction_bug_too_low():
    # Counterpart: guess < secret must return "Too Low" with a "HIGHER" hint.
    outcome, message = app_check_guess(40, 50)
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}'"
    assert "HIGHER" in message
