import pygame.font
from src.constantes import *

class Boton:
    def __init__(self, x, y, fuente = B_FUENTE, tamanio = B_FTAMANIO, colort = BLANCO, bg = NEGRO, escala = B_ESCALA, m = None, accion=None):
        self.x, self.y = x, y
        self.anchura, self.altura = escala
        self.fuente = pygame.font.SysFont(fuente, tamanio)
        self.fondo = bg
        self.fondoPorDefecto = bg
        self.colorTexto = colort
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.altura)
        self.accion = accion
        self.mensaje = m
        self.prepararMensaje(self.mensaje)
    
    def prepararMensaje(self, mensaje):
        self.imagenMensaje = self.fuente.render(mensaje, True, self.colorTexto, self.fondo)
        self.imagenMensajeRect = self.imagenMensaje.get_rect()
        self.imagenMensajeRect.center = self.rect.center

    def cambiarColor(self, colorTexto, colorFondo):
        self.imagenMensaje = self.fuente.render(self.mensaje, True, colorTexto, colorFondo)
        self.fondo = colorFondo
    
    def estaColiccionando(self, punto):
        return self.rect.collidepoint(punto)

    def ejecutarAccion(self):
        return self.accion
    
    def mostrar(self, pantalla):
        pantalla.fill(self.fondo, self.rect)
        pantalla.blit(self.imagenMensaje, self.imagenMensajeRect)