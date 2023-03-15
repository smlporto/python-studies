class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(guess, current_question.answer)

    def check_answer(self, user_guess, correct_answer):
        if user_guess.lower() == correct_answer.lower():
            print("Congrats! You got it right.")
            self.score += 1
        else:
            print("Oh oh! That's incorrect.")
        print(f"Current score: {self.score}/{self.question_number}")
