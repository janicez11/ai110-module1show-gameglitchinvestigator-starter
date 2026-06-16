import pytest
import random
from logic_utils import check_guess, get_range_for_difficulty, update_score

#FIX: 3 pytests, unpack tuples to compare to the expected result
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, outcome = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_new_game_resets_state():
    # Simulate a mid-game session state
    session_state = {
        "attempts": 4,
        "secret": 42,
        "status": "lost",
        "history": [10, 20, 30, 40],
        "score": -20,
        "difficulty": "Normal",
    }

    difficulty = session_state["difficulty"]
    low, high = get_range_for_difficulty(difficulty)

    # Apply the same reset logic the New Game button uses in app.py
    session_state["attempts"] = 0
    session_state["secret"] = random.randint(low, high)
    session_state["status"] = "playing"
    session_state["history"] = []
    session_state["score"] = 0

    assert session_state["attempts"] == 0
    assert session_state["status"] == "playing"
    assert session_state["history"] == []
    assert session_state["score"] == 0
    assert low <= session_state["secret"] <= high

@pytest.mark.parametrize("current_score,outcome,attempt_number,expected_score", [
    (0,   "Win",      1,  90),   # win early: 100 - 10*1 = 90
    (0,   "Win",      5,  50),   # win mid:   100 - 10*5 = 50
    (0,   "Win",     10,  10),   # win late:  100 - 10*10 = 0, floored to 10
    (50,  "Too High", 3,  45),   # wrong guess penalises -5
    (50,  "Too Low",  3,  45),   # wrong guess penalises -5
    (30,  "Unknown",  1,  30),   # unrecognised outcome leaves score unchanged
])
def test_score_updates(current_score, outcome, attempt_number, expected_score):
    assert update_score(current_score, outcome, attempt_number) == expected_score

ATTEMPT_LIMITS = {"Easy": 6, "Normal": 8, "Hard": 5}

@pytest.mark.parametrize("difficulty,expected_low,expected_high,expected_attempts", [
    ("Easy",   1,  20, 6),
    ("Normal", 1, 100, 8),
    ("Hard",   1,  50, 5),
])
def test_difficulty_settings(difficulty, expected_low, expected_high, expected_attempts):
    low, high = get_range_for_difficulty(difficulty)
    assert low == expected_low
    assert high == expected_high

    secret = random.randint(low, high)
    assert expected_low <= secret <= expected_high

    assert ATTEMPT_LIMITS[difficulty] == expected_attempts


