class QuizBrain:
    def __init__(self, question_list):
        """Initializing the QuizBrain Class"""
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        """Function to ask the questions"""
        user_choice = input(f"Q.{self.question_number +
                                 1}: {self.question_list[0].text} (True/False)?: ")
        self.question_number += 1

    def still_has_questions(self):
        """Function to check if the user gave the correct answer or not?"""
        if user_choice
