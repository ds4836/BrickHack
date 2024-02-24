import tkinter as tk
from tkinter import filedialog

def confirm_button_click():
    file_path = file_path_entry.get()
    # Do something with the file path, such as printing it
    print("File path:", file_path)

root = tk.Tk()

# Create a label and entry for the file path
file_path_label = tk.Label(root, text="File Path:")
file_path_label.pack()
file_path_entry = tk.Entry(root)
file_path_entry.pack()

# Create a button to confirm
confirm_button = tk.Button(root, text="Confirm", command=confirm_button_click)
confirm_button.pack()

root.mainloop()