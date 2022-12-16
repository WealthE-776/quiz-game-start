class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
    # WE SET THE USER ANSWER AS AN INPUT RATHER THAN A PRINT STATEMENT SO WE WILL BE ABLE
    # TO COLLECT DATA FROM THE USER IN THE FORM OF INPUT . AS SHOWN BELOW
        user_answer = input(f"Q.{self.question_number},{current_question.question}.(True/False) ")
        self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current is {self.score}/{self.question_number}")
        print("\n")
