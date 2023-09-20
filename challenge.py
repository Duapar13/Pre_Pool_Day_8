import tkinter as tk

def create_sphere_with_shadow(canvas, x, y, radius):
    # Créer l'ellipse de l'ombre étendue vers la droite
    shadow_x = x + 30  # Ajustez la coordonnée x de l'ombre pour l'étendre vers la droite
    shadow_y = y + 10  # Ajustez la coordonnée y de l'ombre si nécessaire
    canvas.create_oval(shadow_x - radius, shadow_y - radius + 20, shadow_x + radius + 40, shadow_y + radius + 20, fill='black', outline='gray')

    # Créer la sphère principale (ellipse)
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='white', outline='black')

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Sphère avec ombre étendue")

# Créer un widget canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Appeler la fonction pour créer la sphère avec l'ombre étendue
create_sphere_with_shadow(canvas, 200, 200, 50)

# Exécuter la boucle principale Tkinter
root.mainloop()
