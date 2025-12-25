import math
def multiplicacion(numero1, numero2):
    return numero1 * numero2

multiplicacion = lambda numero1, numero2: numero1 * numero2

resultado = multiplicacion(4,4)

print(resultado)

(lambda numero1, numero2: print(numero1 + numero2)) (7,5)

PI = 3.1416

#Calculator area of circle
circle_area = lambda radio: PI * radio**2
resultado  = round(circle_area(float(input("Enter the radio of the circle: "))), 2)
print(f"The circle area result is: {resultado} cm.")


#One fuction
(lambda name: print(f"Welcome to my python lambda practice {name}.")) ("Andrés")

#Show the position number of the color with lambda fuction
colors = ["rojo","azul","verde","amarillo"]

(lambda color: print(f"The color is at the position {colors.index(color)+1} in the list")) ("verde")
