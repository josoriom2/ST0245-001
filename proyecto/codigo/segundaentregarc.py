import numpy as np
import math
import os
import matplotlib.pyplot as plt
from numpy import loadtxt



cwdpath = os.getcwd()
imagenespath = os.path.join(cwdpath, "imagenes") 
csvpath = os.path.join(cwdpath, "archivos_csv2") 
#se usaron relative paths para hacer mas amena la asignacion de rutas, ya que solo se necesitan los nombres de las carpeta de origen y la de destino
listaarchivos =os.listdir(csvpath)


def comprimir(imagen: np.ndarray , escala : int):
    try:
        if escala == 1:
            comprimida = imagen    #caso en donde la imagen quedaria igual   
        else:
            filas, columnas = imagen.shape
            filascomprimidas, columnascomprimidas = math.ceil(filas/escala), math.ceil(columnas/escala)
            comprimida = np.zeros((filascomprimidas,columnascomprimidas), dtype=int)
            for i in range(0, filas, escala):
                for j in range(0, columnas, escala):
                    comprimida[i//escala,j//escala]=imagen[i,j]
            return comprimida  
    except:
        print("Error")
    
def guardarcsv(pathimagen : str): 
    matrizcsv = loadtxt(str(pathimagen),dtype=int, delimiter=',')
    return matrizcsv #parte de la primera entrega, recorre la carpeta


for imagen in listaarchivos:
#el codigo integra la primera entrega por lo que es capaz de recorrer una carpeta de csv
#e irlos guardando en memoria mientras comprime todos los csv y los guarda nuevamente como imagenes comprimidas en una ruta asignada.

    csvpatharchivo= os.path.join(csvpath, imagen)
    print(csvpatharchivo)
    currentcsv = guardarcsv(csvpatharchivo)
    csvcomprimido = comprimir(currentcsv, 3) 
    imagencomprimida = os.path.join(imagenespath,'Comprimida '+ imagen +'.jpg')
    plt.imsave(imagencomprimida, csvcomprimido, cmap='gray')





