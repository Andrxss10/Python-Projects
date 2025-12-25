import tkinter

#Inicializar programa
root = tkinter.Tk()

#Titulo de la ventana
root.title("Tkinter Program :)")

#Tamaño de la ventana
root.geometry("800x600+420+150")


#Creación de etiquetas
message = tkinter.Label(root, text="My first program with tkinter, first message")
message_2 = tkinter.Label(root, text="This is the second message.")

#Muestra de la etiqueta 
#mensaje.pack()
#mensaje_2.pack()

#Muestra la etiqueta por filas y columnas
message.grid(row=0, column=1)
message_2.grid(row=1, column=0)

"""El método grid crea una tabla de posiciones"""

#Bucle de ejecución para evitar cierre de programa
root.mainloop()
































