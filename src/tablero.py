from src.funciones import *
from src.constantes import *

class Tablero:
    def __init__(self):
        self.jugadores = list()
        self.dineroInicial = DINERO_INICIAL
        self.salario = CANTIDAD_SALARIOS[SALARIO_PREDETERMINADO]
        self.netoMaximo = CANTIDAD_NETOS[NETO_PREDETERMINADO]
        self.cantidadJugadores = CANTIDAD_JUGADORES[JUGADORES_PREDETERMINADO]
        self.posicionCasillas = generarPosicionesTablero()

    def cambiarCantidadJugadores(self):
        self.cantidadJugadores = CANTIDAD_JUGADORES[siguienteItem(self.cantidadJugadores, CANTIDAD_JUGADORES)]
        return self.cantidadJugadores
    
    def limpiarJugadores(self): self.jugadores.clear()

    def cambiarSalario(self):
        self.salario = CANTIDAD_SALARIOS[siguienteItem(self.salario, CANTIDAD_SALARIOS)]
        return self.salario
    
    def cambiarNeto(self):
        self.netoMaximo = CANTIDAD_NETOS[siguienteItem(self.netoMaximo, CANTIDAD_NETOS)]
        return self.netoMaximo
    
    def mostrarPosiciones(self):
        return self.posicionCasillas
    
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)