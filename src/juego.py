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
        self.fps = FPS_DISPONIBLES[0]
        self.reloj = py.time.Clock()
        self.centro =  ANCHURA/2 - ESCALA_NORMAL[0]/2
        self.pantalla = py.display.set_mode( (ANCHURA, ALTURA) )
        self.posicionDelRaton = py.mouse.get_pos()

        self.tablero = Tablero()

        self.ingresandoInformacion = False
        self.objetivoJugador = 0
        self.entradaObjetivo = None
        self.bufferJugador = []

        py.display.set_caption("Monospolis")

        self.contador = 0
        self.eventoAdvertencia = py.USEREVENT + 1
        self.botonAdvertencia = self.botonAdvertencia = Boton(100, 100, bg=NEGRO, escala=(300,40), tamaniof=20,m='Nadita', dinamico=True)
        self.hayAdvertencia = False

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

                    Texto(self.centro/1.6, 300, tamaniof=25, m='Fps'),
                    Boton(ANCHURA/2, 310, tamaniof=20, escala=ESCALA_INTER, bg=AZUL_OSCURO, dinamico=True,
                        m = self.fps,
                        acciones = [self.cambiarFps]
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
    
    def agregarAdvertencia(self, mensaje, tiempo):
        self.contador = tiempo
        self.botonAdvertencia.cambiarTexto(mensaje)
        py.time.set_timer(self.eventoAdvertencia, tiempo)

    def cambiarFps(self):
        pass

    def comenzarPartida(self):
        
        if self.ingresandoInformacion: self.ingresandoInformacion = False
        if len(self.bufferJugador) != self.tablero.cantidadJugadores:
            self.hayAdvertencia = True
            print(self.posicionDelRaton)
            self.botonAdvertencia.rect.x, self.botonAdvertencia.rect.y= self.posicionDelRaton
            self.agregarAdvertencia('Ingresa todos los nombres', 20)

    
    def actualizarFondo(self): self.obtenerPanelActual().mostrarFondo()

    def restablecerJugadores(self): 
        self.objetivoJugador = 0
        self.ingresandoInformacion = False
        if self.entradaObjetivo: self.entradaObjetivo.cambiarColor(BLANCO, COLOR_JUGADORES[self.objetivoJugador])
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
        
        if self.ingresandoInformacion and self.obtenerColiccionBoton().permiteEntrada: 
            self.entradaObjetivo = self.obtenerColiccionBoton()
            self.entradaObjetivo.cambiarTexto('')

        self.obtenerPanelActual().accionarElemento(self.posicionDelRaton)

    def prepararPartida(self):
        self.establecerPanelIngreso()

    def chequearIngresoTeclado(self, evento):
        if evento.unicode.isalpha(): self.entradaObjetivo.agregarCaracter(evento.unicode)
        elif evento.key == py.K_BACKSPACE: self.entradaObjetivo.eliminarCaracter()
        elif evento.key == py.K_SPACE: self.entradaObjetivo.agregarCaracter(' ')

        elif evento.key == py.K_RETURN and self.entradaObjetivo.mensaje != '':
            self.bufferJugador.append(self.entradaObjetivo.obtenerTexto())
            self.objetivoJugador += 1
            self.actualizarEntradaObjetivo()
            if self.objetivoJugador == self.tablero.cantidadJugadores:
                print(self.bufferJugador)
                self.ingresandoInformacion = False
                self.establecerPanelPartida()

    def actualizarAdvertencia(self):
        self.contador -= 1
        if self.contador == 0:
            self.hayAdvertencia = False
            py.time.set_timer(self.eventoAdvertencia, 0)
    
    def mostrarAdvertencia(self): self.botonAdvertencia.mostrar(self.pantalla)

    def chequearEventos(self):
        self.chequearSuperposicion()

        for evento in py.event.get():
            if evento.type == py.QUIT: self.detener()
            elif evento.type == py.MOUSEBUTTONDOWN: self.accionarBoton() if self.obtenerColiccionBoton() else None
            elif evento.type == py.MOUSEMOTION: pass
            elif evento.type == self.eventoAdvertencia: self.actualizarAdvertencia()
            elif evento.type == py.KEYDOWN and self.ingresandoInformacion: self.chequearIngresoTeclado(evento)
    
    def actualizarEntradaObjetivo(self):
        self.entradaObjetivo.cambiarColor(BLANCO, COLOR_JUGADORES[self.objetivoJugador])
        self.entradaObjetivo.cambiarTexto('Clic para ingresar nombre')
    
    def actualizarPantalla(self):
        self.actualizarFondo()
        self.actualizarPosicionDelRaton()
        self.obtenerPanelActual().mostrarElementos()
        if self.hayAdvertencia: self.mostrarAdvertencia()
        self.reloj.tick(60)
        py.display.update()

    def iniciar(self):
        self.corriendo = True
        self.panelActual = PANEL_MENU
        self.actualizarPantalla()
        while self.corriendo: 
            self.actualizarPantalla()
            self.chequearEventos()
        py.quit()