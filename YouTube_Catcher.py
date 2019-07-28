 /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy

ventana=Tk()
ventana.geometry("712x490")
ventana.configure(background="navajo white")
ventana.title("DESCARGA DESDE YOUTUBE")
URLL=StringVar()
directorio_actual=StringVar()

def dire_actu():
    directorio_actual.set(os.getcwd())
    

def direc():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
        directorio_actual.set(os.getcwd())

def extrae_audio():
    if URLL.get()!="":
        try:
            v = pafy.new(URLL.get())
            print(v.title)
            try:
                s = v.getbestaudio(preftype="m4a")
            except:
                s = v.getbestaudio()
            s.download()
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
            try:
                s = v.getbest(preftype="mp4")
            except:
                s = v.getbest()
            filename = s.download()
            print(filename)
            messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
        except:
            messagebox.showwarning("ERROR","Se ha producido un error en la descarga")
    else:
        messagebox.showwarning("ERROR","Introduzca URL de video")
dire_actu()
    

Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30).place(x=196,y=130)
Entry(ventana,font=('Arial',8),textvariable=directorio_actual,width=60).place(x=185,y=455)
Label(ventana,width=12,text="DESTINO",bg="navajo white").place(x=314,y=432)
Label(ventana,font=('Arial',30,'bold'),text="YouTube Catcher!",fg="red",bg="navajo white").place(x=193,y=17)
Button(ventana,width=20,text="CAMBIAR DIRECTORIO",bg="pale green",command=direc).place(x=287,y=270)
Button(ventana,width=20,text="DESCARGAR VIDEO",bg="pale green",command=descarga).place(x=287,y=310)
Label(ventana,width=12,text="URL de video",bg="navajo white").place(x=314,y=109)
Button(ventana,width=20,text="EXTRAER AUDIO",bg="pale green",command=extrae_audio).place(x=287,y=350)

ventana.mainloop()

