# Juego del blackjack con interfaz gráfica usando Tkinter

import random
import tkinter as tk

PALOS = ("♠", "♥", "♦", "♣")
VALORES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

ventana = None

mazo = []
mano_jugador = []
mano_crupier = []

partida_terminada = False

fila_cartas_crupier = None
fila_cartas_jugador = None
etiqueta_puntuacion_crupier = None
etiqueta_puntuacion_jugador = None

etiqueta_estado = None
boton_pedir = None
boton_plantarse = None

ventana = tk.Tk()
ventana.title("Blackjack")
ventana.resizable(False, False)
ventana.configure(bg="#075b38")

tk.Label(
    ventana,
    text="BLACKJACK",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#075b38",
).pack(pady=(18, 12))

mesa = tk.Frame(ventana, bg="#087044", padx=24, pady=18)
mesa.pack(padx=18, pady=8)

tk.Label(
    mesa,
    text="CRUPIER",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#087044",
).pack(anchor="w")

etiqueta_puntuacion_crupier = tk.Label(
    mesa, text="", font=("Arial", 11), fg="white", bg="#087044"
)
etiqueta_puntuacion_crupier.pack(anchor="w", pady=(2, 6))

fila_cartas_crupier = tk.Frame(mesa, bg="#087044", height=112)
fila_cartas_crupier.pack(fill="x", pady=(0, 20))

tk.Label(
    mesa,
    text="TU MANO",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#087044",
).pack(anchor="w")

etiqueta_puntuacion_jugador = tk.Label(
    mesa, text="", font=("Arial", 11), fg="white", bg="#087044"
)
etiqueta_puntuacion_jugador.pack(anchor="w", pady=(2, 6))

fila_cartas_jugador = tk.Frame(mesa, bg="#087044", height=112)
fila_cartas_jugador.pack(fill="x")

etiqueta_estado = tk.Label(
    ventana,
    text="",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#075b38",
    width=38,
)
etiqueta_estado.pack(pady=14)

controles = tk.Frame(ventana, bg="#075b38")
controles.pack(pady=(0, 18))

estilo_boton = {
    "font": ("Arial", 11, "bold"),
    "width": 11,
    "bg": "#f0f0f0",
    "activebackground": "#d8d8d8",
}


def robar_carta():
    return mazo.pop()


def valor_mano(mano):
    total = 0
    ases = 0

    for valor, _ in mano:
        if valor == "A":
            total += 11
            ases += 1
        elif valor in ("J", "Q", "K"):
            total += 10
        else:
            total += int(valor)

    while total > 21 and ases:
        total -= 10
        ases -= 1

    return total


def dibujar_carta(contenedor, carta=None, oculta=False):
    if oculta:
        color_fondo = "#173c70"
        color_texto = "white"
        texto_superior = ""
        texto_central = "★"
    else:
        valor, palo = carta
        es_roja = palo in ("♥", "♦")
        color_fondo = "white"
        color_texto = "#c62828" if es_roja else "#202020"
        texto_superior = valor
        texto_central = palo

    carta_marco = tk.Frame(
        contenedor,
        bg=color_fondo,
        width=72,
        height=102,
        relief="raised",
        bd=2,
    )
    carta_marco.pack(side="left", padx=(0, 8))
    carta_marco.pack_propagate(False)

    tk.Label(
        carta_marco,
        text=texto_superior,
        font=("Arial", 13, "bold"),
        fg=color_texto,
        bg=color_fondo,
    ).pack(anchor="nw", padx=6, pady=(4, 0))

    tk.Label(
        carta_marco,
        text=texto_central,
        font=("Arial", 30, "bold"),
        fg=color_texto,
        bg=color_fondo,
    ).place(relx=0.5, rely=0.56, anchor="center")


def actualizar_interfaz(ocultar_crupier=False):
    for elemento in fila_cartas_crupier.winfo_children():
        elemento.destroy()

    for elemento in fila_cartas_jugador.winfo_children():
        elemento.destroy()

    if ocultar_crupier:
        dibujar_carta(fila_cartas_crupier, mano_crupier[0])
        dibujar_carta(fila_cartas_crupier, oculta=True)
        puntuacion_crupier = "Puntuación: ?"
    else:
        for carta in mano_crupier:
            dibujar_carta(fila_cartas_crupier, carta)
        puntuacion_crupier = f"Puntuación: {valor_mano(mano_crupier)}"

    for carta in mano_jugador:
        dibujar_carta(fila_cartas_jugador, carta)

    etiqueta_puntuacion_crupier.config(text=puntuacion_crupier)
    etiqueta_puntuacion_jugador.config(
        text=f"Puntuación: {valor_mano(mano_jugador)}"
    )

    estado_boton = tk.NORMAL if not partida_terminada else tk.DISABLED
    boton_pedir.config(state=estado_boton)
    boton_plantarse.config(state=estado_boton)


def finalizar_ronda():
    global partida_terminada

    partida_terminada = True
    puntuacion_jugador = valor_mano(mano_jugador)
    puntuacion_crupier = valor_mano(mano_crupier)

    blackjack_jugador = len(mano_jugador) == 2 and puntuacion_jugador == 21
    blackjack_crupier = len(mano_crupier) == 2 and puntuacion_crupier == 21

    if puntuacion_jugador > 21:
        resultado = "¡Te pasaste! Gana el crupier."
    elif puntuacion_crupier > 21:
        resultado = "¡El crupier se pasó! Ganaste."
    elif blackjack_jugador and blackjack_crupier:
        resultado = "¡Empate! Ambos tienen blackjack."
    elif blackjack_jugador:
        resultado = "¡Blackjack! Ganaste."
    elif blackjack_crupier:
        resultado = "El crupier tiene blackjack. Gana el crupier."
    elif puntuacion_jugador > puntuacion_crupier:
        resultado = "¡Ganaste!"
    elif puntuacion_jugador < puntuacion_crupier:
        resultado = "Gana el crupier."
    else:
        resultado = "Empate."

    etiqueta_estado.config(text=resultado)
    actualizar_interfaz(ocultar_crupier=False)


def nueva_partida():
    global mazo, mano_jugador, mano_crupier, partida_terminada

    mazo = [(valor, palo) for palo in PALOS for valor in VALORES]
    random.shuffle(mazo)

    mano_jugador = [robar_carta(), robar_carta()]
    mano_crupier = [robar_carta(), robar_carta()]
    partida_terminada = False

    etiqueta_estado.config(text="Tu turno: pide una carta o plántate.")

    if valor_mano(mano_jugador) == 21 or valor_mano(mano_crupier) == 21:
        finalizar_ronda()
    else:
        actualizar_interfaz(ocultar_crupier=True)


def pedir_carta():
    if partida_terminada:
        return

    mano_jugador.append(robar_carta())

    if valor_mano(mano_jugador) >= 21:
        finalizar_ronda()
    else:
        actualizar_interfaz(ocultar_crupier=True)


def plantarse():
    if partida_terminada:
        return

    while valor_mano(mano_crupier) < 17:
        mano_crupier.append(robar_carta())

    finalizar_ronda()

boton_pedir = tk.Button(
    controles, text="Pedir carta", command=pedir_carta, **estilo_boton
)
boton_pedir.pack(side="left", padx=5)

boton_plantarse = tk.Button(
    controles, text="Plantarse", command=plantarse, **estilo_boton
)
boton_plantarse.pack(side="left", padx=5)

tk.Button(
    controles, text="Nueva partida", command=nueva_partida, **estilo_boton
).pack(side="left", padx=5)


def iniciar():
    nueva_partida()
    ventana.mainloop()


if __name__ == "__main__":
    iniciar()