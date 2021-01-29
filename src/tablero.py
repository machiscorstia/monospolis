from src.funciones import *

class Tablero:
    def __init__(self):
        self.jugadores = list()
        self.posicionCasillas = generarPosicionesTablero()

    def mostrarPosiciones(self):
        return self.posicionCasillas
    
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)