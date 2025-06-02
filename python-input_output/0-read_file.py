#!/usr/bin/python3
def read_file(filename=""):
    """Lit un fichier texte UTF-8 et affiche son contenu sur stdout"""
    with open(filename, "r") as file:
        print(file.read(), end="")

