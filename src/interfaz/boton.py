import pygame.font
from src.constantes import *

class Boton:
    def __init__(self, x, y, fuente=FUENTE_PRINCIPAL, tamaniof=TF_NORMAL, grueso=False, colort=BLANCO, bg=NEGRO, escala=ESCALA_NORMAL, m=None, input=False, acciones=False):
        self.x, self.y = x, y
        self.anchura, self.altura = escala
        self.fuente = pygame.font.SysFont(fuente, tamaniof, bold=False)
        self.permiteEntrada = input
        self.fondo = bg
        self.fondoPorDefecto = bg
        self.colorTexto = colort
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.altura)
        self.acciones = acciones
        self.mensaje = m
        self.prepararMensaje(self.mensaje)
    
    def prepararMensaje(self, mensaje):
        self.imagenMensaje = self.fuente.render(mensaje, True, self.colorTexto, self.fondo)
        self.imagenMensajeRect = self.imagenMensaje.get_rect()
        self.imagenMensajeRect.center = self.rect.center

    def cambiarColor(self, colorTexto, colorFondo):
        self.imagenMensaje = self.fuente.render(self.mensaje, True, colorTexto, colorFondo)
        self.fondo = colorFondo

    def cambiarTexto(self, m):
        self.mensaje = m
    
    def estaColiccionando(self, punto):
        return self.rect.collidepoint(punto)

    def agregarAccion(self, accion):
        print(accion, 'agregando')
        self.acciones.append(accion)
    
    def ejecutarAcciones(self):
        if not self.acciones: return False 
        else: 
            for accion in self.acciones: accion()
    
    def mostrar(self, pantalla):
        pantalla.fill(self.fondo, self.rect)
        pantalla.blit(self.imagenMensaje, self.imagenMensajeRect)