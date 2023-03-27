#!/usr/bin/python3
import sys
import string

def text_analyzer(message=None):
    """
    Recibe un argumento por parametro e imprime las letras que tiene, mayusculas, minisculas, espacios y signos de puntuacion
    """
    if not message:
        message = input("What is the text to analyze?\n")
    print("The text contains " + str(len(message)) + " character(s)")
    print("Capital Letters: ", sum(1 for c in message if c.isupper()))
    print("Lower Letters: ", sum(1 for c in message if c.islower()))
    print("Punctuation mark(s): ", sum(1 for c in message if c in string.punctuation))
    print("Space(s): ", sum(1 for c in message if c.isspace()))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    if len(sys.argv) == 1:
        text_analyzer("")