import tkinter as tk

window = tk.Tk()

window.geometry("950x780")
window.title("First Python Software")

label = tk.Label(window, text="This my first software", font =("Helvetica", 30), fg="#52f747")
label.pack(expand=True)

window.mainloop()