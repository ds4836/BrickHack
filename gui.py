import tkinter as tk
from tkinter import filedialog

from api import parse_csv, post_data, get_question

import tkinter as tk
global correct_answer
correct_answer = "D"
def check_answer(checkbox1var, checkbox2var, checkbox3var, checkbox4var, checkbox1, checkbox2, checkbox3, checkbox4, label):
        global correct_answer
        result = False
        if correct_answer == "A" and checkbox1var.get() == 1:
            result = True
        elif correct_answer == "B" and checkbox2var.get() == 1:
            result = True
        elif correct_answer == "C" and checkbox3var.get() == 1:
            result = True
        elif correct_answer == "D" and checkbox4var.get() == 1:
            result = True
        if result:
            question = get_question()
            label.config(text=question[0])
            checkbox1.config(text=question[1])
            checkbox2.config(text=question[2])
            checkbox3.config(text=question[3])
            checkbox4.config(text=question[4])
            correct_answer = question[5]
        print(correct_answer)

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

        self.show_frame("main")
        
    def create_main_frame(self):
        main_frame = tk.Frame(self)
        
        button1 = tk.Button(main_frame, text="Add questions", command=lambda: self.show_frame("input_frame"))
        button1.pack()
        
        button2 = tk.Button(main_frame, text="Quiz", command=lambda: self.show_frame("guessing_frame"))
        button2.pack()
        
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
        label.pack()  # Pack the label at the top of the frame
        checkbox1var = tk.IntVar()
        checkbox2var = tk.IntVar()
        checkbox3var = tk.IntVar()
        checkbox4var = tk.IntVar()
        
        checkbox1 = tk.Checkbutton(guessing_frame, text=question[1], variable=checkbox1var)
        checkbox1.pack()
        
        checkbox2 = tk.Checkbutton(guessing_frame, text=question[2], variable=checkbox2var)
        checkbox2.pack()
        
        checkbox3 = tk.Checkbutton(guessing_frame, text=question[3], variable=checkbox3var)
        checkbox3.pack()
        
        checkbox4 = tk.Checkbutton(guessing_frame, text=question[4], variable=checkbox4var)
        checkbox4.pack()
        correct_answer = question[5]
        button = tk.Button(guessing_frame, text="Submit", command=lambda: check_answer(checkbox1var, checkbox2var, checkbox3var, checkbox4var, checkbox1, checkbox2, checkbox3, checkbox4, label))
        button.pack()

        back_button = tk.Button(guessing_frame, text="Back to Main", command=lambda: self.show_frame("main"))
        back_button.pack()

        self.frames["guessing_frame"] = guessing_frame
        
    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_remove()  # Hide all frames
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nsew")  # Show the desired frame
        self.update_idletasks()  # Force the window to update

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()