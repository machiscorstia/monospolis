from src.constantes import *
from src.graficos import *

class Jugador:
    def __init__(self, nombre = J_NOMBRE, posicion = J_POSICION, color = J_COLOR):
        self.nombre = nombre
        self.dinero = J_DINERO
        self.posicion = nombre
        self.imagen = cargarImagenFicha()
        self.moviendose = False
        self.rect = self.imagen.get_rect()
        self.rect.x, self.rect.y = posicion

    def mostrar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)