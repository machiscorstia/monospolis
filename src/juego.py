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
        self.objetivoJugador = 0
        self.entradaObjetivo = None

        py.display.set_caption("Monospolis")

        self.panelActual = None
        self.paneles = [
            Panel(self.pantalla, 
            fondo = os.getcwd() + '/imgs/fondos/menu.jpg', 
            elementos = [
                    Texto(self.centro, 180, grueso=True, tamaniof=60 , m='MONOS POLIS'),
                    Boton(self.centro, 300, m='Jugar', acciones = [self.prepararPartida]), 
                    Boton(self.centro, 400, m='Configurar', acciones = [self.establecerPanelConfiguracion]),
                    Boton(self.centro, 500, m='Salir', acciones = [self.detener])
                ]
            ),
            Panel(self.pantalla, 
                fondo = os.getcwd() + '/imgs/fondos/configuracion.jpg', 
                elementos = [
                    Texto(self.centro, 50, grueso=True, tamaniof=50 , m='Configuracion'),

                    Texto(self.centro/1.5, 150, tamaniof=25, m='Jugadores'),
                    Boton(ANCHURA/2, 160, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, dinamico=True,
                        m = self.tablero.cantidadJugadores, 
                        acciones = [self.tablero.cambiarCantidadJugadores]
                    ),

                    Texto(self.centro/1.5, 200, tamaniof=25, m='Salario'),
                    Boton(ANCHURA/2, 210, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, dinamico=True,
                        m = self.tablero.salario, 
                        acciones = [self.tablero.cambiarSalario]
                    ),

                    Texto(self.centro/1.6, 250, tamaniof=25, m='Neto máximo'),
                    Boton(ANCHURA/2, 260, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, dinamico=True,
                        m = self.tablero.netoMaximo,
                        acciones = [self.tablero.cambiarNeto]
                    ),

                    Boton(self.centro, 700, m='Volver', acciones=[self.establecerPanelMenu])
                ]
            ),
            Panel(self.pantalla, 
                fondo = os.getcwd() + '/imgs/fondos/configuracion.jpg', elementos=[
                    Texto(self.centro, 100, m='INGRESAR JUGADOR'),
                    Boton(self.centro/1.5, 200, m='Clic para ingresar nombre', bg=COLOR_JUGADORES[self.objetivoJugador], escala=[400, 50],input=True, dinamico=True),
                    Boton(self.centro, 430, m='Iniciar', bg=VERDE_OSCURO, acciones=[self.comenzarPartida]),
                    Boton(self.centro, 550, m='Volver', acciones=[self.restablecerJugadores, self.establecerPanelMenu])
                ]
            )
        ]
    
    def detener(self): self.corriendo = False
    
    def comenzarPartida(self):
        pass

    def actualizarFondo(self): self.obtenerPanelActual().mostrarFondo()

    def restablecerJugadores(self): 
        self.objetivoJugador = 0
        self.ingresandoInformacion = False
        self.obtenerPanelActual().obtenerElementos()[1].cambiarTexto('Clic para ingresar nombre')
        self.tablero.limpiarJugadores()

    def actualizarPosicionDelRaton(self): self.posicionDelRaton = py.mouse.get_pos()

    def establecerPanelMenu(self): self.panelActual = PANEL_MENU

    def establecerPanelIngreso(self): self.panelActual = PANEL_INGRESO

    def establecerPanelPartida(self): self.panelActual = PANEL_PARTIDA
    
    def establecerPanelConfiguracion(self): self.panelActual = PANEL_CONFIGURACION

    def chequearSuperposicion(self): self.obtenerPanelActual().chequearSuperposicion(self.posicionDelRaton)

    def obtenerPanelActual(self): return self.paneles[self.panelActual]

    def obtenerColiccionBoton(self): return self.obtenerPanelActual().obtenerColiccion(self.posicionDelRaton, Boton)

    def accionarBoton(self):
        if not self.ingresandoInformacion and self.obtenerColiccionBoton().permiteEntrada:
            self.entradaObjetivo = self.obtenerColiccionBoton()
            self.entradaObjetivo.cambiarTexto('')
            self.ingresandoInformacion = True
        self.obtenerPanelActual().accionarElemento(self.posicionDelRaton)

    def prepararPartida(self):
        self.establecerPanelIngreso()
    
    def chequearIngresoTeclado(self, evento):
        if evento.unicode.isalpha(): self.entradaObjetivo.agregarCaracter(evento.unicode)
        elif evento.key == py.K_BACKSPACE: self.entradaObjetivo.eliminarCaracter()
        elif evento.key == py.K_SPACE: self.entradaObjetivo.agregarCaracter(' ')
        elif evento.key == py.K_RETURN and self.entradaObjetivo.mensaje != '':
            self.objetivoJugador += 1
            self.entradaObjetivo.cambiarColor(BLANCO, COLOR_JUGADORES[self.objetivoJugador])
            self.entradaObjetivo.cambiarTexto('Nombre..')
            if self.objetivoJugador == self.tablero.cantidadJugadores:
                self.ingresandoInformacion = False
                self.entradaObjetivo.cambiarColor(BLANCO, COLOR_JUGADORES[self.objetivoJugador])
                self.establecerPanelPartida()

    def chequearEventos(self):
        self.chequearSuperposicion()

        for evento in py.event.get():
            if evento.type == py.QUIT: self.detener()
            if evento.type == py.MOUSEBUTTONDOWN: self.accionarBoton() if self.obtenerColiccionBoton() else None
            if evento.type == py.MOUSEMOTION: pass
            if evento.type == py.KEYDOWN and self.ingresandoInformacion: self.chequearIngresoTeclado(evento)
    
    def actualizarPantalla(self):
        self.actualizarFondo()
        self.actualizarPosicionDelRaton()
        self.obtenerPanelActual().mostrarElementos()
        py.display.update()

    def iniciar(self):
        self.corriendo = True
        self.panelActual = PANEL_MENU
        self.actualizarPantalla()
        while self.corriendo: 
            self.actualizarPantalla()
            self.chequearEventos()
        py.quit()