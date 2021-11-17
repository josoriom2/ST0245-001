import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
from collections import deque
import time
import os
import math
import pandas as pd
from numpy import genfromtxt

#JERONIMO OSORIO M
#JORGE VILLAREAL 
#FUNCIONES AUXILIARES
def aLista(path):
    image = loadtxt(str(path),dtype=int, delimiter=',')
    nFilas, nColumnas = image.shape
    lista = []
    for i in range(nFilas):
        for j in range(nColumnas):
            lista.append(image[i][j])
    return lista

def MedirTiempo(funcion):
    def Medir(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return Medir

def findMatch(lista, i, TamanoVentanaAdelante, TamanoVentanaContenidos):
    FinalBuffer = min(i + TamanoVentanaAdelante, len(lista) + 1)

    Distancia = -1
    Longitud = -1

    for j in range(i, FinalBuffer):
        startIndex = max(0, i - TamanoVentanaContenidos)
        subList = lista[i:j+1]
        for m in range(startIndex, i):
            repeticiones = len(subList)//(i-m)
            last = len(subList)%(i-m)

            matchedList = lista[m:i] * repeticiones + lista[m:m+last]

            if matchedList == subList and len(subList)>Longitud:
                Distancia = i - m
                Longitud = len(subList)
    if Distancia > 0 and Longitud > 0:
        return (Distancia, Longitud)
    return None


def resize(Nfilas,Mcolumnas,lista):
    if(Nfilas*Mcolumnas)!=len(lista):
        lista.pop()
        matriz=np.array(lista).reshape(Nfilas,Mcolumnas)
        return matriz
        
    matriz=np.array(lista).reshape(Nfilas,Mcolumnas)
    return matriz


def to_csv(matriz,imagen,path):
    df = pd.DataFrame(matriz)
    df.to_csv(os.path.join(path,"Lz77 "+imagen))
    
    
def guardarcsv(pathimagen): 
    matrizcsv = np.genfromtxt(str(pathimagen),dtype=int, delimiter=',')[:,:-1]
    return matrizcsv #parte de la primera entrega, recorre la carpeta


def guardarImagen(pathO,pathL):
    listalz77 =os.listdir(pathO)
    for imagen in listalz77:
        csvpatharchivo= os.path.join(pathO, imagen)
        csvTemp=guardarcsv(csvpatharchivo)
        imagenescomprimidas = os.path.join(pathL,"("+imagen+")"+".jpg")
        plt.imsave(imagenescomprimidas, csvTemp, cmap='gray')


#FUNCIONES PRINCIPALES
def comprimirLZ77(lista,n,m):
    TamanoVentanaContenidos = n # tamano del buffer que contiene una porcion de la secuencia codificada recientemente
    TamanoVentanaAdelante = m  # tamano del buffer que contiene la proxima porciona a ser codificada
    i = 0
    listaN = []
    while i < len(lista):
        match = findMatch(lista, i, TamanoVentanaAdelante, TamanoVentanaContenidos)
        if match:
            Distancia, Longitud = match
            Diferencia = min(i+Longitud, len(lista)-1)
            listaN.append("<" + str(Distancia) + "," + str(Longitud) + "," + str(lista[Diferencia]) + ">")
            i = i + Longitud+1
        else:
            listaN.append('<0,0,' + str(lista[i]) + '>')
            i = i + 1
    return listaN



    
def descomprimir(ListaComprimida):
    ListaDescomprimida = []
    i = 0
    while i < len(ListaComprimida):
        decompressing = ListaComprimida[i]
        firstComma = decompressing.index(',')
        secondComma = decompressing.index(',', firstComma + 1)
        if ListaComprimida[i][1:firstComma] == '0':
            ListaDescomprimida.append(ListaComprimida[i][secondComma+1:decompressing.index('>')])
            i = i + 1
        else:
            if ListaComprimida[i][firstComma+1:secondComma] == '1':
                number = ListaDescomprimida[-(int(ListaComprimida[i][1:firstComma]))]
                ListaDescomprimida.append(number)
                ListaDescomprimida.append(ListaComprimida[i][secondComma+1:decompressing.index('>')])
                i = i + 1
            else:
                aApenear = []
                f = -(int(ListaComprimida[i][1:firstComma]))
                m = int(ListaComprimida[i][firstComma+1:secondComma])
                if abs(f) > m:
                    while m > 0:
                        aApenear.append(ListaDescomprimida[f])
                        f = f + 1
                        m = m - 1
                    for item in aApenear:
                        ListaDescomprimida.append(item)
                    ListaDescomprimida.append(ListaComprimida[i][secondComma+1:decompressing.index('>')])
                    i = i + 1
                else:
                    save = m - int(ListaComprimida[i][1:firstComma])
                    m = int(ListaComprimida[i][1:firstComma])
                    while m > 0:
                        aApenear.append(ListaDescomprimida[f])
                        f = f + 1
                        m = m - 1
                    for item in aApenear:
                        ListaDescomprimida.append(item)
                    while save > 0:
                        ListaDescomprimida.append(ListaDescomprimida[-1])
                        save = save - 1
                    ListaDescomprimida.append(ListaComprimida[i][secondComma+1:decompressing.index('>')])
                    i = i + 1
    return ListaDescomprimida



#RUTAS

cwdpath= os.getcwd()
imagenesLz77=os.path.join(cwdpath,"ImagenesJPGlz77")
csvlz77comprimidospath=os.path.join(cwdpath, "LZ77Comprimidos") 
csvlz77path = os.path.join(cwdpath, "CSVsLZ77Descomprimidas") 
csvpath = os.path.join(cwdpath, "ARCHIVOSCVSORIGINALES") 
#se usaron relative paths para hacer mas amena la asignacion de rutas, ya que solo se necesitan los nombres de las carpeta de origen y la de destino
listaarchivos =os.listdir(csvpath)


        
    

def main():
    
    for imagen in listaarchivos:
        
        csvpatharchivo= os.path.join(csvpath, imagen)
        
        lista = aLista(csvpatharchivo)
        
        #""" decidimos hacerlo aqui en vez de un metodo para evitar inconvenientes
        
        image = loadtxt(str(csvpatharchivo),dtype=int, delimiter=',')
        nFilas, mCol = image.shape
        #""""
        
        imagencomprimida = comprimirLZ77(lista,5,10)
        
        imagendescomprimida = descomprimir(imagencomprimida)
        
        matrizdescomprimida=resize(nFilas,mCol,imagendescomprimida)
        #guardamos los csv comprimidos con lz77 
        
        to_csv(imagendescomprimida,imagen,csvlz77comprimidospath)
        
        #guardamos los csv descomprimidos con lz77
        
        to_csv(matrizdescomprimida,imagen,csvlz77path)
        
        #convertimos y guardamos en imagenes
        guardarImagen(csvlz77path,imagenesLz77)
        
    
main()