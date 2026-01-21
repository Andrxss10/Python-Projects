import tkinter as tk

root = tk.Tk()

root.title("Frames in Python with Tkinter")

root.geometry("500x500+50+50")

marco_entry = tk.LabelFrame(root, text="Entrada de datos", padx=15, pady=15)
marco_entry.pack(padx=15, pady=15)

marco_button = tk.LabelFrame(root, text="Enviar", padx=15, pady=15)
marco_button.pack(padx=5, pady=15)

marco_result = tk.LabelFrame(root, text="Resultado", padx=15, pady=15)
marco_result.pack(padx=5, pady=15)

#No se inicia en root si no directamente en marco
entrada = tk.Entry(marco_entry,
                   background="cyan",
                   border=3,
                   foreground="red",
                   width=30
                   ).pack()


def enviar():
    tk.Label(marco_result, text="Se ha pulsado el botón",
             background="skyblue",
             width=26
             ).pack()

boton = tk.Button(marco_button, text="Enviar", command=enviar,
                  background="deepskyblue",
                  foreground="gray98",
                  border=3,
                  width=25
                  ).pack()


root.mainloop()
