from numpy import *


def floor(x):
    if not isreal(x):
        print(x, " is not a real number")
        return False
    elif x % 1 == 0:
        return int(x)
    elif x > 0:
        i = 0
        while i < x:
            i = i + 1
        return int(i - 1)
    else:
        i = 0
        while i > x:
            i = i - 1
        return int(i)


def ceiling(x):
    if not isreal(x):
        return print(x, " is not a real number")
    return -floor(-x)


def gcd(x, y):
    if not isreal(x):
        return print(x, " is not a real number")
    elif not isreal(y):
        return print(y, " is not a real number")
    elif x % 1 != 0:
        return print(x, " is not an integer")
    elif y % 1 != 0:
        return print(y, " is not an integer")
    a = min(abs(x), abs(y))
    b = max(abs(x), abs(y))
    if b % a == 0:
        return a
    for i in arange(floor(a/2), 1, -1):
        if b % i == 0:
            return i
    return 1


def lcm(x, y):
    if (type(x) != float) & (type(x) != int):
        return print(x, " is not a real number")
    elif (type(y) != float) & (type(y) != int):
        return print(y, " is not a real number")
    elif (x % 1 != 0) or (y % 1 != 0):
        return print("One or both arguments is not an integer")
    elif (x == 0) or (y == 0):
        return print("Arguments must be non-zero")
    elif x == y:
        return x
    a = min(abs(x), abs(y))
    b = max(abs(x), abs(y))
    n = 1
    while (n * b) % a != 0:
        n = n + 1
    return n * b
 
