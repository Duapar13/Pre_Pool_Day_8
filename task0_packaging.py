import tkinter as tk

root = tk.Tk()
root.title("Game GUI")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

gui_frame = tk.Frame(root, bg="gray")
gui_frame.place(relx=0.5, rely=0.05, relwidth=0.95, relheight=0.1, anchor="n")

score_label = tk.Label(gui_frame, text="Score: 0", font=("Arial", 16), bg="gray")
score_label.pack(side="left")

time_label = tk.Label(gui_frame, text="Time: 0:00", font=("Arial", 16), bg="gray")
time_label.pack(side="left")

life_label = tk.Label(gui_frame, text="Life:", font=("Arial", 16), bg="gray")
life_label.pack(side="left")
life_bar = tk.Label(gui_frame, text="██████████", font=("Arial", 16), bg="red")
life_bar.pack(side="left")

inventory_label = tk.Label(gui_frame, text="Inventory:", font=("Arial", 16), bg="gray")
inventory_label.pack(side="left")
inventory = tk.Label(gui_frame, text="Items: 0", font=("Arial", 16), bg="gray")
inventory.pack(side="left")


# Start the main loop
root.mainloop()
