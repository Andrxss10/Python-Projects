import tkinter as tk

root = tk.Tk()

root.title("Styles in Python with Tkinter")

root.geometry("500x500+50+50")

tk.Label(root, text="Ingresa tu mamada",
         foreground="green").pack()


entrada = tk.Entry(root,
                   background="cyan",
                   border=3,
                   foreground="red",
                   width=30
                   ).pack()


def enviar():
    tk.Label(root, text="Se ha pulsado el botón",
             background="skyblue",
             width=26
             ).pack()

boton = tk.Button(root, text="Enviar", command=enviar,
                  background="deepskyblue",
                  foreground="gray98",
                  border=3,
                  width=25
                  ).pack()

root.mainloop()
