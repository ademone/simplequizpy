from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answ = item["answer"]
    new_question = Question(question_text, question_answ)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# QuizBrain(question_bank)
# print(question_bank[0].answer)