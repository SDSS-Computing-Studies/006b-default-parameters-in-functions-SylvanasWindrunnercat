#!python3

import assignment


def tempConversion(a,b):
    if b == "F":
        a = int(a)
        c = 5 * a / 9
        return c
    else:
        a = int(a)
        d = 1.8 * a + 32
        return d

c = input("The number is:")
d = input("It is celsius or fahrenheit:")

x = tempConversion(c,d)

print(x)
