# /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy
import threading
#https://youtu.be/8tQ5YhpGl0Q

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

def verif_url():
    try:
        v = pafy.new(URLL.get())
        print(v.title)
        return v
    except:
        messagebox.showwarning("ERROR","Introduzca URL de video")

def get(c,v):
    if c == "vid":
        try:
            s = v.getbest(preftype="mp4")
        except:
            s = v.getbest()
    else:
        try:
            s = v.getbestaudio(preftype="m4a")
        except:
            s = v.getbestaudio()
    return s

def descargando(co,vid):
    so = get(co,vid)
    try:
        if co == "vid":
            filename = so.download()
        else:
            so.download()
        messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
    except:
        messagebox.showwarning("ERROR","Se ha producido un error en la descarga")
    
def descarga(co):
    vid = verif_url()
    if vid!=None:
        t1 = threading.Thread(target = descargando , args =(co,vid) )
        t1.start()
    
dire_actu()
    
Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30).place(x=196,y=130)
Entry(ventana,font=('Arial',8),textvariable=directorio_actual,width=60).place(x=185,y=455)
Label(ventana,width=12,text="DESTINO",bg="navajo white").place(x=314,y=432)
Label(ventana,font=('Arial',30,'bold'),text="YouTube Catcher!",fg="red",bg="navajo white").place(x=193,y=17)
Button(ventana,width=20,text="CAMBIAR DIRECTORIO",bg="pale green",command=direc).place(x=287,y=270)
Button(ventana,width=20,text="DESCARGAR VIDEO",bg="pale green",command=lambda:descarga("vid")).place(x=287,y=310)
Label(ventana,width=12,text="URL de video",bg="navajo white").place(x=314,y=109)
Button(ventana,width=20,text="EXTRAER AUDIO",bg="pale green",command=lambda:descarga("aud")).place(x=287,y=350)
Label(ventana,width=12,text="PROGRESO",bg="navajo white").place(x=314,y=180)
progressbar = ttk.Progressbar().place(x=196,y=200,width=335)
ventana.mainloop()
