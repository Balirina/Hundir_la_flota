![alt text](./battleship.jpg "Battleship")
# Hundir la Flota en Python 🚢

Este proyecto implementa el clásico juego de mesa **Hundir la Flota** utilizando el lenguaje de programación Python, separando la lógica del tablero, los barcos y la interacción.

### 1. `Jugador` ⚓

* **Propósito:** Es la clase de **modelo de datos** para una embarcación individual.
* **Responsabilidad:** Almacena el **nombre** del jugador, una lista de los barcos con las **posiciones exactas** que ocupa en el tablero, otra lista que refleja **su tablero** con los barcos colocados y otra lista que refleja **el tablero del rival**. Mantiene un registro de los **intentos anteriores** para mostrar un aviso cuando se intenta disparar en las **mismas coordenadas**.

### 2. `Utils` 💥

* **Propósito:** Es el fichero donde se guardan todas las **funciones** de las que se hace uso en este proyecto.
* **Funciones:**

(`(crear_tablero)`) - crea un tablero teniendo en calculo el tamaño

(`(mostrar_tablero)`) - función para imprimir el tablero

(`(colocar_barcos)`) - funcion que recibe como parametro unn jugador y va colocando en su tablero los barcos que recibe de la función crear barcos. También los barcos se guardan en el atributo barcos del jugador para ir borandolas mas adelante.

(`(disparar)`) - función que simplemente pide al usuario las coordenadas y las devuelve como un **x** y una **y**.

(`(crear_barcos)`) - función para crear barcos partiendo de un array de esloras y que devuelva una lista con posiciones de estos barcos

(`(crear_barco)`) - función que crea un solo barco de una longitud que recibe como parametro

(`(borrar_castilla)`) - función que recibe un array de barcos y unas coordenadas de una casilla, busca esta casilla en todos los barcos y la borra o borra el barco entero en el caso de que este barco solo tiene esta casilla.

(`(comprobar_exist)`) - función que recibe la lista de los barcos y un barco, busca este barco en la lista y devuelve True si lo encuentra

(`(preparar_juego)`) - función para preparar los jugadores con sus tableros


## Flujo Principal del Juego

1.  Se solicita el nombre del jugador y se inicializan cuatro  **`tableros`** (dos para el jugador y dos para la máquina).
2.  Un tablero de cada jugador se puebla con barcos de manera aleatoria.
3.  El juego entra en un bucle de turnos:
    * El jugador crea un **`Disparo`** con coordenadas válidas.
    * El disparo se aplica al **`Tablero`** de la máquina, y se guarda en la variable **barcos** del jugador.
    * La máquina genera un **`Disparo`** aleatorio.
    * El disparo se aplica al **`Tablero`** del jugador, que devuelve el resultado.
4.  La partida continúa mientras hayan barcos de la maquina o del jugador. Una vez que se han hundido todos los barcos de algun jugador el juego finaliza y se declara un ganador.
