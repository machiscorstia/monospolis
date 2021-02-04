import pygame.font
from src.constantes import *

class Texto:
    def __init__(self, x, y, fuente=FUENTE_PRINCIPAL, grueso=False, tamaniof=TF_NORMAL, bg=NEGRO, colort=BLANCO, escala=ESCALA_NORMAL, m=None, dinamico=True):
        self.x, self.y = x, y
        self.anchura, self.altura = escala
        self.fuente = pygame.font.SysFont(fuente, tamaniof, bold= grueso)
        self.colorFondo = bg
        self.colorTexto = colort
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.altura)
        self.mensaje = m
        self.dinamico = dinamico
        self.caracterLimite = None
        self.prepararMensaje(self.mensaje)
    
    def cambiarTexto(self, m): self.mensaje = str(m)
    
    def agregarCaracter(self, caracter): self.mensaje += str(caracter)
    
    def eliminarCaracter(self): 
        if self.mensaje[len(self.mensaje) - 1] != self.caracterLimite: self.mensaje = self.mensaje[:-1]

    def prepararMensaje(self, mensaje):
        self.mensajeImagen = self.fuente.render(mensaje, True, self.colorTexto, self.colorFondo)
        self.mensajeImagenRect = self.mensajeImagen.get_rect()
        self.mensajeImagenRect.center = self.rect.center

    def mostrar(self, pantalla):
        if self.dinamico: self.prepararMensaje(self.mensaje)
        self.mensajeImagen.set_colorkey(self.colorFondo)
        pantalla.blit(self.mensajeImagen, self.mensajeImagenRect)