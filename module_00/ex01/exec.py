import sys

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        sys.exit() 
    print ("Number of arguments:" + str(len(sys.argv)) + "arguments.")
    print ("Argument List:" + str(sys.argv))
    print ("Argument List:" + str(sys.argv[0]))
    output = ""
    for i in range (1, len(sys.argv)):
        for j in sys.argv[i]:
            if j.islower():
                output += str(j.upper())
            else:
                output += str(j.lower())
        if i != len(sys.argv) - 1:
            output += ' '        
    print (output)
    output = output [::-1]
    print (output)
