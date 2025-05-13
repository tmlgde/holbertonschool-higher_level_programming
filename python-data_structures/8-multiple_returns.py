#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)

    longueur = len(sentence)
    premier = sentence[0]

    return (longueur, premier)
