import tkinter as tk
from tkinter import filedialog

from test import parse_csv, post_data

def confirm_file_path():
    parse_csv(file_path_entry.get())
    

def confirm_fields():
    checkbox_values = []
    if checkbox_var1.get():
        checkbox_values.append("sample1")
    if checkbox_var2.get():
        checkbox_values.append("sample2")
    if checkbox_var3.get():
        checkbox_values.append("sample3")
    if checkbox_var4.get():
        checkbox_values.append("sample4")

    data = {
        "app": "3",
        "record": {
            "test1": {"value": input_entry1.get()},
            "test2": {"value": input_entry2.get()},
            "number": {"value": int_input_entry.get()},
            "multiChoice": {"value": checkbox_values},
        }
    }
    post_data(data)


def change_frame():
    global input_entry1, input_entry2, checkbox1, checkbox2, checkbox3, checkbox4, int_input_entry, checkbox_var1, checkbox_var2, checkbox_var3, checkbox_var4
    for widget in root.winfo_children():
        widget.destroy()

    new_frame = tk.Frame(root)
    
    checkbox_var1 = tk.IntVar()
    checkbox_var2 = tk.IntVar()
    checkbox_var3 = tk.IntVar()
    checkbox_var4 = tk.IntVar()

    checkbox_label = tk.Label(new_frame, text="Checkboxes:")
    checkbox_label.pack()

    checkbox1 = tk.Checkbutton(new_frame, text="Checkbox 1", variable=checkbox_var1)
    checkbox1.pack()
    checkbox2 = tk.Checkbutton(new_frame, text="Checkbox 2", variable=checkbox_var2)
    checkbox2.pack()
    checkbox3 = tk.Checkbutton(new_frame, text="Checkbox 3", variable=checkbox_var3)
    checkbox3.pack()
    checkbox4 = tk.Checkbutton(new_frame, text="Checkbox 4", variable=checkbox_var4)
    checkbox4.pack()

    int_input_label = tk.Label(new_frame, text="Integer Input:")
    int_input_label.pack()
    int_input_entry = tk.Entry(new_frame)
    int_input_entry.pack()
    input_label1 = tk.Label(new_frame, text="Input 1:")
    input_label1.pack()
    input_entry1 = tk.Entry(new_frame)
    input_entry1.pack()


    input_label2 = tk.Label(new_frame, text="Input 2:")
    input_label2.pack()
    input_entry2 = tk.Entry(new_frame)
    input_entry2.pack()

    confirm_button = tk.Button(new_frame, text="Confirm2", command=confirm_fields)
    confirm_button.pack()

    

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