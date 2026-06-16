# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
Guess the secret number.

- [ ] Detail which bugs you found.
1. Hint logic reversed
2. New game button did not reset game
3. Input type error
4. Difficulty level not updating paramteres
5. Hardcoded displays
6. Score logic error
7. Attempts left off by one error
8. Enter key not implemented

- [ ] Explain what fixes you applied.
1. Reverse the guess comparison logic
2. Reset all paramteres when new game button is pressed
3. Cast input to int to compare
4. Generate secret number based on difficulty level range
5. Replace hardcoded with variables
6. Fix confusing score logic and show to user
7. Start attempts with the proper number
8. Use st.form to capture Enter key input

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects difficulty level "Hard" with 5 attempts allowed and the secret number should be between 1 to 50. The secret number it generated is 4.
2. User enters a guess of 25 and the game shows hint "go lower"
3. Score and attempts left updates correctly.
4. User enters a guess of 1 and the game shows hint 'go higher"
5. Score and attempts left updated correctly.
6. User enters a guess of 4 and the game shows "you won!" with a final score of 60.
7. User clicks on new game button and a new secret number is generated. It is 30.
8. Score resets to 0, attempts left resets properly, and history clears.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
