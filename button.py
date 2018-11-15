pulsantePic = PhotoImage(file='400_ombra.png')

b=Button(root)
b.pack(expand=True)
b.config(image=pulsantePic, command=lambda: changeImage(b))

def changeImage(button=None):

    
    pulsantePic = PhotoImage(file='400_premuto.png')
    button.config(image=pulsantePic)
    onAction()
