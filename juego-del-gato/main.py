import numpy as np


def ImprimirTablero(tablero: np.ndarray) -> None:
    ren, _ = tablero.shape
    for i in range(ren):
        print(" | ".join(tablero[i, :]))
        if i < ren - 1:
            print("--|--|--")
    print()


def HayGanador(tablero: np.ndarray, turno: str) -> bool:
    ren, col = tablero.shape

    for i in range(ren):
        if np.all(tablero[i, :] == turno):
            return True

    for i in range(col):
        if np.all(tablero[:, i] == turno):
            return True

    if np.all(np.diag(tablero) == turno):
        return True

    if np.all(np.diag(np.fliplr(tablero)) == turno):
        return True

    return False


def ObtenerPosicion(tablero: np.ndarray) -> tuple[int, int]:
    while True:
        try:
            pos = int(input("Dónde quieres colocar tu ficha (1-9): "))
            if pos < 1 or pos > 9:
                print("Error: debe ser un número del 1 al 9")
                continue

            ren = (pos - 1) // 3
            col = (pos - 1) % 3

            if tablero[ren, col] != str(pos):
                print("Error: casilla ocupada")
                continue

            return (ren, col)
        except ValueError:
            print("Error: se espera un número entero")


if __name__ == "__main__":
    tablero = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], dtype=str)

    ImprimirTablero(tablero)
    turno = "X"
    casillasOcupadas = 0

    while True:
        print(f"Turno: {turno}")
        ren, col = ObtenerPosicion(tablero)

        tablero[ren, col] = turno
        casillasOcupadas += 1

        ImprimirTablero(tablero)

        if HayGanador(tablero, turno):
            print(f"Ganó: {turno}")
            break
        if casillasOcupadas == 9:
            print("Gano el gato")
            break

        turno = "O" if turno == "X" else "X"