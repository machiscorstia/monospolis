from src.funciones import *

class Tablero:
    def __init__(self):
        self.jugadores = list()
        self.posicionCasillas = generarPosicionesTablero()

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)