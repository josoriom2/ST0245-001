import csv
import numpy as np

class LectorPrimera():
    
    def __init__(self):##setter
        self.matrix = []
        
    def matrix(self): ##getter
        return self.matrix
        
    def guardarcsv(self, nombre):
        try:
            muestra = csv.reader(open(nombre), delimiter=",")
            x = list(muestra)
            lista = np.array(x).astype("int")
            self.matrix = lista
            return self.matrix
        except:
            print("Nombre equivocado")

class principal():
    csvarchivo = 'prueba.csv'
    imagen = LectorPrimera()
    imagen.guardarcsv(csvarchivo)
    print(imagen.matrix)