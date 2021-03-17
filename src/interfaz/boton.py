import pygame.font
from src.constantes import *

class Boton:
    def __init__(self, x, y, fuente=FUENTE_PRINCIPAL, tamaniof=TF_NORMAL, grueso=False, colort=BLANCO, bg=NEGRO, escala=ESCALA_NORMAL, m=None, oculto=False, dinamico=False, input=False, acciones=False):
        self.x, self.y = x, y
        self.anchura, self.altura = escala
        self.fuente = pygame.font.SysFont(fuente, tamaniof, bold=False)
        self.permiteEntrada = input
        self.fondo = bg
        self.fondoPorDefecto = bg
        self.oculto = oculto
        self.colorTexto = colort
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.altura)
        self.acciones = acciones
        self.mensaje = str(m) if type(m) == int else m
        self.dinamico = dinamico
        self.prepararMensaje(self.mensaje)
    
    def prepararMensaje(self, m):
        self.imagenMensaje = self.fuente.render(m, True, self.colorTexto, self.fondo)
        self.imagenMensajeRect = self.imagenMensaje.get_rect()
        self.imagenMensajeRect.center = self.rect.center

    def obtenerTexto(self): return self.mensaje
    
    def cambiarFondo(self, fondo): self.fondo = fondo
    
    def cambiarColor(self, colorTexto, colorFondo):
        self.imagenMensaje = self.fuente.render(self.mensaje, True, colorTexto, colorFondo)
        self.fondo = colorFondo

    def mensajeNulo(self): return self.mensaje

    def agregarCaracter(self, caracter): self.mensaje += str(caracter)
    
    def eliminarCaracter(self): self.mensaje = self.mensaje[:-1]
    
    def cambiarTexto(self, m): self.mensaje = str(m)
    
    def estaColiccionando(self, punto): return self.rect.collidepoint(punto)

    def agregarAccion(self, accion): self.acciones.append(accion)
    
    def ejecutarAcciones(self):
        if not self.acciones: return False 
        else: 
            for accion in self.acciones: 
                accion = accion()
                if accion: self.mensaje = str(accion) if type(accion) == int else accion
    
    def mostrar(self, pantalla):
        if self.oculto: return
        if self.dinamico: self.prepararMensaje(self.mensaje)
        pantalla.fill(self.fondo, self.rect)
        pantalla.blit(self.imagenMensaje, self.imagenMensajeRect)