import tkinter as tk
from tkinter import filedialog

root = tk.TK()
root.withdraw()

file_path = filedialog.askopenfilename()
#file_path = filedialog.askdirectory()  --> to select the folder path.
print(file_path)

input('press any key to exit')

