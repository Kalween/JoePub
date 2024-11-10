from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BUTTON_TRUE = 'images/true.png'
BUTTON_FALSE = 'images/false.png'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)

        self.score_label = Label(text="Score 0",padx=20, pady=20,fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some Question text", 
            fill=THEME_COLOR,
            font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file=BUTTON_TRUE)
        self.false_img = PhotoImage(file=BUTTON_FALSE)

        self.button_true = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=10, column=0, padx=20,pady=20)

        self.button_false = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=10, column=1, padx=20, pady=20)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score:{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quizz")
            self.button_true.config(state='diabled')
            self.button_false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        