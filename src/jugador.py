import pygame as py
from src.constantes import *
from src.interfaz.graficos import *
from src.interfaz.texto import Texto

class Jugador:
    def __init__(self, nombre, posicion = J_POSICION_PREDETERMINADO, casilla=0, color = J_COLOR_PREDETERMINADO):
        self.nombre = nombre
        self.neto = 0
        self.dinero = J_DINERO_PREDETERMINADO
        self.posicion = posicion
        self.casilla = 0
        self.casillaFinal = 0
        self.imagen = cargarImagenFicha()
        self.textoNombre = Texto(100, 100, grueso=True, colort=color,tamaniof=TF_MEDIANO, escala=ESCALA_MEDIANA, centrado=False, m=f'{self.nombre}')
        self.textoDinero = Texto(100, 100, grueso=True, tamaniof=TF_MEDIANO, escala=ESCALA_MEDIANA, centrado=False, colort=VERDE, m=f'{self.dinero}$ ({self.neto})', dinamico=True)
        self.colorFicha = py.Surface(self.imagen.get_size()).convert_alpha()
        self.colorFicha.fill(color)
        self.imagen.blit(self.colorFicha, (0,0), special_flags= py.BLEND_RGBA_MULT)
        self.rect = self.imagen.get_rect()
        self.rect.x, self.rect.y = posicion
    
    def mostrarNombre(self, pantalla, posicion):
        self.textoNombre.rect.x, self.textoNombre.rect.y = posicion
        self.textoNombre.mostrar(pantalla)
    
    def mostrarDinero(self, pantalla, posicion):
        self.textoDinero.rect.x, self.textoDinero.rect.y = posicion
        self.textoDinero.mostrar(pantalla)
    
    def obtenerPosicion(self): return self.rect

    def establecerPosicion(self, posicion):
        self.posicion = posicion
        self.rect.centerx, self.rect.centery = self.posicion

    def mostrar(self, pantalla): pantalla.blit(self.imagen, self.rect)