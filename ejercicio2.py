import random

tablero = [" " for _ in range(9)]

def display_board():
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("----------")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("----------")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

def player_move():
    while True:
        move = input("Tu turno (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and tablero[int(move) - 1] == " ":
            tablero[int(move) - 1] = "x"
            break
        else:
            print("Movimiento inválido. Intenta otra vez.")

def computer_move():
    print("Turno de la computadora...")
    posibles = [i for i, val in enumerate(tablero) if val == " "]
    move = random.choice(posibles)
    tablero[move] = "O"

def check_winner(player):
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(tablero[a] == tablero[b] == tablero[c] == player for a,b,c in combos)

def play_game():
    display_board()
    for _ in range(9):
        player_move()
        display_board()
        if check_winner("x"):
            print("¡Ganaste!")
            return
        if " " not in tablero:
            break
        computer_move()
        display_board()
        if check_winner("O"):
            print("¡La computadora ganó!")
            return
    print("¡Empate!")

play_game()
    