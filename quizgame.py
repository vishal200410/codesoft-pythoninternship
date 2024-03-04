import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is 40 + 55?",
                "options": ["92", "95", "82", "70"],
                "answer": "95"
            },
            {
                "question": "Who wrote 'Harry Potter' series?",
                "options": ["J.K. Rowling", "Stephen King", "George R.R. Martin", "J.R.R. Tolkien"],
                "answer": "J.K. Rowling"
            }
        ]
        self.current_question_index = 0
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack()
            self.option_buttons.append(button)

        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question_index]
        if question_data["options"][selected_option] == question_data["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect!", "Your answer is incorrect!")

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
            self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()