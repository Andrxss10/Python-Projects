def dicctionary():
    #DICCTIONARY
    inventario = {
        #KEY: VALUE
        1: "Espada",
        2: "escudo",
        3: "Poción de regeneración",
        4: "Libro de encantamientos"
        }

    #Print Dicctionary
    print(f"Normal dicctioanry: {inventario}")
    #Print a value by key
    print(f"Value: {inventario[4]} represent key 4.")

    #Add new key and value
    inventario[5] = "Casco"
    inventario["Test"] = 6

    print(f"New elements in dicctionary: {inventario}")

    #Modify an element in dicctionary
    inventario["Test"] = "Comida"

    print(f"Modify Dicctionary: {inventario}")

    print("Keys:")
    #Iteration of keys in dicctionary with for:
    for element in inventario:
        print(f"-{element}")

    #Iteration of values in dicctionary with for:
    print("Values:")
    for element in inventario:
        print(f"-{inventario[element]}")

#dicctionary()

def sets():

    #Create set like dicctionary, but it hasn't keys, only values:
    animals = {"dog","cat","bear","lion"}

    #Print set, his order change by execution
    print(animals)

    #It can't repeat values like lists:
    animals = {"dog","cat","dog","cat","lion","cat"}
    print(animals)
sets()













    
