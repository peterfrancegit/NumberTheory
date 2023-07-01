from numberTheoryFunctions import *

run = False
while run is True:
    print("What would you like to do?")
    print("1) Calculate floor of a real number")
    print("2) Calculate ceiling of a real number")
    print("3) Calculate GCD of two integers")
    print("4) Calculate LCM of two integers")
    print("5) Exit")
    print("Choose 1, 2, 3, 4 or 5:")
    num = input()
    if num == "1":
        print("You have chosen floor.")
        print("Enter a real number:")
        x = float(input())
        print("The floor of ", x, " is ", FLOOR(x))
    elif num == "2":
        print("You have chosen ceiling.")
        print("Enter a real number:")
        x = float(input())
        print("The ceiling of ", x," is ", CEILING(x))
    elif num == "3":
        print("You have chosen GCD.")
        print("Enter first integer:")
        x = int(input())
        print("Enter second integer:")
        y = int(input())
        print("The greatest common divisor of ", x, " and ", y, " is ", GCD(x,y))
    elif num == "4":
        print("You have chosen LCM.")
        print("Enter first integer:")
        x = int(input())
        print("Enter second integer:")
        y = int(input())
        print("The lowest common multiple of ", x, " and ", y, " is ", LCM(x,y))
    elif num == "5":
        run = False
    else:
        print("Invalid choice")
            
