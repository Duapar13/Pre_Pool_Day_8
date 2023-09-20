import random

def devine_le_nombre():
    nombre_a_deviner = random.randint(1, 100)
    nombre_essais = 0
    
    print("Bienvenue dans Devine le Nombre!")
    print("Je choisis un nombre entre 1 et 100. À vous de deviner!")
    
    while True:
        supposition = input("Entrez votre supposition (ou 'q' pour quitter) : ")
        
        if supposition.lower() == 'q':
            print(f"Le nombre à deviner était {nombre_a_deviner}. Au revoir!")
            break
        
        try:
            supposition = int(supposition)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        
        nombre_essais += 1
        
        if supposition < nombre_a_deviner:
            print("Le nombre à deviner est plus grand.")
        elif supposition > nombre_a_deviner:
            print("Le nombre à deviner est plus petit.")
        else:
            print(f"Bravo! Vous avez deviné le nombre en {nombre_essais} essais!")
            break

if __name__ == "__main__":
    devine_le_nombre()
