#!/usr/bin/python3

import sys

def errors(var):
    if len(var) != 3:
        print("AssertionError: more than one argument are provided")
        return(False)
   # for i in sys.argv[1]:
    if not var[1].isdigit() or not var[2].isdigit():
        print("No es un numero")
        return(False)
    return (True)

if __name__ == "__main__":
    if not errors(sys.argv):
        exit()
    print("Sum:        " + str(int(sys.argv[1]) + int(sys.argv[2])))
    print("Differencie:" + str(int(sys.argv[1]) - int(sys.argv[2])))
    print("Product:    " + str(int(sys.argv[1]) * int(sys.argv[2])))
    try:
        print("Quotient:   " + str(int(sys.argv[1]) / int(sys.argv[2])))
        print("Quotient:   " + str(int(sys.argv[1]) % int(sys.argv[2])))

    except ZeroDivisionError:
        print("Quotient:   ERROR (division by zero)")
        print("Remainder:  ERROR (modulo by zero)")
    