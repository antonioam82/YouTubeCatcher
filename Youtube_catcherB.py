# /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy

#https://youtu.be/bAmPr2B1kmo

ventana=Tk()
ventana.geometry("712x490")
ventana.configure(background="navajo white")
ventana.title("DESCARGA DESDE YOUTUBE")
URLL=StringVar()
directorio_actual=StringVar()
titulo_video=StringVar()
v=""

def dire_actu():
    directorio_actual.set(os.getcwd())
    

def direc():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
        directorio_actual.set(os.getcwd())

def carga():
    global v
    if URLL.get()!="":
        try:
            v = pafy.new(URLL.get())
            titulo_video.set(v.title)
        except:
            messagebox.showwarning("ERROR","URL no válida")

def extrae_audio():
    if URLL.get()!="":
        try:
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
            s = v.getbest()
            filename = s.download()
            print(filename)
            messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
        except:
            messagebox.showwarning("ERROR","Se ha producido un error en la descarga")
    else:
        messagebox.showwarning("ERROR","Introduzca URL de video")
dire_actu()
    
Entry(ventana,font=('Arial',15,'bold'),textvariable=titulo_video,width=30).place(x=196,y=148)
Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30).place(x=196,y=94)
Entry(ventana,font=('Arial',8),textvariable=directorio_actual,width=60).place(x=185,y=455)
Button(ventana,width=20,text="DESCARGAR VIDEO",bg="pale green",command=descarga).place(x=287,y=310)
Button(ventana,width=20,text="CARGAR VIDEO",bg="pale green",command=carga).place(x=287,y=180)
Label(ventana,width=12,text="DESTINO",bg="navajo white").place(x=314,y=432)
Label(ventana,width=12,text="TITULO VIDEO",bg="navajo white").place(x=314,y=127)
Button(ventana,width=20,text="CAMBIAR DIRECTORIO",bg="pale green",command=direc).place(x=287,y=270)
Label(ventana,width=12,text="URL de video",bg="navajo white").place(x=314,y=70)
Button(ventana,width=20,text="EXTRAER AUDIO",bg="pale green",command=extrae_audio).place(x=287,y=350)

ventana.mainloop()
