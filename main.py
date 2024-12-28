from question_model import Question
from data import question_data

questions_bank = []  # Initialize the list to store the questions

questions_len = len(question_data)

for x in range(questions_len):
    questions_bank.append(
        Question(question_data[x]['text'], question_data[x]['answer']))

print(questions_bank)
