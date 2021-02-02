import pygame as py
import os
from src.constantes import *
from src.interfaz.boton import Boton

class Panel:
    def __init__(self, pantalla, fondo, elementos=[]):
        self.pantalla = pantalla   
        self.imagen = py.image.load(fondo)
        self.elementos = elementos
    
    def modificar(self, elemento, mensaje=None):
        if mensaje == None: return False
    
    def agregarElemento(self, elemento):
        self.elementos.update(elemento)

    def mostrarFondo(self):
        self.pantalla.blit(self.imagen, (0, 0))
    
    def obtenerColiccion(self, punto, tipo):
        for elemento in self.elementos:
            if isinstance(elemento, tipo) and elemento.estaColiccionando(punto):
                return elemento
    
    def chequearSuperposicion(self, punto):
        for elemento in self.elementos:
            if isinstance(elemento, Boton):
                if elemento.estaColiccionando(punto): elemento.cambiarColor(NEGRO, BLANCO)
                else: elemento.cambiarColor(BLANCO, elemento.fondoPorDefecto)

    def accionarElemento(self, punto):
        for elemento in self.elementos: 
            if elemento == self.obtenerColiccion(punto, Boton): elemento.ejecutarAcciones()
    
    def mostrarElementos(self):
        for elemento in self.elementos: elemento.mostrar(self.pantalla)