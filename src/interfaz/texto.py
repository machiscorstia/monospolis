import pygame.font
from src.constantes import *

class Texto:
    def __init__(self, x, y, fuente=FUENTE_PRINCIPAL, grueso=False, tamaniof=TF_NORMAL, colort=BLANCO, escala=ESCALA_NORMAL, m=None):
        self.x, self.y = x, y
        self.anchura, self.altura = escala
        self.fuente = pygame.font.SysFont(fuente, tamaniof, bold= grueso)
        self.colorFondo = (0,0,0,0)
        self.colorTexto = colort
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.altura)
        self.mensaje = m
        self.prepararMensaje(self.mensaje)
    
    def prepararMensaje(self, mensaje):
        self.mensajeImagen = self.fuente.render(mensaje, True, self.colorTexto, self.colorFondo)
        self.mensajeImagenRect = self.mensajeImagen.get_rect()
        self.mensajeImagenRect.center = self.rect.center

    def mostrar(self, pantalla):
        self.mensajeImagen.set_colorkey(self.colorFondo)
        pantalla.blit(self.mensajeImagen, self.mensajeImagenRect)