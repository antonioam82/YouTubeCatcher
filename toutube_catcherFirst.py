import pafy
import os

def direct():
    while True:
        dire = input("Introduce directorio: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        print("DIRECTORIO DESCONOCIDO")


def validate_url():
    while True:
        URL_video=input("Introduce URL de video: ")
        try:
            v = pafy.new(URL_video)
            print(v.title)
            break
        except:
            print("INTRODUCE URL DE VIDEO VÁLIDA")
    return v
    
def descarga(vi):
    try:
        s=vi.getbest()
        filename=s.download()
    except:
        print("HUBO UN PROBLEMA AL EFECTUAR LA DESCARGA")


pregunta_direc=ns(input("¿Desea cambiar el directorio actual?: "))
if pregunta_direc=="s":
    direc()
vid=validate_url()
descarga(vid)
