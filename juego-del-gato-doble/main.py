import tkinter as tk
import numpy as np

arreglo = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

for index, value in enumerate(arreglo):
    print(arreglo[index])

renglon = int(input("Introduce renglon: "))
columna = int(input("Introduce columna: "))

# cambiar ese valor por 1

arreglo[renglon][columna] = 1

for index, value in enumerate(arreglo):
    print(arreglo[index])


"""if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Gato Ultimate")
    ventana.resizable(False, False)

    canvas = tk.Canvas(ventana, width=500, height=500, bg="white")
    canvas.grid()

    ventana.mainloop()"""