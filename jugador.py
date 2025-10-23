'''
Clase jugador para poder guardar:
su nombre,
su tablero con los barcos colocados,
el tablero del rival,
una lista con los barcos
y una lista con los intentos que ha hecho, para no dejar que un jugador introduzca dos veces las mismas coordenadas

'''
class Jugador:
    nombre: str
    mi_tablero = list()
    tablero_rival = list()
    barcos =list()
    intentos = list()
    
    def __init__(self, nombre, mi_tab, tab_riv):
        self.nombre = nombre
        self.mi_tablero = mi_tab
        self.tablero_rival = tab_riv
        