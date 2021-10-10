import numpy as np
import math
import os
import matplotlib.pyplot as plt
from numpy import loadtxt



cwdpath = os.getcwd()
imagenespath = os.path.join(cwdpath, "imagenes") 
csvpath = os.path.join(cwdpath, "archivos_csv2") 

listaarchivos =os.listdir(csvpath)


def comprimir(imagen: np.ndarray , escala : int):
    try:
        if escala == 1:
            comprimida = imagen       
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
    return matrizcsv


for imagen in listaarchivos:

    csvpatharchivo= os.path.join(csvpath, imagen)
    print(csvpatharchivo)
    currentcsv = guardarcsv(csvpatharchivo)
    csvcomprimido = comprimir(currentcsv, 3) 
    imagencomprimida = os.path.join(imagenespath,'Comprimida '+ imagen +'.jpg')
    plt.imsave(imagencomprimida, csvcomprimido, cmap='gray')





