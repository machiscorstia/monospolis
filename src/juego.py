import sys, os, pygame as py

from src.constantes import *
from src.tablero import *

from src.interfaz.graficos import *
from src.interfaz.texto import Texto
from src.interfaz.boton import Boton
from src.interfaz.panel import Panel

class Juego:
    def __init__(self):
        py.init()
        self.corriendo = False
        self.centro =  ANCHURA/2 - ESCALA_NORMAL[0]/2
        self.pantalla = py.display.set_mode( (ANCHURA, ALTURA) )
        self.posicionDelRaton = py.mouse.get_pos()

        self.tablero = Tablero()

        self.ingresandoInformacion = False
        self.objetivoInput = None

        py.display.set_caption("Monospolis")

        self.panelActual = None
        self.paneles = [
            Panel(self.pantalla, 
            fondo = os.getcwd() + '/imgs/fondos/menu.jpg', 
            elementos = [
                    Texto(self.centro, 180, grueso=True, tamaniof=60 , m='MONOS POLIS'),
                    Boton(self.centro, 300, m='Empezar', acciones = [self.establecerPanelPartida]), 
                    Boton(self.centro, 400, m='Configurar', acciones = [self.establecerPanelConfiguracion]),
                    Boton(self.centro, 500, m='Salir', acciones = [self.detener])
                ]
            ),
            Panel(self.pantalla, 
                fondo = os.getcwd() + '/imgs/fondos/configuracion.jpg', 
                elementos = [
                    Texto(self.centro, 50, grueso=True, tamaniof=50 , m='Configuracion'),

                    Texto(self.centro/1.5, 150, tamaniof=25, m='Jugadores'),
                    Boton(ANCHURA/2, 160, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, 
                        m = str(self.tablero.cantidadJugadores), 
                        acciones = [self.cambiarCantidadJugadores]
                    ),

                    Texto(self.centro/2, 200, tamaniof=25, m='Dinero neto máximo'),
                    Boton(ANCHURA/2, 210, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, 
                        m = str(self.tablero.netoMaximo) + '$', 
                        acciones = [self.cambiarNetoMaximo]
                    ),

                    Boton(self.centro, 700, m='Volver', acciones=[self.establecerPanelMenu])
                ]
            )
        ]
    
    def cambiarCantidadJugadores(self): self.obtenerColiccionBoton().cambiarTexto(str(self.tablero.cambiarCantidadJugadores()))
    
    def cambiarNetoMaximo(self): self.obtenerColiccionBoton().cambiarTexto(str(self.tablero.cambiarNeto()) + '$')

    def establecerAjustes(self): pass

    def detener(self): self.corriendo = False

    def actualizarFondo(self): self.paneles[self.panelActual].mostrarFondo()

    def actualizarPosicionDelRaton(self): self.posicionDelRaton = py.mouse.get_pos()

    def establecerPanelMenu(self): self.panelActual = PANEL_MENU

    def establecerPanelPartida(self): self.panelActual = PANEL_PARTIDA
    
    def establecerPanelConfiguracion(self): self.panelActual = PANEL_CONFIGURACION

    def chequearSuperposicion(self): self.paneles[self.panelActual].chequearSuperposicion(self.posicionDelRaton)

    def obtenerColiccionBoton(self): return self.paneles[self.panelActual].obtenerColiccion(self.posicionDelRaton, Boton)

    def accionarAccionBoton(self):
        if not self.ingresandoInformacion and self.obtenerColiccionBoton().permiteEntrada:
            self.entradaObjetivo = self.obtenerColiccionBoton()
            self.ingresandoInformacion = True
        self.paneles[self.panelActual].accionarElemento(self.posicionDelRaton)

    def chequearEventos(self):
        self.chequearSuperposicion()
        for evento in py.event.get():
            if evento.type == py.QUIT: self.detener()
            if evento.type == py.MOUSEBUTTONDOWN: self.accionarAccionBoton() if self.obtenerColiccionBoton() else None
            if evento.type == py.MOUSEMOTION: self.actualizarPantalla()
            if evento.type == py.KEYDOWN and self.ingresandoInformacion:
                if evento.unicode.isalpha():
                    print(evento.unicode)
                elif evento.key == py.K_RETURN:
                    self.ingresandoInformacion = False
    
    def actualizarPantalla(self):
        self.actualizarFondo()
        self.actualizarPosicionDelRaton()
        self.paneles[self.panelActual].mostrarElementos()
        py.display.update()

    def iniciar(self):
        self.corriendo = True
        self.panelActual = PANEL_MENU
        self.actualizarPantalla()
        while self.corriendo: self.chequearEventos()
        py.quit()