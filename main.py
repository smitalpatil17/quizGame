from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

while True:
    question_bank = []
    categories = ['Science: Computers', 'Science: Nature', 'Entertainment: Music', 'Entertainment: Film', 'Geography',
                  'History', 'Animals', 'General Knowledge']
    print("Welcome to QUIZ...\nFollowing are the categories for quiz.")
    i = 0
    for ctgr in categories:
        i += 1
        print(f"{i}. {ctgr}")
    choice = int(input("Select number of category: "))

    for que in question_data[choice-1]['questions_list']:
        question_bank.append(Question(que['question'], que['correct_answer']))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f'Your final score was: {quiz.score}/{quiz.question_number}')

    if input("Type yes if you want to play again. Or type no: ").lower()=='no':
        break
    else:
        os.system("cls")

