def crearRutaVertical(yi, yf, x, s):
    ruta = list()
    for y in range(yi, yf, s): ruta.append([x, y])
    return ruta

def crearRutaHorizontal(xi, xf, y, s):
    ruta = list()
    for x in range(xi, xf, s):
        ruta.append([x, y])
    return ruta

def siguienteItem(valorActual, lista):
    index = lista.index(valorActual)
    if index < len(lista) - 1: index += 1
    else: index = 0
    return index

def verificarExistencia(numero, lista):
    existe = False
    for i in lista:
        if numero == i: existe = True
    return existe
        
def generarPosicionPrecios():
    ruta = list()
    temp = None
    for i, r in enumerate(generarPosicionesTablero()):
        if i < 7: temp = [r[0]-15, r[1]- 40]
        elif i > 7 and i < 14: temp = [r[0], r[1]-35]
        elif i > 14 and i < 21: temp = [r[0], r[1]-35]
        else: temp = [r[0]+15, r[1]-35]
        ruta.append(temp)
    return ruta   

def generarPosicionPropietario():
    ruta = list()
    temp = None
    for i, r in enumerate(generarPosicionesTablero()):
        if i < 7: temp = [r[0]-40, r[1]- 35]
        elif i > 7 and i < 14: temp = [r[0]+20, r[1]-35]
        elif i > 14 and i < 21: temp = [r[0]+20, r[1]-35]
        else: temp = [r[0]+15, r[1]-35]
        ruta.append(temp)
    return ruta   

def generarPosicionCiudades():
    ruta = list()
    temp = None
    for i, r in enumerate(generarPosicionesTablero()):
        if i < 7: temp = [r[0]-10, r[1]+18]
        elif i > 7 and i < 14: temp = [r[0]-5, r[1]+18]
        elif i > 14 and i < 21: temp = [r[0]-10, r[1]+18]
        else: temp = [r[0]-10, r[1]+18]
        ruta.append(temp)
    return ruta

def generarPosicionesTablero():
    ruta = list()
    for posicion in crearRutaVertical(750, 0, x=50, s=-100): ruta.append(posicion)
    for posicion in crearRutaHorizontal(150, 800, y=50, s=100): ruta.append(posicion)
    for posicion in crearRutaVertical(150, 800, x=750, s=100): ruta.append(posicion)
    for posicion in crearRutaHorizontal(650, 50, y=750, s=-100): ruta.append(posicion)
    return ruta