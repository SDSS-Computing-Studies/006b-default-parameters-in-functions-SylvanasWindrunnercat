#! python3

import math

def tempConversion(tm,by = "C"):
    if by == "C":
        a = (tm * 9 / 5) + 32
    elif by == "F":
        a = 5 * (tm - 32) / 9
    a = round(a,1)
    return a

def factorPair(a,b):
    numlist = []
    numlist.append(b)
    numlist.apped(a / b)
    numlist.sort()
    return numlist

def toRadians(degree):
    result = math.pi / 180 * degree
    return result

def solution(x):
    x.sort()
    yoxi = x[1]
    return yoxi

def quadratic(t,u,i):
    a1 = (-u + math.sqrt(u ** 2 - 4 * t * i)) / (2 * t)
    a2 = (-u - math.sqrt(u ** 2 - 4 * t * i)) / (2 * t)
    alist = [a1,a2]
    alist.sort()
    return alist

def cosineLaw(side1,side2,dg,oppositeSide = True):
    if oppositeSide == True:
        v = math.sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * math.cos(toRadians(dg)))
        return v
    elif oppositeSide == False:
        a1 = 1
        b1 = -2 * side1 * math.cos(toRadians(dg))
        c1 = side1 **2 - side2 ** 2
        if b1 ** 2 - 4 * a1 * c1 >= 0:
            y = quadratic(a1,b1,c1)
            x = solution(y)
            return x
        else:
            a1 = 1
            b1 = -2 * side1 * math.cos(toRadians(dg))
            c1 = side2 ** 2 - side1 ** 2
            y = quadratic(a1,b1,c1)
            x = solution(y)
            return x
          
