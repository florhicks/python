from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain ):
        self.quiz =quiz_brain

        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_canvas = self.canvas.create_text(150, 125, text="Text goes here.", font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50,pady=50)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(relief="flat", highlightthickness=0, image=true_button_image, command=self.true)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(relief="flat", highlightthickness=0, image=false_button_image,command=self.false)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white",font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text_canvas, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)




    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
