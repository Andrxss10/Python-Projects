import tkinter as tk
root = tk.Tk()

root.title("Widgets con Tkinter")

root.geometry("450x320+520+250")
"""
entrada = tk.Entry(root)

entrada.insert(0, "Escribe cualquier cosa :)....")

#Al pulsar click izquierdo se borra el insert con el mensaje
entrada.bind("<Button-1>", lambda x: entrada.delete(0, tk.END))

#Una alternativa a lo anterior sería con todo el teclado en vez del mouse
#entrada.bind("<Key>", lambda x: entrada.delete(0, tk.END))

entrada.pack()

def pulsar_boton():
    print("Mensaje en Consola :)")

    #Mensaje extraído de la entrada por teclado
    texto = entrada.get()
    tk.Label(root, text=texto).pack()

tk.Button(root, text="Púlsame rápido :O", command=pulsar_boton).pack()
"""
tk.Label(root, text="Nombre").grid(row=0, column=0)
nombre = tk.Entry()
nombre.grid(row=0, column=1)
nombre.insert(0, "Ej: Jack")

nombre.bind("<Button-1>", lambda x: nombre.delete(0, tk.END))

tk.Label(root, text="Edad").grid(row=1, column=0)
edad = tk.Entry()
edad.grid(row=1, column=1)
edad.insert(0, "Ej: 25")
edad.bind("<Button-1>", lambda x: edad.delete(0, tk.END))

def generar_mensaje():
    texto_nombre = nombre.get()
    texto_edad = edad.get()

    tk.Label(root, text=f"Bienvenido {texto_nombre}. Tienes {texto_edad} años.").grid(row=3, column=1)

tk.Button(root, text="Enviar datos", command=generar_mensaje).grid(row=2, column=1)


root.mainloop()
