#!python3
def factor(a):
    output = []
    i = 2
    while a // i > 0:
        if a % i == 0:
            output.append(i)
            a //= i
        else: i += 1
    return(output)

print(factor(12))

b = int(input("The number1 is:"))
c = int(input("The number2 is:"))

d = b * c

x = factor(d)

print(x)
