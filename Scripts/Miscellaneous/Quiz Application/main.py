from quiz import start_quiz
import random
import json

# QUESTIONS 
with open('./questions.json') as f:
    data = json.load(f)


questions = data["questions"]

# RANDOM QUESTIONS

random_questions = random.sample(questions, k=5)

# RUN QUIZ 
start_quiz(random_questions)
