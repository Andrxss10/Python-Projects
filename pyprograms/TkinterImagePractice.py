import tkinter as tk
import os
from PIL import ImageTk, ImageColor, Image

#Acceso a ruta/directorio actual
carpeta_principal = os.path.dirname(__file__)
print(carpeta_principal)

#Acceso a carpeta de images
carpeta_images = os.path.join(carpeta_principal, "images")
print(carpeta_images)

#Acceso a carpeta de images/motocicletas
carpeta_motocicletas = os.path.join(carpeta_images, "motocicletas")
print(carpeta_motocicletas)

#Ventana principal
root = tk.Tk()

root.title("Práctica de manejo de imagenes con tkinter y pillow")

root.geometry("800x600+400+130")

root.iconbitmap(os.path.join(carpeta_images, "image-ico.ico"))

#Imagen motocicleta 1
moto_1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_motocicletas, "moto-1.jpg")).resize((396,296)))
label_moto_1 = tk.Label(image=moto_1)
label_moto_1.grid(row=0,column=0)

#Imagen motocicleta 2
moto_2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_motocicletas, "moto-2.jpg")).resize((396,296)))
label_moto_2 = tk.Label(image=moto_2)
label_moto_2.grid(row=0,column=1)

#Imagen motocicleta 3
moto_3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_motocicletas, "moto-3.jpg")).resize((396,296)))
label_moto_3 = tk.Label(image=moto_3)
label_moto_3.grid(row=1,column=0)

#Imagen motocicleta 4
moto_4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_motocicletas, "moto-4.jpg")).resize((396,296)))
label_moto_4 = tk.Label(image=moto_4)
label_moto_4.grid(row=1,column=1)

#Bucle principal
root.mainloop()

