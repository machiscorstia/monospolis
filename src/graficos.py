import pygame as py
from src.constantes import *

def cargarFondos():
    return [
        py.image.load('./imgs/fondos/menu.jpg'),
        py.image.load('./imgs/fondos/configuracion.jpg'),
        py.image.load('./imgs/fondos/partida.png')
    ]
def cargarImagenFicha():
    return py.image.load('./imgs/ficha.png')
    
