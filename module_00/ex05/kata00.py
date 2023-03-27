#!/usr/bin/python3

kata = (19,(42, 4) ,21)
print(type(kata))
print("The " + str(len(kata)) + " numbers are:", end=" ")
for t in range(len(kata)):
    if t < len(kata) -1 :
        print(kata[t], end=", ")
    else:
        print(kata[t])