import numpy as np

arreglo = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

print(arreglo)

fila = int(input("Introduce la fila: "))
columna = int(input("Introduce la columna: "))

arreglo[fila, columna] = 1
arreglo[fila - 1, columna] = 1
arreglo[fila + 1, columna] = 1
arreglo[fila, columna - 1] = 1
arreglo[fila, columna + 1] = 1
arreglo[fila - 1, columna - 1] = 1
arreglo[fila - 1, columna + 1] = 1
arreglo[fila + 1, columna - 1] = 1
arreglo[fila + 1, columna + 1] = 1

print(arreglo)