class QuizBrain:
    def __init__(self,que_list):
        self.question_number = 0
        self.question_list = que_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}:{question.text} (True/False)?')
        self.check_answer(user_ans, question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


