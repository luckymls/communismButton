from tkinter import *

root = Tk()
root.geometry("300x250")                                #Dimensioni finestra
root.title("Communism is here")                             #Titolo finestra
root.resizable(1,1)                             #Rende la finestra resizable
root.iconbitmap(r"C:\Users\alber\Desktop\Immagine.ico")               #Icona

Label(root, text = "URSS")

Text(root).pack



menu = Menu(root)
root.confg(menu = menu)
menu.add_command(label = "File")
