### Importando modulos
import random


### Constantes
LINEAS_MAX = 3
APUESTA_MAX = 100
APUESTA_MIN = 1

ROWS = 3
COLS = 3

### Recuento de simbolos
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


### Funcion para obtener las vueltas de la maquina
def obtener_vuelta_maquina(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



## Funcion que permite depositar el monto
def deposito():
    while True:
        monto = input("Cuanto te gustaria depositar? $")
        if monto.isdigit(): #verificamos de que el monto sea un digito, sino se convierte
            monto = int(monto)
            if monto > 0:
                break
            else:
                print("El monto debe ser mayor a 0 (cero).")
        else:
            print("Porfavor ingrese un numero.")

    return monto



## funcion que obtiene el numero de lineas sobre las que va a apostar el jugador
def obtener_numero_de_lineas():
    while True:
        lineas = input("Ingrese la cantidad de lineas a apostar (1-" + str(LINEAS_MAX) + ")? ")
        if lineas.isdigit(): #verificamos de que la cantidad sea un digito, sino se convierte
            lineas = int(lineas)
            if 1 <= lineas <= LINEAS_MAX:
                break
            else:
                print("Ingrese un numero valido de Lineas")
        else:
            print("Porfavor ingrese un numero.")

    return lineas



## funcion que obtiene la apuesta establecida 
def obtener_apuesta():
    while True:
        monto = input("Cuanto te gustaria Apostar en cada linea? $")
        if monto.isdigit(): #erificamos de que el monto sea un digito, sino se convierte
            monto = int(monto)
            if APUESTA_MIN <=monto <=APUESTA_MAX:
                break
            else:
                print(f"El monto debe ser entre ${APUESTA_MIN} - ${APUESTA_MAX}")
        else:
            print("Porfavor ingrese un numero.")

    return monto

def spin(balance):
    lineas = obtener_numero_de_lineas()
    while True:
        apuesta = obtener_apuesta()
        apuesta_total = apuesta * lineas

        if apuesta_total > balance:
            print(f"No tenes suficiente Balance para apostar, tu Balance actual es: ${balance}")
        else:
            break

    print(f"Estas apostando ${apuesta} en {lineas} Lineas. La apuesta total es igual a: ${apuesta_total}")
  
    slots = obtener_vuelta_maquina(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lineas, apuesta, symbol_value)
    print(f"Your Won ${winnings}.")
    print(f"Your Won on lines:", *winning_lines)
    return winnings - apuesta_total



### FUNCION PRINCIPAL ###
def main():
    balance = deposito()
    while True:
        print(f"Su Balance actual es de ${balance}")
        answer = input("Presiona enter para jugar (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

## LLamando a la funcion principal
main()