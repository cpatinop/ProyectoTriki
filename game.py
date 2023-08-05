tablero = ["  " for i in range(9)]

def print_tablero():
    row1 ="| {} | {}  |{}  |".format(tablero[0], tablero[1],tablero[2])
    row2 ="| {} | {}  |{}  |".format(tablero[3], tablero[4],tablero[5])
    row3 ="| {} | {}  |{}  |".format(tablero[6], tablero[7],tablero[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def  mov_player(icono):
    if icono == "X":
        numero = 1
    elif icono == "O":
        numero =2
    print("Tu turno jugador {}".format(numero))
    elige =  int (input("Elige tu moviemiento (1-9):   ").strip())
    if tablero[elige -1] == "  ":
        tablero[elige -1] = icono
    else:
        print()
        print("Ese espacio esta ocupado") 

def es_empate ():
    if "  " not in tablero:
        return True
    else:
        return False

def es_victoria (icono):
    if  (tablero[0] == icono and tablero[1] == icono and tablero[2] == icono) or \
        (tablero[3] == icono and tablero[4] == icono and tablero[5] == icono) or \
        (tablero[6] == icono and tablero[7] == icono and tablero[8] == icono) or \
        (tablero[0] == icono and tablero[3] == icono and tablero[6] == icono) or \
        (tablero[1] == icono and tablero[4] == icono and tablero[7] == icono) or \
        (tablero[2] == icono and tablero[5] == icono and tablero[8] == icono) or \
        (tablero[0] == icono and tablero[4] == icono and tablero[8] == icono) or \
        (tablero[2] == icono and tablero[4] == icono and tablero[6] == icono):
            return True
    else:
        return False



while True: 
    print_tablero()
    mov_player("X")
    print_tablero()
    if es_victoria("X"):
        print(" X es el ganador")
        break
    elif es_empate():
        print("Esto es empate")
        break
    mov_player("O")
    if es_victoria("O"):
        print_tablero()
        print(" O es el ganador")
        break
    elif es_empate():
        print("Esto es empate")
        break
