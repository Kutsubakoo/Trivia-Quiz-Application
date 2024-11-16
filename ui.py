from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_label.grid(column=1, row=0, pady=15, padx=15)

        self.canvas = Canvas(width=300, height=250)
        self.question_label = self.canvas.create_text(150,
                                                      125,
                                                      width=280,
                                                      text="test",
                                                      fill=THEME_COLOR,
                                                      font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2, pady=20, padx=5)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2, pady=20, padx=5)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_label, text=f"You've reached the end of the quiz. You got "
                                                             f"{self.quiz.score} correct answers!")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




