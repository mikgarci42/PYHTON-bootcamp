import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument are provided")
        exit()
   # for i in sys.argv[1]:
    if not sys.argv[1].isdigit():
        print("No es un numero")
        exit ()
    if int(sys.argv[1]) == 0:
        print("I'm Zero")
        exit ()
    if int(sys.argv[1]) % 2 == 1:
        print("I'm Odd")
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even")

    