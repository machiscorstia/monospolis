def crearCasillaVertical(x_max, positivo=True, y=100, saltos=100):
    casilla = []
    target = None
    if positivo: 
        x = 0 
        target = x_max
    else: 
        x = 800
        target = 0

    while x != target:
        if positivo: x += saltos
        else: x -= saltos
        casilla.append([x, y])
    return casilla

            
print(crearCasillaVertical(800, positivo=False, y=100, saltos=100))