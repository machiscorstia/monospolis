# Pantalla
FPS_PREDETERMINADO  = 2
FPS_DISPONIBLES     = [25, 30, 60, 120]
ANCHURA, ALTURA     = 800, 800

# Tablero
JUGADORES_PREDETERMINADO    = 0
NETO_PREDETERMINADO         = 0
SALARIO_PREDETERMINADO      = 0

POSICION_CASILLA        = 0
POSICION_NOMBRE_CIUDAD  = 1
POSICION_PRECIO_CIUDAD  = 2
POSICION_PROP_CIUDAD    = 3

CIUDADES = {
    0: '', 
    1: ('Melbourne', 20), 
    2: ('Montevideo', 100), 
    3: ('Rivera', 20), 
    4: ('Maldonado', 20), 
    5: ('Bs As', 20), 
    6: ('Cordoba', 20), 
    7: '',
    8: ('Tokio', 20), 
    9: ('Fuji', 20), 
    10: ('Rio', 100), 
    11: ('San Pablo', 300), 
    12: ('Paris', 200), 
    13: ('Versace', 100), 
    14: '',
    15: ('Barcelona', 20), 
    16: ('Madrid', 20), 
    17: ('Valencia', 20), 
    18: ('Nueva York', 100), 
    19: ('Florida', 200), 
    20: ('Brisbane', 200), 
    21: '',
    22: ('Sidney', 20), 
    23: ('Ginebra', 20), 
    24: ('Berna', 200), 
    25: ('Hamburgo', 100), 
    26: ('Berlin', 150), 
    27: ('Munich', 300)
}

# Casillas
POSICION_CASILLA_INICIO     = [50, 750]
POSICION_CASILLA_RANDOM     = [50, 50]
POSICION_CASILLA_CARCEL     = [750, 50]
POSICION_CASILLA_SUBASTA    = [750, 750]

CANTIDAD_JUGADORES  = [2, 3, 4, 6]
CANTIDAD_NETOS      = [2000, 4000, 7000]
CANTIDAD_SALARIOS   = [200, 300, 400]
DINERO_INICIAL      = 1000

# Escalas
ESCALA_NORMAL   = (200, 50)
ESCALA_MEDIANA  = (100, 50)
ESCALA_INTER    = (100, 30)
ESCALA_PEQUE    = (50, 30)

# Fuentes, Tamaño fuente -> TF
FUENTE_PRINCIPAL    = 'arial'
TF_NORMAL           = 30
TF_MEDIANO          = 20
TF_PEQUE            = 10

# Jugador
MAX_LONGITUD_NOMBRE         = 10
J_DINERO_PREDETERMINADO     = 1000
J_COLOR_PREDETERMINADO      = (0, 0, 0)
J_POSICION_PREDETERMINADO   = (50, 750)

# Paneles
PANEL_MENU          = 0
PANEL_CONFIGURACION = 1
PANEL_INGRESO       = 2
PANEL_PARTIDA       = 3

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CIELO = (0, 53, 138)
VERDE = (0, 200, 0)
ROJO = (255, 0, 0)

CYAN_OSCURO = (0, 38, 24)
VERDE_OSCURO = (17, 89, 6)
AZUL_OSCURO = (0, 51, 89)
ROJO_OSCURO = (196, 12, 12)

COLOR_JUGADORES = [ROJO, AZUL, VERDE, CYAN_OSCURO, BLANCO]