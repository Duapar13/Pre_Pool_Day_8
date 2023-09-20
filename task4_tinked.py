import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Animating Stickman")

# Create a Canvas
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

# Initialize the stickman's positions
left_arm_up = True
right_arm_up = False
left_leg_up = True
right_leg_up = False

# Function to animate the stickman
def animate_stickman():
    global left_arm_up, right_arm_up, left_leg_up, right_leg_up

    # Move the arms up and down
    if left_arm_up:
        canvas.move(left_arm, 0, -5)
        left_arm_up = False
    else:
        canvas.move(left_arm, 0, 5)
        left_arm_up = True

    if right_arm_up:
        canvas.move(right_arm, 0, -5)
        right_arm_up = False
    else:
        canvas.move(right_arm, 0, 5)
        right_arm_up = True

    # Move the legs up and down
    if left_leg_up:
        canvas.move(left_leg, 0, -5)
        left_leg_up = False
    else:
        canvas.move(left_leg, 0, 5)
        left_leg_up = True

    if right_leg_up:
        canvas.move(right_leg, 0, -5)
        right_leg_up = False
    else:
        canvas.move(right_leg, 0, 5)
        right_leg_up = True

    # Schedule the next animation frame after 500 milliseconds
    root.after(500, animate_stickman)

# Draw the stickman's head (a circle)
head = canvas.create_oval(80, 50, 120, 90, outline="black", fill="white")

# Draw the stickman's body (a line)
body = canvas.create_line(100, 90, 100, 170, fill="black")

# Draw the stickman's arms (two lines)
left_arm = canvas.create_line(100, 100, 60, 130, fill="black")
right_arm = canvas.create_line(100, 100, 140, 130, fill="black")

# Draw the stickman's legs (two lines)
left_leg = canvas.create_line(100, 170, 60, 220, fill="black")
right_leg = canvas.create_line(100, 170, 140, 220, fill="black")

# Start the animation
animate_stickman()

# Run the Tkinter main loop
root.mainloop()
