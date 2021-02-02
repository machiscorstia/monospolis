def crearRutaVertical(yi, yf, x, s):
    ruta = list()
    for y in range(yi, yf, s): ruta.append([x, y])
    return ruta

def crearRutaHorizontal(xi, xf, y, s):
    ruta = list()
    for x in range(xi, xf, s): ruta.append([x, y])
    return ruta

def siguienteItem(valorActual, lista):
    index = lista.index(valorActual)
    if index < len(lista) - 1: index += 1
    else: index = 0
    return index
    
def generarPosicionesTablero():
    ruta = list()
    for posicion in crearRutaVertical(750, 0, x=50, s=-50): ruta.append(posicion)
    for posicion in crearRutaHorizontal(100, 800, y=50, s=50): ruta.append(posicion)
    for posicion in crearRutaVertical(50, 800, x=750, s=50): ruta.append(posicion)
    for posicion in crearRutaHorizontal(800, 50, y=750, s=-50): ruta.append(posicion)
    return ruta