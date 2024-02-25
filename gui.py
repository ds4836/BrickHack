import tkinter as tk
from tkinter import filedialog

from api import parse_csv, post_data, get_question

import tkinter as tk

def check_answer(checkbox1var, checkbox2var, checkbox3var, checkbox4var, correct_answer):
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
            print("Correct!")

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
        
        button1 = tk.Button(main_frame, text="Go to Frame 2", command=lambda: self.show_frame("input_frame"))
        button1.pack()
        
        button2 = tk.Button(main_frame, text="Go to Frame 3", command=lambda: self.show_frame("guessing_frame"))
        button2.pack()
        
        self.frames["main"] = main_frame
        
    def create_input(self):
        input_frame = tk.Frame(self)
        
        for i in range(5):  # Create 5 text boxes
            label = tk.Label(input_frame, text=f"Text Box {i+1}:")
            label.grid(row=i, column=0)
            textbox = tk.Entry(input_frame)
            textbox.grid(row=i, column=1)

        confirm_button = tk.Button(input_frame, text="Confirm")
        confirm_button.grid(row=5, column=0, columnspan=2)

        back_button = tk.Button(input_frame, text="Back to Main Frame", command=lambda: self.show_frame("main"))
        back_button.grid(row=6, column=0, columnspan=2)

        self.frames["input_frame"] = input_frame
        
    def create_guess_frame(self):
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
        
        button = tk.Button(guessing_frame, text="Submit", command=lambda: check_answer(checkbox1var, checkbox2var, checkbox3var, checkbox4var, question[5]))
        button.pack()
        
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