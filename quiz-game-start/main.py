from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for que in question_data:
    my_question = Question(que["text"],que["answer"])
    Question_bank.append(my_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()
    if not quiz.still_has_question():
        print(f"you've completed the quiz.\nyour final score is : {quiz.score}/{quiz.question_number}")


