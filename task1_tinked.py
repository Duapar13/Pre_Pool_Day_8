import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Example")

label_frame = tk.LabelFrame(root, text="Label Frame")
label_frame.pack(padx=20, pady=20)

inner_frame = tk.Frame(label_frame)
inner_frame.pack(padx=10, pady=10)

label = tk.Label(inner_frame, text="This is an inner Frame.")
label.pack()

button = tk.Button(inner_frame, text="Click Me")
button.pack()

# Run the Tkinter main loop
root.mainloop()
