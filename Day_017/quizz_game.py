from data import *

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



question_bank = []
for key in question_data:
    text = key["question"]
    answer = key["correct_answer"]
    #creating new object that takes the keys as arguments
    new_question = Question(text, answer)
    #appending the new object every time to the bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
