from button_act import *
from button import *

from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.config(background="white")
root.geometry('560x400')
root.title('Communism Button')

def cInfo(event=None):
  messagebox.showinfo("Info", "Developed by: @Luckymls @Albe_gss @Zeroandahalf")
def cDonate(event=None):
  showinfo("Donate", "If you enjoyed using this app consider to donate a coffee")
def cExit(event=None):
  if askokcancel("Quit", "Do you really want to quit?"):
    root.destroy()

menu = Menu(root)
root.config(menu=menu)
menu.add_command(label='Info', command=cInfo)
menu.add_command(label='Donate', command=cDonate)
menu.add_command(label='Exit', command=cExit)
