from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy

ventana=Tk()
ventana.geometry("700x480")
ventana.configure(background="navajo white")
ventana.title("DESCARGA DESDE YOUTUBE")
URLL=StringVar()

def direc():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)

def descarga():
    print(URLL.get())
    v = pafy.new(URLL.get())
    print(v.title)
    s = v.getbest()
    try:
        filename = s.download()
        messagebox.showinfo("FIN DE DESCARGA","Descarga finalizada con éxito")
    except:
        messagebox.showwarning("ERROR","Se ha iterrumpido la descarga")
    

Entry(ventana,font=('Arial',15,'bold'),textvariable=URLL,width=30).place(x=196,y=130)
Button(ventana,width=20,text="DIRECTORIO",bg="pale green",command=direc).place(x=287,y=270)
Button(ventana,width=20,text="DESCARGA",bg="pale green",command=descarga).place(x=287,y=310)

ventana.mainloop()
