import utils as fn 
import random

print("Bienvenidos a la batalla de las naves")

jugador1, jugador2 = fn.preparar_juego()

fn.colocar_barcos(jugador1)
fn.colocar_barcos(jugador2)
jugador1.intentos = []
jugador2.intentos = []
print(jugador1.mi_tablero)
print(45*"∞")
print(jugador2.mi_tablero)

turno = 1

while len(jugador1.barcos) > 0 and len(jugador2.barcos) > 0:
    if(turno == 1):
        #dispara el primero
        x, y = fn.disparar()
        b = (x, y)
        if b not in jugador1.intentos:
            jugador1.intentos.append(b)
            if jugador2.mi_tablero[x][y] == "O":
                jugador1.tablero_rival[x][y] = "X"
                jugador2.mi_tablero[x][y] = "X"
                #b =(x, y)
                ultima = fn.borrar_casilla(jugador2.barcos, b)
                if ultima == True:
                    print("Hundido")
                    #marcar con agua alrededor
                else:
                    print("Tocado")
                print(jugador1.tablero_rival)
                
                turno = 1
            else:
                print("Agua")
                jugador1.tablero_rival[x][y] = "*"
                jugador2.mi_tablero[x][y] = "*"
                print(jugador1.tablero_rival)
                turno = 2

        else:
            print("Ya has intentado con estas coordenadas")
            
        
    else:
        #dispara la maquina
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if jugador1.mi_tablero[x][y] == "O":
            jugador2.tablero_rival[x][y] = "X"
            jugador1.mi_tablero[x][y] = "X"
            print("El Capitan MAC ha disparado tu barco en posición ",x, "y", y)
            b =(x, y)
            fn.borrar_casilla(jugador1.barcos, b)
            print(jugador2.tablero_rival)
            turno = 2
        else:
            jugador2.tablero_rival[x][y] = "*"
            jugador1.mi_tablero[x][y] = "*"
            print("El Capitan MAC ha disparado al agua")
            print(jugador2.tablero_rival)
            turno = 1
            
        
if jugador1.barcos == 0:
    print("El Capitan MAC ha ganado")
else:
    print("Felicidades",jugador1.nombre, "Has ganado!")
