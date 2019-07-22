#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy

#https://youtu.be/uQ9nsr9YoCQ

ventana=Tk()
ventana.geometry("700x480")
ventana.configure(background="navajo white")
ventana.title("DESCARGA DESDE YOUTUBE")
URLL=StringVar()

def direc():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)

def extrae_audio():
    if URLL.get()!="":
        try:
            v = pafy.new(URLL.get())
            print(v.title)
            s = v.getbestaudio()
            s.download()
            print(filename)
            messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
        except:
            messagebox.showwarning("ERROR","Se he producido un error en la descarga")
    else:
        messagebox.showwarning("ERROR","Introduzca URL de video")
    

def descarga():
    if URLL.get()!="":
        try:
            v = pafy.new(URLL.get())
            print(v.title)
            s = v.getbest()
            filename = s.download()
            print(filename)
            messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
        except:
            messagebox.showwarning("ERROR","Se ha producido un error en la descarga")
    else:
        messagebox.showwarning("ERROR","Introduzca URL de video")
    

Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30).place(x=196,y=130)
Button(ventana,width=20,text="CAMBIAR DIRECTORIO",bg="pale green",command=direc).place(x=287,y=270)
Button(ventana,width=20,text="DESCARGAR VIDEO",bg="pale green",command=descarga).place(x=287,y=310)
Label(ventana,width=12,text="URL de video",bg="navajo white").place(x=314,y=109)
Button(ventana,width=20,text="EXTRAER AUDIO",bg="pale green",command=extrae_audio).place(x=287,y=350)
ventana.mainloop()
