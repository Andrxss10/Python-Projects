import tkinter as tk
import os
from PIL import ImageTk, ImageColor, Image

#--Carga de directorios--
#Directorio principal
carpeta_principal = os.path.dirname(__file__)
print(carpeta_principal)

#Acceder al directorio de imagenes
carpeta_imagenes = os.path.join(carpeta_principal, "images")
print(carpeta_imagenes)

#Acceder al directorio de imagenes/paisajes
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")
print(carpeta_paisajes)

#Creación de ventana principal
root = tk.Tk()

#Dimensiones de ventana
root.geometry("350x200+480+250")

#Título de ventana
root.title("Tkinter Program With Python :)")

#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "image-ico.ico"))

#Carga de imagen
imagen_paisaje = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje.jpg")).resize((800,500)))

#Etiqueta para mostrar la imagen
etiqueta = tk.Label(image=imagen_paisaje)

#Mostramos la etiqueta con la imagen
etiqueta.pack()

#Bucle de ejecución permanente de ventana
root.mainloop()
