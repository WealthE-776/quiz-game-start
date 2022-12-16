from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank)
# To get the question and answer directly used in the dictionary use this syntax
#     question_bank.append(question['text'])
#     question_bank.append(question['answer']),"\n"
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("You have completed the quiz")
    print(f"You final score : {quiz.score}/{quiz.question_number}")
