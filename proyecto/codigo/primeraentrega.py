from numpy import loadtxt
import os
matriz=[]
def guardarcsv(imagen,path,directorio): 
    my_data = loadtxt(str(path)+str(imagen),dtype=int, delimiter=',')
    return my_data
path="C:/Users/user/proyectoestructuradedatos/archivos_csv2/"
listaarchivos =os.listdir("C:/Users/user/proyectoestructuradedatos/archivos_csv2/")
cont=1
for imagen in listaarchivos:
    print(guardarcsv(imagen,path,listaarchivos))
    print(cont)
    cont+=1



        