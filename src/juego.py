import sys, pygame as py
from src.constantes import *
from src.graficos import *
from src.tablero import *
from src.texto import *
from src.boton import *

class Juego:
    def __init__(self):
        py.init()
        self.centro =  ANCHURA/2 - B_ESCALA[0]/2
        self.corriendo = False
        self.panelActual = None
        self.panelFondos = cargarFondos()
        self.panelElementos = list()
        self.tablero = Tablero()
        self.cargarElementos()
        self.pantalla = py.display.set_mode( (ANCHURA, ALTURA) )
        self.posicionDelRaton = py.mouse.get_pos()
        py.display.set_caption("Monospolis")

    def establecerAjustes(self): pass

    def detener(self): self.corriendo = False

    def actualizarFondo(self): self.pantalla.blit(self.panelFondos[self.panelActual], (0, 0))

    def actualizarPosicionDelRaton(self): self.posicionDelRaton = py.mouse.get_pos()

    def establecerPanelMenu(self): self.panelActual = PANEL_MENU

    def establecerPanelPartida(self): self.panelActual = PANEL_PARTIDA
    
    def establecerPanelConfiguracion(self): self.panelActual = PANEL_CONFIGURACION

    def cargarElementos(self):
        self.panelElementos.append(self.cargarElementosMenu())
        self.panelElementos.append(self.cargarElementosConfiguracion())
    
    def cargarElementosConfiguracion(self):
        return {
            Texto(self.centro, 180, grueso=True, tamaniof=50 , m='Configuracion'): NotImplemented,
            Boton(self.centro, 500, m='Volver'): self.establecerPanelMenu
        }

    def cargarElementosMenu(self):
        return {
            Texto(self.centro, 180, grueso=True, tamaniof=60 , m='MONOS POLIS'): NotImplemented,
            Boton(self.centro, 300, m='Empezar'): self.establecerPanelPartida, 
            Boton(self.centro, 400, m='Configurar'): self.establecerPanelConfiguracion,
            Boton(self.centro, 500, m='Salir'): self.detener
        }
    
    def chequearSuperposicionBoton(self):
        for elemento in self.panelElementos[self.panelActual]:
            if isinstance(elemento, Boton):
                if elemento.estaColiccionando(self.posicionDelRaton): elemento.cambiarColor(NEGRO, BLANCO)
                else: elemento.cambiarColor(BLANCO, elemento.fondoPorDefecto)

    def obtenerColiccionBoton(self):
        for elemento in self.panelElementos[self.panelActual]:
            if isinstance(elemento, Boton) and elemento.estaColiccionando(self.posicionDelRaton):
                return elemento

    def chequearClickBoton(self):
        for elemento, accion in self.panelElementos[self.panelActual].items(): 
            if elemento == self.obtenerColiccionBoton(): accion()

    def chequearEventos(self):
        self.chequearSuperposicionBoton()
        for evento in py.event.get():
            if evento.type == py.QUIT: self.detener()
            if evento.type == py.MOUSEBUTTONDOWN: self.chequearClickBoton() if self.obtenerColiccionBoton else None
            if evento.type == py.MOUSEMOTION: self.actualizarPantalla()
    
    def actualizarPantalla(self):
        self.actualizarFondo()
        self.actualizarPosicionDelRaton()
        for elemento in self.panelElementos[self.panelActual]: elemento.mostrar(self.pantalla)
        py.display.update()

    def iniciar(self):
        self.corriendo = True
        self.panelActual = PANEL_MENU
        self.actualizarPantalla()
        print(self.tablero.mostrarPosiciones())
        while self.corriendo: self.chequearEventos()
        py.quit()