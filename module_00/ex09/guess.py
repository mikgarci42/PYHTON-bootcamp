#!/usr/bin/python3
from random import randint

if __name__ == "__main__":
    print("This is an interactvie guessing game.\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit'to end the game.\nGood luck!\n\n")
    val = randint(0, 99)
    ejem = 1

    while True:
        try:
            numero = input("What's your guess between 1 and 99?\n")
            numero = int(numero)
            if numero < 0 or numero > 99:
                raise
            if numero > val: print("Demasiado alto.")
            elif numero < val: print("Demasiado bajo.")
            elif numero == val:
                print("Felicidades, los has adivinad en " + str(ejem) + " intentos.")
                break
            ejem += 1

        except ValueError:
            print("Expresion no valida")
        except KeyboardInterrupt:
            print("\n¡Se ha interrumpido la ejecución del programa!")
            break
        except:
            print("Numero introducido fuera de rango")    

