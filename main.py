from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []  # Initialize the list to store the questions

questions_len = len(question_data)

for x in range(questions_len):
    # For Loop to retrieve the questions from data and append them into the questions_bank list.
    questions_bank.append(
        Question(question_data[x]['text'], question_data[x]['answer']))


quiz = QuizBrain(questions_bank)
quiz.next_question()
