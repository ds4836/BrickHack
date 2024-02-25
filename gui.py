import random
import tkinter as tk
from tkinter import filedialog

from api import parse_csv, post_data, get_question, reset_limit_questions

import tkinter as tk
global correct_answer, total_guesses, correct_guesses
total_guesses = 0
correct_guesses = 0
correct_answer = "D"
limit_questions = reset_limit_questions()

def check_answer(selected_option, label, radio_buttons, button):
    global correct_answer, total_guesses, correct_guesses
    total_guesses += 1
    if correct_answer == selected_option.get():
        correct_guesses += 1
        question = question_customized()
        label.config(text=question[0])
        alpha = ["A) ", "B) ", "C) ", "D) "]
        for i in range(4):  # Update the text of the radio buttons
            radio_buttons[i].config(text=alpha[i] + question[i+1])
        correct_answer = question[5]
    elif gui.check_vars[1].get() == 0:  # If "Unlimited Guesses" is not checked
        question = question_customized()
        label.config(text=question[0])
        alpha = ["A) ", "B) ", "C) ", "D) "]
        for i in range(4):  # Update the text of the radio buttons
            radio_buttons[i].config(text=alpha[i] + question[i+1])
        correct_answer = question[5]

    # Disable the button
    button.config(state="disabled")

    # Enable the button after 0.2 seconds
    button.after(200, lambda: button.config(state="normal"))

def question_customized():
    global limit_questions
    if gui.check_vars[0].get() == 0:
        limit_questions -= 1
        if limit_questions == 0:
            gui.end_quiz()
            limit_questions = reset_limit_questions()
            return
    if gui.check_vars[3].get() == 1:
        data = list(get_question(True))
    else:
        data = list(get_question())
    question = data[0]
    options = data[1:5]
    correct = data[5]
    correct_option = "C"

    if gui.check_vars[2].get() == 1:
        if data[5] == "A":
            correct_option = data[1]
        elif data[5] == "B":
            correct_option = data[2]
        elif data[5] == "C":
            correct_option = data[3]
        elif data[5] == "D":
            correct_option = data[4]

        # Randomize the order of the options
        random.shuffle(options)

        for i in options:
            if i == correct_option:
                if options.index(i) == 0:
                    correct = "A"
                elif options.index(i) == 1:
                    correct = "B"
                elif options.index(i) == 2:
                    correct = "C"
                elif options.index(i) == 3:
                    correct = "D"
                break

    return (question, *options, correct)

def add_question(textbox1, textbox2, textbox3, textbox4, textbox5, textbox6):
    data = {
    "app": "3",
    "record": {
        "question": {"value": textbox1.get()},
        "option1": {"value": textbox2.get()},
        "option2": {"value": textbox3.get()},
        "option3": {"value": textbox4.get()},
        "option4": {"value": textbox5.get()},
        "correct": {"value": textbox6.get()},
        }
    }
    textbox1.delete(0, "end")
    textbox2.delete(0, "end")
    textbox3.delete(0, "end")
    textbox4.delete(0, "end")
    textbox5.delete(0, "end")
    textbox6.delete(0, "end")
    post_data(data)

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry("400x300")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}

        self.create_main_frame()
        self.create_input()
        self.create_guess_frame()
        self.create_quiz_customize()  # Create the quiz customize frame

        self.show_frame("main")
        
    def create_main_frame(self, label_text=None):
        main_frame = tk.Frame(self)

        if label_text == None:
            label_text = "Welcome to the Quiz!"
        self.main_label = tk.Label(main_frame, text=label_text)  # Store the label in an instance variable
        self.main_label.pack()

        button1 = tk.Button(main_frame, text="Add questions", command=lambda: self.show_frame("input_frame"))
        button1.pack()
        
        button2 = tk.Button(main_frame, text="Quiz", command=lambda: self.show_frame("guessing_frame"))
        button2.pack()

        # Add a button to customize the quiz
        button3 = tk.Button(main_frame, text="Customize Quiz", command=lambda: self.show_frame("quiz_customize_frame"))
        button3.pack()

        self.frames["main"] = main_frame
        
    def create_input(self):
        input_frame = tk.Frame(self)
        
        textboxes = []  # Create a list to store the textboxes
        text_fields = ["Question", "Option 1", "Option 2", "Option 3", "Option 4", "Correct Answer"]
        for i in range(6):  # Create 6 text boxes
            label = tk.Label(input_frame, text=text_fields[i])
            label.grid(row=i, column=0)
            textbox = tk.Entry(input_frame)
            textbox.grid(row=i, column=1)
            textboxes.append(textbox)  # Add the textbox to the list

        confirm_button = tk.Button(input_frame, text="Confirm", command=lambda: add_question(*textboxes))
        confirm_button.grid(row=6, column=0, columnspan=2)

        back_button = tk.Button(input_frame, text="Back to Main", command=lambda: self.show_frame("main"))
        back_button.grid(row=7, column=0, columnspan=2)

        self.frames["input_frame"] = input_frame
        
    def create_guess_frame(self):
        global correct_answer
        guessing_frame = tk.Frame(self)

        question = get_question()
        
        label = tk.Label(guessing_frame, text=question[0])  # Create a label
        label.pack(anchor='w')  # Pack the label at the top of the frame

        selected_option = tk.StringVar()  # Create a variable to store the selected option

        radio_buttons = []  # Create a list to store the radio buttons
        alpha = ["", "A) ", "B) ", "C) ", "D) "]

        for i in range(1, 5):  # Create 4 radio buttons
            radio_button = tk.Radiobutton(guessing_frame, text=alpha[i] + question[i], variable=selected_option, value=chr(64 + i))
            radio_button.pack(anchor='w')  # Pack the radio button on the left side of the frame
            radio_buttons.append(radio_button)  # Add the radio button to the list

        correct_answer = question[5]

        # Create a frame to contain the buttons
        button_frame = tk.Frame(guessing_frame)
        button_frame.pack(anchor='w')

        # In the create_guess_frame method
        button = tk.Button(button_frame, text="Check", command=lambda: check_answer(selected_option, label, radio_buttons, button))
        button.pack(side='left')  # Pack the button on the left side of the button frame

        back_button = tk.Button(button_frame, text="End Quiz", command=lambda: self.end_quiz())
        back_button.pack(side='left', padx=5)  # Pack the button on the left side of the button frame with a padding of 5 pixels

        self.frames["guessing_frame"] = guessing_frame

    def create_quiz_customize(self):
        quiz_customize_frame = tk.Frame(self)

        self.check_vars = []  # Create a list to store the variables for the checkboxes
        option_text = ["Unlimited Questions", "Unlimited Guesses", "Randomize Options", "Unique Questions"]
        for i in range(4):  # Create 4 checkboxes
            check_var = tk.IntVar()  # Create a variable for the checkbox
            checkbox = tk.Checkbutton(quiz_customize_frame, text=option_text[i], variable=check_var)
            checkbox.pack(anchor='w')  # Pack the checkbox on the left side of the frame
            self.check_vars.append(check_var)  # Add the variable to the list

        back_button = tk.Button(quiz_customize_frame, text="Back to Main", command=lambda: self.show_frame("main"))
        back_button.pack()

        self.frames["quiz_customize_frame"] = quiz_customize_frame

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_remove()  # Hide all frames
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nsew")  # Show the desired frame
        self.update_idletasks()  # Force the window to update
    
    def end_quiz(self):
        global total_guesses, correct_guesses, limit_questions
        self.main_label.config(text=f"You got {correct_guesses} out of {total_guesses} correct!")  # Update the main label
        total_guesses = 0
        correct_guesses = 0
        limit_questions = reset_limit_questions()

        self.show_frame("main")

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()