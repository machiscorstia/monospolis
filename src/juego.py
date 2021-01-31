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
        self.tablero = Tablero()
        self.centro =  ANCHURA/2 - B_ESCALA[0]/2
        self.pantalla = py.display.set_mode( (ANCHURA, ALTURA) )
        self.posicionDelRaton = py.mouse.get_pos()
        py.display.set_caption("Monospolis")

        self.panelActual = None
        self.paneles = [
            Panel(self.pantalla, 
            fondo = os.getcwd() + '/imgs/fondos/menu.jpg', 
            elementos = {
                    Texto(self.centro, 180, grueso=True, tamaniof=60 , m='MONOS POLIS'): NotImplemented,
                    Boton(self.centro, 300, m='Empezar'): self.establecerPanelPartida, 
                    Boton(self.centro, 400, m='Configurar'): self.establecerPanelConfiguracion,
                    Boton(self.centro, 500, m='Salir'): self.detener
                }
            ),
            Panel(self.pantalla, 
            fondo = os.getcwd() + '/imgs/fondos/configuracion.jpg', 
            elementos = {
                    Texto(self.centro, 100, grueso=True, tamaniof=50 , m='Configuracion'): None,
                    Texto(self.centro/2, 200, m='Cantidad de jugadores'): None,
                    Boton((self.centro/2)*3, 200, escala=(100, 50), bg=VERDE, m='2'): None,
                    Boton(self.centro, 700, m='Volver'): self.establecerPanelMenu
                }
            )
        ]

    def establecerAjustes(self): pass

    def detener(self): self.corriendo = False

    def actualizarFondo(self): self.paneles[self.panelActual].mostrarFondo()

    def actualizarPosicionDelRaton(self): self.posicionDelRaton = py.mouse.get_pos()

    def establecerPanelMenu(self): self.panelActual = PANEL_MENU

    def establecerPanelPartida(self): self.panelActual = PANEL_PARTIDA
    
    def establecerPanelConfiguracion(self): self.panelActual = PANEL_CONFIGURACION

    def chequearSuperposicion(self): self.paneles[self.panelActual].chequearSuperposicion(self.posicionDelRaton)

    def obtenerColiccionBoton(self): return self.paneles[self.panelActual].obtenerColiccion(self.posicionDelRaton, Boton)

    def accionarAccionBoton(self): self.paneles[self.panelActual].accionarElemento(self.posicionDelRaton)

    def chequearEventos(self):
        self.chequearSuperposicion()
        for evento in py.event.get():
            if evento.type == py.QUIT: self.detener()
            if evento.type == py.MOUSEBUTTONDOWN: self.accionarAccionBoton() if self.obtenerColiccionBoton() else None
            if evento.type == py.MOUSEMOTION: self.actualizarPantalla()
    
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