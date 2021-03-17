import pygame as py
from src.constantes import *
from src.interfaz.texto import Texto
from src.interfaz.boton import Boton

class Ciudad:
    def __init__(self, nombre, precio, posicionNombre, posicionPrecio, posicionPropietario, propietario=None):
        self.nombre = nombre
        self.precio = precio
        self.moviendose = False
        self.propietario = propietario
        self.xn, self.yn = posicionNombre
        self.xp, self.yp = posicionPropietario
        self.xpr, self.ypr = posicionPrecio
        self.textoNombre = Texto(self.xn, self.yn, grueso=False, colort=NEGRO,tamaniof=16, escala=(20,20), centrado=True, m=f'{self.nombre}')
        self.textoPrecio = Texto(self.xpr, self.ypr, grueso=True, colort=BLANCO,tamaniof=TF_MEDIANO, escala=ESCALA_MEDIANA, centrado=False, m=f'{self.precio}$')
        self.botonPropietario = Boton(self.xp, self.yp, grueso=False, escala=(20,20),bg=BLANCO,m='')

    def establecerPosicionPropietario(self, posicion): self.botonPropietario.rect.centerx, self.botonPropietario.rect.centery = posicion
    
    def mostrarPropietario(self, pantalla):
        #if self.propietario: self.botonPropietario.mostrar(pantalla)
        self.botonPropietario.mostrar(pantalla)
    
    def mostrarPrecio(self, pantalla): 
        if self.precio != 0: self.textoPrecio.mostrar(pantalla)
    
    def mostrarNombre(self, pantalla): self.textoNombre.mostrar(pantalla)
    
    def establecerPosicionNombre(self, posicion): self.textoNombre.rect.centerx, self.textoNombre.rect.centery = posicion