from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
QUIZ_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_board = Label(text=f"Score:{0}", background=THEME_COLOR)
        self.score_board.grid(column=1, row=0)

        self.questions_space = Canvas(width=300,height=250, background="white", highlightthickness=0)
        self.question_text = self.questions_space.create_text(150, 125, width=280, text="question goes here", font=QUIZ_FONT, fill=THEME_COLOR)
        self.questions_space.grid(column=0,row=1, columnspan=2, pady=40)

    #buttons
        self.true_img = PhotoImage(file="Day_034/images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file="Day_034/images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.questions_space.config(background="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.questions_space.itemconfig(self.question_text, text=q_text)
        else:
            self.questions_space.itemconfig(self.question_text, text=f"Quiz is over\n Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    

    def give_feedback(self, is_right):
        if is_right:
            self.questions_space.config(background="green")
        else:
            self.questions_space.config(background="red")
        self.window.after(1000, self.get_next_question)
