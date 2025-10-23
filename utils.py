import numpy as np
import random
from jugador import Jugador


#Función para crear una matriz del tamaño que se le pasa como argumento
def crear_tablero(tamanio):
    tablero = np.full((tamanio,tamanio), "_")
    return tablero

#Función para mostrar tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("".join(fila))

#Función que recibe como parametro un jugador y va colocando en su tablero los barcos que recibe de la funcion crear_barcos.
#También los barcos se guardan en el atributo barcos del jugador para ir borandolas mas adelante 
def colocar_barcos(jugador: Jugador):
    tablero = jugador.mi_tablero
    barc = crear_barcos()
    jugador.barcos = barc
    print("barcos de ",jugador.nombre,barc)
    for i in barc:
        for j in i:
            x = j[0]
            y = j[1]
            tablero[x][y] = "O"
    
#Función que simplemente pide al usuario las coordenadas y las devuelve como "x" y "y" 
def disparar():
    coord = input("Introduce las coordenadas donde quieres disparar: ")
    coord = coord.split()
    if len(coord) != 2 and coord[0].isnumeric() == False and coord[1].isnumeric() == False:
        print("Error! Introduce dos numeros separados por un espacio")
    else:
        x = int(coord[0])
        y = int(coord[1])
    return x, y

#Función para crear barcos partiendo de un array de esloras y que devuelva una lista con posiciones de estos barcos
def crear_barcos():
    barcos = []
    esloras = [4, 3, 3, 2, 2, 2]
    for  eslora in esloras:
        added = False
        while added == False:
            b = crear_barco(eslora)
            if b!= None and comprobar_exist(barcos, b) == False:
                barcos.append(b)
                added = True
    return barcos
    
#Función que crea un solo barco de una longitud que recibe como parametro
def crear_barco(long):
    orient = np.random.choice(["V","O"])
    x = np.random.randint(0, 9)
    y = np.random.randint(0, 9)
    barco = []
    if long == 4:
        if orient == "V" and x+3 <= 9:
            barco = [(x,y),(x+1, y), (x+2, y),(x+3, y)]
            return barco
        elif orient == "O" and y+3 <= 9:
            barco = [(x,y),(x, y+1), (x, y+2),(x, y+3)]
            return barco
        else:
            crear_barco(4)
            
    if long == 3:
        if orient == "V" and x+2 <=9:
            barco = [(x,y),(x+1, y), (x+2, y)]
            return barco
        elif orient == "0" and y+2 <= 9:
            barco = [(x,y),(x, y+1), (x, y+2)]
            return barco
        else:
            crear_barco(3)
            
    if long == 2:
        if orient == "V" and x+1 <= 9:
            barco = [(x,y),(x+1, y)]
            return barco
        elif orient == "O" and y+1 <= 9:
            barco = [(x,y),(x,y+1)]
            return barco
        else:
            crear_barco(2)
            
#Función que recibe un array de barcos y unas coordenadas de una casilla ,
#busca esta casilla en todos los barcos y la borra 
# o borra el barco entero en el caso de que haya solo esta casilla
def borrar_casilla(barcos, b):
    ultima =False
    for i, barco in enumerate(barcos):
        if b in barco and len(barco) >1:
            barco.remove(b)
            ultima = False
        elif b in barco and len(barco) == 1:
            barcos.remove(barco)
            ultima = True
    return ultima
            
#Función que recibe la lista de los barcos y un barco, 
# busca este barco en la lista y devuelve True si lo encuentra
def comprobar_exist(barcos, b):
    if b in barcos:
        return True
    for bb in barcos:
        for casilla in b:
            if casilla in bb:
                return True
    return False


#Función para preparar los jugadores con sus tableros
def preparar_juego():
    name1 = input("Introduce tu nombre ")
    name2 = "Capitan MAC"
    tablero1 = crear_tablero(10)
    tablero2 = crear_tablero(10)
    tablero3 = crear_tablero(10)
    tablero4 = crear_tablero(10)
    
    jugador1 = Jugador(name1, tablero1, tablero2)
    
    jugador2 = Jugador(name2, tablero3, tablero4)
    
    return jugador1, jugador2