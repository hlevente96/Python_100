from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

brain = QuizBrain(question_bank)

while not brain.still_has_question():
    brain.next_question()
    print(f"Your final score: {brain.score}/{brain.q_number}")
