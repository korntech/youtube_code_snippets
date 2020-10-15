import tkinter as tk


def print_sth(text):
    print(text)


master = tk.Tk()
master.title("Learning lambda...")
master.geometry("400x300")
master.grid_columnconfigure(0, weight=1)

button = tk.Button(
    master, text="Click me", command=lambda: print_sth("Learning lambda..")
)
button.grid(column=0, row=1)

master.mainloop()
