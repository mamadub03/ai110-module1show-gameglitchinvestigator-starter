# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Some of the bugs that I ran into were that I could input values under 0 and over 100. I did not expect to be able to add invalid values. The comparison does not work as it's saying lower for numbers that are higher and vice versa; I would expect the comparison to work properly. The code does not work when I click restart game. I expected the code to restart properly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

AI suggested the changes by making the switches in logic that I was unable to point out the problems. I was able to use AI to figure out how to switch and update the logic. One example where AI didn't work was with the test cases.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---


I described whether a bug was fixed by actually testing the change inside of the live environment. The AI helped me see where the issue was going wrong and helped me diagnose it.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The reason why it kept changing because anytime you clicked a button, streamlit ended up restarting the whole app again from the top. I would say the reruns are like when a whole entire paper gets erased whenever somebody speaks in a room or does an action. The way I changed it was by only generating a number once the very first round

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to reuse how I go about defining and fixing a bug. One thing I will do differently is go deeper in the AI solution and not just trusting it right away. This proejct showed how AI generated code is not perfect and can lead to issues which is why developers are very important.