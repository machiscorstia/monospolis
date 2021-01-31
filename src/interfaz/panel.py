import pygame as py
import os
from src.constantes import *
from src.interfaz.boton import Boton

class Panel:
    def __init__(self, pantalla, fondo, elementos={}):
        self.pantalla = pantalla   
        self.imagen = py.image.load(fondo)
        self.elementos = elementos
    
    def agregarElemento(self, elemento):
        self.elementos.update(elemento)

    def mostrarFondo(self):
        self.pantalla.blit(self.imagen, (0, 0))
    
    def obtenerColiccion(self, punto, tipo):
        for elemento in self.elementos.keys():
            if isinstance(elemento, tipo) and elemento.estaColiccionando(punto):
                return elemento
    
    def chequearSuperposicion(self, punto):
        for elemento in self.elementos.keys():
            if isinstance(elemento, Boton):
                if elemento.estaColiccionando(punto): elemento.cambiarColor(NEGRO, BLANCO)
                else: elemento.cambiarColor(BLANCO, elemento.fondoPorDefecto)

    def accionarElemento(self, punto):
        for elemento, accion in self.elementos.items(): 
            if elemento == self.obtenerColiccion(punto, Boton): accion()
        
    def mostrarElementos(self):
        for elemento in self.elementos: elemento.mostrar(self.pantalla)