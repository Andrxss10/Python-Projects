from operations.suma import *
from operations.resta import *
from operations.multiplicacion import *
from operations.division import *
from operations.potencia import *
print("Basic Calculator with Functions")

while True:
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")
    print("5. PONTENCIACIÓN")
    print("0. EXIT")

    option = int(input("Enter the operation you want"))

    match option:
        case 1:
            a = float(input("Enter the number 1: "))
            b = float(input("Enter the number 2: "))
            result = suma(a,b)
            print(f"The result of operation: {a} + {b} = {result}")
        case 2:
            a = float(input("Enter the number 1: "))
            b = float(input("Enter the number 2: "))
            result = resta(a,b)
            print(f"The result of operation: {a} - {b} = {result}")
        case 3:
            a = float(input("Enter the number 1: "))
            b = float(input("Enter the number 2: "))
            result = multiplicacion(a,b)
            print(f"The result of operation: {a} * {b} = {result}")
        case 4:
            a = float(input("Enter the number 1: "))
            b = float(input("Enter the number 2: "))
            result = division(a,b)
            print(f"The result of operation: {a} / {b} = {result}")
        case 5:
            a = float(input("Enter the number 1: "))
            b = float(input("Enter the number 2: "))
            result = potencia(a,b)
            print(f"The result of operation: {a} ** {b} = {result}")
        case 0:
            print("See you later !! ...")
            break
        case default:
            print("Enter a valid option please (0-5)")
