# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The game is straight forward to play the first time, but the logic is wrong in many areas. 
1. The hint logic is backwards.
2. The new game button does not clear history and what is printed on screen after winning.
3. Final score does not match the score in the developer debug info, nor does it update correctly.
4. Attempts left is always one less than the attempts allowed.
5. Guesses do not accurately get added to history.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess: 50 |"Go Lower" hint | "Go Higher" hint | none |
| Guess: 50, 75, 100, 25, 1 | History: [50, 75, 100, 25, 1] | History: [50, 75, 25] | none |
| New game button | clears the history and score | Does not clear history and score | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude plugin inside VS Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Some of the guess range displays are hardcoded and the AI was able to point that out for me so that whn I change difficulty level, the display with reflect that. Since this was a display bug, it was easy to verify just by refreshing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I askd the AI to fix the Enter key bug, it suggested using st.form which I wasn't familiar with. I continued with the fix to see what it will do and it actually changed the placement of the new game button and show hint button. Which was not what I wanted it to do. So I gave it further instructions to go back and make the changes without changing the button placements. The key was to check after each change it made, especially for something I wasn't familiar working with.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I manually tested it myself. Later followed by a pytest.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I noticed that with some fixes I tell AI to make, it did not account for multiple occurances in the code. For example, the hardcoded display of range numbers. The AI only changeed the first occurance of it which was the sidebar text. When I manually tested it, I notice the range display at the top of the page did not update. This helped me learn that when giving AI prompts, I need to give clearer instructions to account for the entire scope.  

- Did AI help you design or understand any tests? How?
AI helped me design and understand the tests. I copy and pasted the errors from the failed tests and had AI explain them to me. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns read top to bottom every time a user interacts with the page. The session state allows values to be saved for the next rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
After learning how AI can create pytests for me, it would be useful to make them as I fix each bug in the future.

- What is one thing you would do differently next time you work with AI on a coding task?
I will give clearer prompts with more guidelines. There were times where my prompts were vague and the AI thought forever that I had to stop it.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think it is very powerful to be able to unerstand the full scope of the code and provide changes directly. However, it is not always perfect so I need to provide more guidance. 
