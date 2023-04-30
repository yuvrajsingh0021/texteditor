import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt")
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_box.get("1.0", tk.END)
        output_file.write(text)

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_box.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_box.insert(tk.END, text)

window = tk.Tk()
window.title("yv Text")

text_box = tk.Text(window)
text_box.pack()

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()
