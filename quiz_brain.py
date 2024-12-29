class QuizBrain:
    def __init__(self, question_list):
        """Initializing the QuizBrain Class"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Function to check if the user gave the correct answer or not?"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Function to ask the questions"""
        current_question = self.question_list[self.question_number]
        user_choice = input(f"Q.{self.question_number +
                                 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_choice, correct_answer):
        """Function to check the user's given answers"""
        if user_choice.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("that's wrong.")
        print(f"The Correct answer was: {correct_answer}")
        print(f"Your current score is: {
              self.score}/{self.question_number}")
        print("\n \n")
