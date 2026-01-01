#Join
frase = ["Estoy","aprendiendo","Python","con","el","curso","de","100","días",
         "de","Programación","Fácil."]

print(" ".join(frase))

#Format
colores = ["rojo","azul","verde","amarillo"]
GUION = "-"
PUNTO = "."

for color in colores:
    print( "{}{}{}".format(GUION, color.capitalize(), PUNTO))

#Concatenation with %
numero_1 = 10
numero_2 = 34.50

resultado  = numero_1 * numero_2

print("La multiplicación de %i * %.3f da como resultado: %.3f. "%(numero_1, numero_2, resultado))
print("-------------------------------------------------")

#Found the number of letters in the text by an input
text = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica un gran océano de lenguas"
print(text)
print("")
search = input("Enter a letter to search in text: ")
counter = 0

for letter in text:
    if search == letter:
        counter +=1
    else:
        continue

print(f"The letter {search} has been found {counter} times in the text")
