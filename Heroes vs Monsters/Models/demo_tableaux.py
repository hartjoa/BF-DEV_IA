# Créer grille de 10 x 10 cases
# Chaque élement contient:
# - '.' pour une case vide
# - 'O' pour un obstacle (infranchissable)
# - 'P' pout le personnage

import os
import keyboard
import time

grille = [
    ['.', '.', 'O', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'O', '.', '.', '.', '.', 'O', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'O', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.'],
    ['.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]

# position initiale du personnage (en haut à gauche)
x, y = 0, 0

def afficher_grille():
    """
    Rafraîchir l'affichage de la grille dans la console
    Affiche:
    - '.' pour une case vide
    - 'O' pour un obstacle (infranchissable)
    - 'P' pout le personnage
    """
    os.system("cls" if os.name == "nt" else "clear")

    for row in range(10):
        for column in range(10):
            # On affiche 'P' si c'est la position du personnage
            if row == x and column == y:
                print("P", end = " ")
            # Sinon on affiche le contenu de la grille
            else:
                print(grille[row][column], end = " ")
        print() # saut de ligne après chaque ligne de la grille

try:
    afficher_grille()

    while True:
        # On utilise un flag pour savoir si un déplacement a été effectué
        mouvement = False

        # Détection des touches directionnelles avec keyboard.is_pressed

        # Haut
        if keyboard.is_pressed("up"):
            if x > 0 and grille[x - 1][y] == ".":   # on ne sort pas de la grille et on ne 'marche' pas sur un obstacle
                x -= 1
                mouvement = True

        # Down
        if keyboard.is_pressed("down"):
            if x < 9 and grille[x + 1][y] == ".":   
                x += 1
                mouvement = True

        # Gauche
        if keyboard.is_pressed("left"):
            if y > 0 and grille[x][y - 1] == ".":
                y -= 1
                mouvement = True

        # Droite
        if keyboard.is_pressed("right"):
            if y < 9 and grille[x][y + 1] == ".":   
                y += 1
                mouvement = True

        if mouvement:
            afficher_grille()
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Merci d'avoir joué")