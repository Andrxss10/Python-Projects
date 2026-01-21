# Módulo de division
def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:  
        print("No se puede dividir entre 0")
