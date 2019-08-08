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
total_size=0
dif=0

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
        entrada.delete(0,len(URLL.get()))
    
def get(c,v):
    global total_size
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
    total_size=s.get_filesize()
    return s

def estado(s):
    boton_dire.config(state = s)
    boton_descarga.config(state = s)
    boton_audio.config(state = s)
        
def mycb(total,recvd,ratio,rate,eta):
    global dif
    porcen=((recvd*100)/total_size)
    #avance=porcen-dif
    prog.step(porcen-dif)
    dif=porcen
    print(recvd)

def descargando(co,vid):
    global dif
    so = get(co,vid)
    try:
        so.download(quiet=True,callback=mycb)
        messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
        
    except:
        messagebox.showwarning("ERROR","Se ha producido un error en la descarga")
    estado('normal')
    dif=0
    
def descarga(co):
    vid = verif_url()
    if vid!=None:
        estado('disabled')
        t1 = threading.Thread(target = descargando , args =(co,vid) )
        t1.start()
        
dire_actu()
    
entrada=Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30)
entrada.place(x=196,y=130)
entrada2=Entry(ventana,font=('Arial',8),textvariable=directorio_actual,width=60)
entrada2.place(x=185,y=455)
Label(ventana,width=12,text="DESTINO",bg="navajo white").place(x=314,y=432)
Label(ventana,font=('Arial',30,'bold'),text="YouTube Catcher!",fg="red",bg="navajo white").place(x=193,y=17)
boton_dire=Button(ventana,width=20,text="CAMBIAR DIRECTORIO",bg="pale green",command=direc)
boton_dire.place(x=287,y=270)
boton_descarga=Button(ventana,width=20,text="DESCARGAR VIDEO",bg="pale green",command=lambda:descarga("vid"))
boton_descarga.place(x=287,y=310)
Label(ventana,width=12,text="URL de video",bg="navajo white").place(x=316,y=109)
boton_audio=Button(ventana,width=20,text="EXTRAER AUDIO",bg="pale green",command=lambda:descarga("aud"))
boton_audio.place(x=287,y=350)
Label(ventana,width=12,text="PROGRESO",bg="navajo white").place(x=316,y=180)
prog=progressbar = ttk.Progressbar(ventana)
prog.place(x=196,y=200,width=335)

ventana.mainloop()


