import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()

root.title("Exercise with radio buttons and images with pillow")

root.configure(background="gray80")
#root.geometry("408x460+400+100")

main_folder = os.path.dirname(__file__) 

images_folder = os.path.join(main_folder, "images")

users_folder = os.path.join(images_folder, "users")

buttons_folder = os.path.join(images_folder, "buttons")

#Marco general
marco_general = tk.LabelFrame(root,
                              text=" Select a user: ",
                              padx=10, pady=10,
                              background="MediumPurple3",
                              border=0 #para quitar el margen del marco
                              )
marco_general.pack(padx=10, pady=10)

#Imagenes para cada perfil
user_1 = ImageTk.PhotoImage(Image.open(os.path.join(users_folder, "user1.jpg")).resize((200,200)))
tk.Label(marco_general, image=user_1, background="MediumPurple3").grid(row=0, column=0)

user_2 = ImageTk.PhotoImage(Image.open(os.path.join(users_folder, "user2.jpg")).resize((200,200)))
tk.Label(marco_general, image=user_2, background="MediumPurple3").grid(row=0, column=1)

user_3 = ImageTk.PhotoImage(Image.open(os.path.join(users_folder, "user2.jpg")).resize((200,200)))
tk.Label(marco_general, image=user_3, background="MediumPurple3").grid(row=2, column=0)

user_4 = ImageTk.PhotoImage(Image.open(os.path.join(users_folder, "user1.jpg")).resize((200,200)))
tk.Label(marco_general, image=user_4, background="MediumPurple3").grid(row=2, column=1)

#Imagen del botón
button_image = ImageTk.PhotoImage(Image.open(os.path.join(buttons_folder, "button.png")))

#Botones de radio por cada perfil
option = tk.StringVar(None)
option.set("Error")
tk.Radiobutton(marco_general, text="Jacob",
               variable=option,
               value="Jacob",
               background="skyblue").grid(row=1, column=0)
tk.Radiobutton(marco_general, text="Emma",
               variable=option,
               value="Emma",
               background="yellow").grid(row=1, column=1)
tk.Radiobutton(marco_general, text="Sophia",
               variable=option,
               value="Sophia",
               background="yellow").grid(row=3, column=0)
tk.Radiobutton(marco_general, text="Noah",
               variable=option,
               value="Noah",
               background="skyblue").grid(row=3, column=1)

def saludo_user():
    if option.get() == "Error":
        tk.Label(root, text="!No has seleccionado ninguna cuenta! Por favor, inténtelo de nuevo.",
                 background="gray98",
                 foreground="red2").pack()
    else:
        tk.Label(root, text=f"Hola {option.get()}, Accediendo a tu cuenta personal....").pack()

send_button = tk.Button(root, text="Enter",
                        command=saludo_user,
                        image=button_image,
                        border=None, # 0 para evitar que tenga borde
                        background="gray98" #gray80 para quitar borde
                        ).pack(pady=10)

root.mainloop()









