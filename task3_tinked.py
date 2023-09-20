import tkinter as tk

root = tk.Tk()
root.title("Nestor")

canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

head = canvas.create_oval(80, 50, 120, 90, outline="RED", fill="Brown")

body = canvas.create_line(100, 90, 100, 170, fill="Brown")


left_arm = canvas.create_line(100, 100, 60, 130, fill="Brown")
right_arm = canvas.create_line(100, 100, 140, 130, fill="Brown")

left_leg = canvas.create_line(100, 170, 60, 220, fill="Brown")
right_leg = canvas.create_line(100, 170, 140, 220, fill="Brown")

text = canvas.create_text(100, 30, text="Nestor", fill="Brown")

root.mainloop()
