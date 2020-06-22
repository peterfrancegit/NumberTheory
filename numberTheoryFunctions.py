from numpy import *

def FLOOR(x):
    if (type(x) != float) & (type(x) != int):
        return print(x," is not a real number")
    elif x%1 == 0:
        return x
    elif x > 0:
        i = 0
        while i < x:
            i = i + 1
        return i - 1
    elif x < 0:
        i = 0
        while i > x:
            i = i - 1
        return i
    return

def CEILING(x):
    if (type(x) != float) & (type(x) != int):
        return print(x," is not a real number")
    return -FLOOR(-x)

def GCD(x,y):
    if (type(x) != float) & (type(x) != int):
        return print(x," is not a real number")
    elif (type(y) != float) & (type(y) != int):
        return print(y," is not a real number")
    elif (x%1 != 0) or (y%1 != 0):
        return print("One or both arguments is not an integer")
    elif x == y:
        return x
    a = min(abs(x),abs(y))
    b = max(abs(x),abs(y))
    if b%a == 0:
        return a
    for i in arange(FLOOR(a/2),1,-1):
        if b%i == 0:
            return i
    return 1

def LCM(x,y):
    if (type(x) != float) & (type(x) != int):
        return print(x," is not a real number")
    elif (type(y) != float) & (type(y) != int):
        return print(y," is not a real number")
    elif (x%1 != 0) or (y%1 != 0):
        return print("One or both arguments is not an integer")
    elif (x == 0) or (y == 0):
        return print("Arguments must be non-zero")
    elif x == y:
        return x
    a = min(abs(x),abs(y))
    b = max(abs(x),abs(y))
    n = 1
    while (n * b)%a != 0:
        n = n + 1
    return n * b
 
