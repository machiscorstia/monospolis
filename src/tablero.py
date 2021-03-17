from src.funciones import *
from src.constantes import *
from src.interfaz.texto import Texto
from src.interfaz.boton import Boton
from src.ciudad import Ciudad
from random import randrange

class Tablero:
    def __init__(self):
        self.jugadores = list()
        self.ciudades = list()
        self.jugadorMoviendose = False
        self.jugadorComprando = False
        self.dineroInicial = DINERO_INICIAL
        self.salario = CANTIDAD_SALARIOS[SALARIO_PREDETERMINADO]
        self.netoMaximo = CANTIDAD_NETOS[NETO_PREDETERMINADO]
        self.cantidadJugadores = CANTIDAD_JUGADORES[JUGADORES_PREDETERMINADO]
        self.posiciones = [generarPosicionesTablero(), generarPosicionCiudades(), generarPosicionPrecios(), generarPosicionPropietario()]
        self.jugadorConTurno = False
        self.contador = 0

    def establecerTurnoInicial(self): self.jugadorConTurno = self.jugadores[0]

    def actualizarJugadorConTurno(self):
        self.jugadorConTurno = self.jugadores[siguienteItem(self.jugadorConTurno, self.jugadores)]
    
    def empezarMovimiento(self, casillas):
        casillas += 1
        self.jugadorMoviendose = True
        #self.jugadorConTurno.numeroCasilla += casillas + 1
        if self.jugadorConTurno.casilla + casillas > 27: 
            self.jugadorConTurno.casillaFinal = (self.jugadorConTurno.casilla + casillas) - len(self.posiciones[POSICION_CASILLA])
            print(self.jugadorConTurno.casillaFinal)
        else: self.jugadorConTurno.casillaFinal = self.jugadorConTurno.casilla + casillas
        #self.jugadorConTurno.establecerPosicionFinal(self.posiciones[POSICION_CASILLA][self.jugadorConTurno.numeroCasilla])
        #self.actualizarJugadorConTurno()
    
    def obtenerCiudadActual(self): return self.obtenerCiudadPorCasilla(self.jugadorConTurno.casilla)
    
    def chequearJugadoresEnCasilla(self, casilla):
        if self.obtenerJugadoresEnCasilla(casilla) > 1: # si hay mas jugadores en la casilla
            x, y = self.jugadorConTurno.posicion
            self.jugadorConTurno.establecerPosicion((x + self.obtenerJugadoresEnCasilla(self.jugadorConTurno.casilla) * 5, y))
        
    def terminarMovimiento(self):
        self.chequearJugadoresEnCasilla(self.jugadorConTurno.casilla)
        self.jugadorMoviendose = False
        #self.actualizarJugadorConTurno()
        if not self.obtenerCiudadActual().propietario: self.jugadorComprando = True
    
    def comprarPropiedad(self):
        self.obtenerCiudadActual().propietario = self.jugadorConTurno
        self.jugadorConTurno.dinero = abs(self.obtenerCiudadActual().precio - self.jugadorConTurno.dinero)
        self.jugadorComprando = False
        self.actualizarJugadorConTurno()
        
    def obtenerCiudadPorCasilla(self, casilla):
        return self.ciudades[casilla]
    
    def obtenerJugadoresEnCasilla(self, casilla):
        contador = 0
        for jugador in self.jugadores: 
            if jugador.casilla == casilla: contador += 1
        return contador
    
    def moverJugadorConTurno(self):
        if self.jugadorConTurno.casilla == 27: self.jugadorConTurno.casilla = 0
        if self.jugadorConTurno.casilla != self.jugadorConTurno.casillaFinal: self.jugadorConTurno.casilla += 1
        self.jugadorConTurno.establecerPosicion(self.posiciones[POSICION_CASILLA][self.jugadorConTurno.casilla])
        if self.jugadorConTurno.casilla == self.jugadorConTurno.casillaFinal: self.terminarMovimiento()

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
        jugador.establecerPosicion(self.posiciones[POSICION_CASILLA][0])