from distutils.cmd import Command
from tkinter import *
import pyfirmata
root = Tk()

puerto = "\\.\COM4"
led=(13)
led2=(11)
boton=(2)

tarjeta = pyfirmata.Arduino(puerto)

def clinado():
    tarjeta.digital[led].write(1)
    tarjeta.pass_time(10)
    tarjeta.digital[led].write(0)

boton = Button(root,text="on", command=clinado)
boton.pack()
root.geometry("150x80")
root.mainloop()




