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

#Imagen del login/register
logo_login = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_images, "login.jpg")).resize((200,200)))
label_login = tk.Label(image=logo_login)
label_login.pack()

#Tupla que simula una base de datos para almacenar datos y consultar
usuarios = {}

tk.Label(text="Usuario").pack()
usuario = tk.Entry()
usuario.insert(0, "Ej: andres@gmail.com")
usuario.bind("<Button-1>", lambda x: usuario.delete(0, tk.END))
usuario.pack()

tk.Label(text="Contraseña").pack()
password = tk.Entry()
password.insert(0, "*"*7)
password.bind("<Button-1>", lambda x: password.delete(0, tk.END))
password.pack()

tk.Label(text=" ").pack()

def ingresar():
    user = usuario.get()
    contrasena = password.get()
    if user in usuarios:
        if usuarios[user] == contrasena:
            print("Bienvenido de nuevo !!")
            tk.Label(text="Bienvenido de nuevo :)").pack()
        else:
            print("Usuario o contraseña incorrecta")
            tk.Label(text="Usuario o contraseña incorrecta").pack()
    else:
        usuarios[user] = contrasena
        tk.Label(text="Nuevo usuario creado satisfactoriamente !! :)").pack()
        print("Nuevo usuario creado")

    
tk.Button(text="Ingresar/Registrar", command=ingresar).pack()


#Bucle principal
root.mainloop()

