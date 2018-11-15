from tkinter import *

root = Tk()
root.geometry("400x400")

statoPulsante = IntVar()


Pulsante = PhotoImage(file=r"C:\Users\alber\Desktop\400_ombra.png")

b=Button(root)
b.pack(expand=True)
b.config(image=Pulsante, command=lambda: changeImage(b))

def changeImage(button=None):

    
    pulsantePic = PhotoImage(file=r"C:\Users\alber\Desktop\400_premuto.png")
    button.config(image=pulsantePic)
    # onAction()
