import tkinter as tk
from tkinter import filedialog

def confirm_file_path():
    file_path = file_path_entry.get()
    print("File path:", file_path)

def confirm_field1():
    input1 = input_entry1.get()
    print("Input 1:", input1)

def confirm_field2():
    input2 = input_entry2.get()
    print("Input 2:", input2)

def change_frame():
    global input_entry1, input_entry2
    for widget in root.winfo_children():
        widget.destroy()

    new_frame = tk.Frame(root)

    input_label1 = tk.Label(new_frame, text="Input 1:")
    input_label1.pack()
    input_entry1 = tk.Entry(new_frame)
    input_entry1.pack()

    confirm_button1 = tk.Button(new_frame, text="Confirm1", command=confirm_field1)
    confirm_button1.pack()

    input_label2 = tk.Label(new_frame, text="Input 2:")
    input_label2.pack()
    input_entry2 = tk.Entry(new_frame)
    input_entry2.pack()

    confirm_button2 = tk.Button(new_frame, text="Confirm2", command=confirm_field2)
    confirm_button2.pack()

    

    back_button = tk.Button(new_frame, text="Back", command=main_frame)
    back_button.pack()

    new_frame.pack()

def main_frame():
    global file_path_entry
    for widget in root.winfo_children():
        widget.destroy()

    root_frame = tk.Frame(root)

    file_path_label = tk.Label(root_frame, text="File Path:")
    file_path_label.pack()
    file_path_entry = tk.Entry(root_frame)
    file_path_entry.pack()

    confirm_button = tk.Button(root_frame, text="Confirm", command=confirm_file_path)
    confirm_button.pack()

    change_frame_button = tk.Button(root_frame, text="Change Frame", command=change_frame)
    change_frame_button.pack()

    root_frame.pack()

root = tk.Tk()
main_frame()
root.mainloop()