#!/usr/bin/python3.10

import random



mots = ["ARBRE", "ENFANT", "CHEMIN", "PROJET", "PYTHON"]


def choisir_mot():
    return random.choice(mots)


def afficher_mot(mot, lettres_trouvees):
    return "".join([lettre if lettre in lettres_trouvees else "*" for lettre in mot])


def jeu_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    lettres_proposees = set()
    nombre_essais = 6
    
    print("Bienvenue au jeu du pendu !")
    
    while nombre_essais > 0:
        print("\nMot à deviner : ", afficher_mot(mot_a_deviner, lettres_trouvees))
        print(f"Lettres proposées : {', '.join(sorted(lettres_proposees))}")
        print(f"Nombre d'essais restants : {nombre_essais}")
        
        # ajouter un bloc try catch ici
        lettre = input("Proposez une lettre : ").upper()
        
        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre. Essayez une autre lettre.")
            continue
        
        lettres_proposees.add(lettre)
        
        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            if set(mot_a_deviner).issubset(lettres_trouvees):
                print(f"\nFélicitations ! Vous avez deviné le mot : {mot_a_deviner}")
                break
        else:
            nombre_essais -= 1
            print(f"Lettre incorrecte. Vous perdez un essai.")
        
    if nombre_essais == 0:
        print(f"\nDésolé, vous avez perdu. Le mot à deviner était : {mot_a_deviner}")




# Lancer le jeu du pendu
if __name__ == "__main__":
  jeu_pendu()














