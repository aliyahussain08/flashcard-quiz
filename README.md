# Flashcard Quiz

A command-line flashcard quiz in Python that tests you on questions and tracks your score.

I built this to help me revise for my OCR A Level Business Studies, and to practise my Python skills outside of GCSE Computer Science.

## How it works

- Asks you 10 Business Studies questions one at a time
- Tells you straight away if you're right or wrong, and shows the correct answer
- Accepts answers in any capitalisation (e.g. "Maslow" and "maslow" both count)
- Gives you a final score at the end

## How to run it

1. Copy the code from `flashcard_quiz.py`
2. Paste it into an online Python compiler such as [Programiz](https://www.programiz.com/python-programming/online-compiler), or run it with Python on your computer:
   ```
   python flashcard_quiz.py
   ```
3. Type your answer to each question and press Enter

## What I used

- **Dictionaries** to store each question with its answer
- **For loops** to go through the questions one by one
- **If/else statements** to check answers
- **Input and string methods** (`.lower()`) to handle what the user types

## Ideas for next steps

- Shuffle the questions so they come in a different order each time
- Save high scores to a file
- Load questions from a separate file so new topics can be added easily
