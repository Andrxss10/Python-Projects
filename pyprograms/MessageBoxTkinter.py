import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()

root.title("Message Box in python with tkinter :)")

root.geometry("500x500+400+50")

#Función para mensaje informativo
def show_info():
    msgbox.showinfo("Mensaje informativo",
                "Esta es una caja de mensaje emergente informativa!")

def show_warning():
    msgbox.showwarning("Mensaje de advertencia",
                "Esta es una caja de mensaje emergente de advertencia!")

def show_error():
    msgbox.showerror("Mensaje de ERROR",
                "Esta es una caja de mensaje emergente de error!")

def ask_question():
    msgbox.askquestion("¿Sabías que?",
                "El Barcelona es el primer equipo en la historia en ganar un sextete")

def ask_okorcancel():
    msgbox.askokcancel("¿Seguro deseas continuar?",
                "La acción que va a ejecutar puede realizar cambios permanentes en su PC.")

def ask_yesnocancel():
    msgbox.askyesnocancel("¿Deseas continuar?",
                "La acción que va a ejecutar puede realizar cambios permanentes en su DB.")

def ask_retryorcancel():
    msgbox.askretrycancel("Ejecución fallida",
                          "¿La acción no pudo completarse, desea intentarlo de nuevo?")

button_info = tk.Button(root, text="Informative Message", command=show_info, width=35).pack()
button_warning = tk.Button(root, text="Warning Message", command=show_warning, width=35).pack()
button_error = tk.Button(root, text="Error Message", command=show_error, width=35).pack()
button_question = tk.Button(root, text="Question", command=ask_question, width=35).pack()
button_okorcancel = tk.Button(root, text="Ok or Cancel", command=ask_okorcancel, width=35).pack()
button_yesnocancel = tk.Button(root, text="Yes, no or cancel", command=ask_yesnocancel, width=35).pack()
button_retryorcancel = tk.Button(root, text="Retry or cancel", command=ask_retryorcancel, width=35).pack()

root.mainloop()
