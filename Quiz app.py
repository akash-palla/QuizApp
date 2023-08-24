import tkinter as tk
from tkinter import Radiobutton
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.quiz = [ {
            "question" : " What is the most common type of cyberattack? ",
            "options" : ["Phishing","Ransomware","Data Breach","DOS"],
            "answer" : 0
        },
        {
        "question": " What is a zero-day attack? ",
        "options": ["A cyberattack that exploits a vulnerability in software that the software vendor is not aware of","A cyberattack that targets a specific individual or organization","A cyberattack that uses social engineering to trick the victim into clicking on a malicious link","A cyberattack that uses a denial-of-service attack to make a website or service unavailable"],
        "answer": 0
        },
        {

            "question": " What is the best way to protect yourself from phishing attacks? ",
            "options": ["Install a firewall","Keep your software up to date","Be careful about what links you click on","All of the above"],
            "answer": 3
        },
        {
            "question": " What is a denial-of-service attack? ",
            "options": ["An unauthorized access to sensitive data","A type of cyberattack that encrypts your files and demands a ransom payment to decrypt them","A type of cyberattack that floods a website with traffic, making it unavailable to users","A type of cyberattack that tries to trick you into giving up your personal information"],
            "answer": 2
        },
        {
            "question": " What is a man-in-the-middle attack? ",
            "options": ["A cyberattack that intercepts communications between two parties","A cyberattack that exploits a vulnerability in software that the software vendor is not aware of","A cyberattack that targets a specific individual or organization","A cyberattack that uses social engineering to trick the victim into clicking on a malicious link"],
            "answer": 0
        }

                    ]
        
        self.current_Qindex = 0
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Cybersecurity Quiz")

        self.Qlabel = tk.Label(self.window, text="", font=("Open Sans", 18))
        self.Qlabel.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        self.options_frame = tk.Frame(self.window)
        self.options_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        self.options=[]
        self.selected_option = tk.IntVar()
        for i in range(4):
            option = Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=i,
                command=self.check,
                font=("Open Sans", 12)  # Set the font for the option text
            )
            option.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.options.append(option)

        self.answered = [False] * len(self.quiz)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=20, command=self.nextQ)
        self.next_question_button.grid(row=2, column=0, padx=20, pady=15, sticky="w")

    def start(self):
        self.loadQ()
        self.window.mainloop()

    def check(self):
        if self.answered[self.current_Qindex]:
            messagebox.showerror("Already Answered", "You've already answered this question.")
            return

        selected = self.selected_option.get()

        if selected == -1:
            messagebox.showerror("No Answer", "Please select an answer.")
            return

        self.answered[self.current_Qindex] = True
        answer = self.quiz[self.current_Qindex]["answer"]

        if selected == answer:
            self.score += 1
            messagebox.showinfo("Correct", "You're right")
        else:
            self.score -= 0.25
            messagebox.showerror("Incorrect", "Your answer is Incorrect")

        for option in self.options:
            option.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)

    def loadQ(self):
        Qdata = self.quiz[self.current_Qindex]
        self.Qlabel.config(text = Qdata["question"])
        options = Qdata["options"]
        for i in range(4):
            self.options[i].config(text=options[i], state=tk.NORMAL)
        self.selected_option.set(-1)

    def nextQ(self):
        self.current_Qindex+= 1
        if self.current_Qindex == len(self.quiz):
            messagebox.showinfo("You have completed the Quiz", f" Your score : {self.score}/{len(self.quiz)}")
            self.window.destroy()
        else:
            self.loadQ()

cysec_quiz = QuizApp()
cysec_quiz.start()

