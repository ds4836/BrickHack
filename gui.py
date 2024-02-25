import tkinter as tk
from tkinter import filedialog

from api import parse_csv, post_data

import tkinter as tk

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
        
        label = tk.Label(guessing_frame, text="This is Frame 3")  # Create a label
        label.pack()  # Pack the label at the top of the frame
        
        checkbox1 = tk.Checkbutton(guessing_frame, text="")
        checkbox1.pack()
        
        checkbox2 = tk.Checkbutton(guessing_frame, text="Checkbox 2")
        checkbox2.pack()
        
        checkbox3 = tk.Checkbutton(guessing_frame, text="Checkbox 3")
        checkbox3.pack()
        
        checkbox4 = tk.Checkbutton(guessing_frame, text="Checkbox 4")
        checkbox4.pack()
        
        button = tk.Button(guessing_frame, text="Submit")
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