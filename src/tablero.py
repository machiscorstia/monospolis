from src.funciones import *
from src.constantes import *
from src.interfaz.texto import Texto
from src.ciudad import Ciudad
from random import randrange

class Tablero:
    def __init__(self):
        self.jugadores = list()
        self.ciudades = list()
        self.jugadorMoviendose = None
        self.dineroInicial = DINERO_INICIAL
        self.salario = CANTIDAD_SALARIOS[SALARIO_PREDETERMINADO]
        self.netoMaximo = CANTIDAD_NETOS[NETO_PREDETERMINADO]
        self.cantidadJugadores = CANTIDAD_JUGADORES[JUGADORES_PREDETERMINADO]
        self.posiciones = [generarPosicionesTablero(), generarPosicionCiudades(), generarPosicionPrecios(), generarPosicionPropietario()]
        self.turnoJugador = None
        self.contador = 0

    def establecerTurnoInicial(self): self.jugadorConTurno = self.jugadores[0]

    def mostrarInformacionJugadores(self, pantalla):
        dy= 200
        xn = 110
        for jugador in self.jugadores:
            jugador.mostrarNombre(pantalla, (xn, dy))
            jugador.mostrarDinero(pantalla, (xn*2 - len(jugador.nombre)*4, dy))
            dy += 30
    
    def cambiarCantidadJugadores(self):
        self.cantidadJugadores = CANTIDAD_JUGADORES[siguienteItem(self.cantidadJugadores, CANTIDAD_JUGADORES)]
        return self.cantidadJugadores
    
    def mostrarJugadores(self, pantalla): 
        for jugador in self.jugadores: jugador.mostrar(pantalla)

    def limpiarJugadores(self): self.jugadores.clear()

    def cambiarSalario(self):
        self.salario = CANTIDAD_SALARIOS[siguienteItem(self.salario, CANTIDAD_SALARIOS)]
        return self.salario
    
    def cambiarNeto(self):
        self.netoMaximo = CANTIDAD_NETOS[siguienteItem(self.netoMaximo, CANTIDAD_NETOS)]
        return self.netoMaximo
    
    def tirarDados(self):
        return randrange(6)
    
    def mostrarCiudades(self, pantalla):
        for ciudad in self.ciudades:
            ciudad.mostrarNombre(pantalla)
            ciudad.mostrarPropietario(pantalla)
            ciudad.mostrarPrecio(pantalla)
    
    def mostrarPosiciones(self):
        return self.posiciones[0]
    
    def mover(self):
        if self.contador +1 == len(self.posiciones[0]): self.contador = 0
        else: self.contador += 1
        self.jugadores[0].establecerPosicion(self.posiciones[0][self.contador])

    def establecerCiudades(self):
        for i in CIUDADES:
            if verificarExistencia(i, [0, 7, 14, 21]): continue
            self.agregarCiudad(
                Ciudad(
                    CIUDADES[i][0], CIUDADES[i][1],
                    posicionNombre = self.posiciones[POSICION_NOMBRE_CIUDAD][i], 
                    posicionPrecio = self.posiciones[POSICION_PRECIO_CIUDAD][i],
                    posicionPropietario = self.posiciones[POSICION_PROP_CIUDAD][i]
                )
            )
    
    def agregarCiudad(self, ciudad):
        self.ciudades.append(ciudad)
    
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
        jugador.establecerPosicion(self.posiciones[0][0])