#!/usr/bin/python3

#Hay que utilizar el format del print

kata = (2009, 9, 2, 3, 30)

print("{:02}/{:02}/{:02} {:02}:{:02}".format(kata[1], kata[2], kata[0] % 100, kata[3], kata[4]))