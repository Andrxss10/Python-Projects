import tkinter as tk

root = tk.Tk()

root.title("RadioButton and control variables")

root.geometry("500x500+250+50")

option = tk.StringVar()
option.set(None)

#Función para el botón de envío
def update_radio(value):
    tk.Label(root, text=value).pack()
    

tk.Radiobutton(root,
               text="Red",
               variable=option,
               value="rojo"
               ).pack()
tk.Radiobutton(root,
               text="Yellow",
               variable=option,
               value="amarillo"
               ).pack()
tk.Radiobutton(root,
               text="Black",
               variable=option,
               value="negro"
               ).pack()
tk.Radiobutton(root,
               text="White",
               variable=option,
               value="blanco"
               ).pack()

send_button = tk.Button(root, text="Send",
                        command=lambda:update_radio(option.get())).pack()

root.mainloop()












