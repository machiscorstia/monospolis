import pygame as py
from src.constantes import *
from src.interfaz.graficos import *
from src.interfaz.texto import Texto

class Jugador:
    def __init__(self, nombre = J_NOMBRE, posicion = J_POSICION, color = J_COLOR):
        self.nombre = nombre
        self.dinero = J_DINERO
        self.posicion = nombre
        self.imagen = cargarImagenFicha()
        self.moviendose = False
        self.imagenInformacion = Texto(100, 100, grueso=True, tamaniof=TF_MEDIANO, escala=ESCALA_MEDIANA, m=f'{self.nombre}: {self.dinero}', dinamico=True)
        self.colorFicha = py.Surface(self.imagen.get_size()).convert_alpha()
        self.colorFicha.fill(color)
        self.imagen.blit(self.colorFicha, (0,0), special_flags= py.BLEND_RGBA_MULT)
        self.rect = self.imagen.get_rect()
        self.rect.x, self.rect.y = posicion

    def comenzarMovimiento(self, posicionInicio, posicionFinal):
        pass
    
    def mostrarInformacion(self, pantalla, posicion):
        self.imagenInformacion.rect.x, self.imagenInformacion.rect.y = posicion
        self.imagenInformacion.mostrar(pantalla)
    
    def establecerPosicion(self, posicion): self.rect.centerx, self.rect.centery = posicion

    def mostrar(self, pantalla): pantalla.blit(self.imagen, self.rect)