from pygame import mixer

from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.config(background="white")
root.geometry('400x400')
root.title('Communism Button')
root.iconbitmap('icon.ico')

global pulsantePicPremuto
pulsantePic = PhotoImage(file='400_ombra.png')
pulsantePicPremuto = PhotoImage(file='400_premuto.png')
b=Button(root)
b.pack(expand=True)
b.config(image=pulsantePic, command=lambda: changeImage(button=b))

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



statoBottone = IntVar()


def onAction (event=None):


                              # Richiano funzione con file in riproduzione
    if statoBottone.get():  # Se il bottone è attivo
        statoBottone.set(0) # Il bottone è stato usato
        innoStop()          # Ferma il brano
    else:
        statoBottone.set(1)
        innoStart()
    
def innoStart (): # Richiamo file
    mixer.init()
    mixer.music.load('soviet-anthem1977.mp3')
    mixer.music.play(start=1.5)

def innoStop ():
    mixer.init()
    mixer.music.stop()





def changeImage(event=None, button=None):

    global pulsantePicPremuto

    if statoBottone.get() == 0:
      button.config(image=pulsantePicPremuto)

    else:
      button.config(image=pulsantePic)
    onAction() 

b.bind_all("<Any-KeyPress>", lambda x: changeImage('',button=b))
