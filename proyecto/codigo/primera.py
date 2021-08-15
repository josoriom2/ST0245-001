import csv
import numpy as np
import os
matriz=[]
def guardarcsv(imagen,path,directorio): 
    muestra = csv.reader(open(str(path)+str(imagen)), delimiter=",")
    x = list(muestra)
    lista = np.array(x).astype("int")
    matriz = lista
    return matriz
path="C:/Users/user/proyectoestructuradedatos/archivos_csv2/"
listaarchivos =os.listdir("C:/Users/user/proyectoestructuradedatos/archivos_csv2/")
for imagen in listaarchivos:
    print(guardarcsv(imagen,path,listaarchivos))



        