from typing import List
from collections.abc import Iterable
import random

def print_word(word, found_letters):
    return print("".join([letter if letter in found_letters else "*" for letter in word]))


def play(word:str, nb_tries:int, letters:Iterable):
    found_letters = set()
    win = False

    for letter in letters:
        print_word(word, found_letters)
        print(f"essais : {nb_tries}")
        if nb_tries == 0:
            break

        if letter in word:
            found_letters.add(letter)
        else:
            nb_tries -= 1

        if set(word) == found_letters:
            win = True
            print("!!! BRAVO !!!")
            break      
    
    return win


# Lancer le jeu du pendu
if __name__ == "__main__":

    mots = ["ARBRE", "ENFANT", "CHEMIN", "PROJET", "PYTHON"]
    mot = random.choice(mots)

    def create_input_generator() :
        while True :
            yield input("Proposez une lettre : ").upper()

    play(mot, 2, create_input_generator())
    

