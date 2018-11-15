from pygame import mixer
from tkinter import *

root = Tk()
statoBottone = IntVar()


def onAction (event=None): # Richiano funzione con file in riproduzione
    if statoBottone.get(): # Se il bottone è attivo
        statoBottone.set(0) # Il bottone è stato usato
        innoStop()
    else:
        statoBottone.set(1)
        innoStart()
    
def innoStart (): # Richiamo file
    mixer.init()
    mixer.music.load('C:/Users/Luca Corona/Downloads/soviet-anthem1944.mp3')
    mixer.music.play()

def innoStop ():
    mixer.init()
    mixer.music.stop()
