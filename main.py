DIV = "------------"
positions = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
board = (f"{positions[0]}|{positions[1]}|{positions[2]}\n{DIV}\n"
         f"{positions[3]}|{positions[4]}|{positions[5]}\n{DIV}\n"
         f"{positions[6]}|{positions[7]}|{positions[8]}")
player_1 = "X"
player_2 = "O"
GAME_ON = True
CURRENT_PLAYER = player_1

def print_board(positions):
    board = (f"{positions[0]}|{positions[1]}|{positions[2]}\n{DIV}\n"
             f"{positions[3]}|{positions[4]}|{positions[5]}\n{DIV}\n"
             f"{positions[6]}|{positions[7]}|{positions[8]}")
    print(board)


def place_mark(player):
    while True:
        position = int(input(
            f"You got {player}, please indicate where you would like to place the {player}, position 1-9 from left to right, top to bottom.\n"))
        if position in range(1, 10) and positions[position - 1] == "   ":
            break
        else:
            print("This spot is not available, choose again.")
    positions[position - 1] = f" {player} "
    print_board(positions)


def switch_player():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == player_1:
        CURRENT_PLAYER = player_2
    elif CURRENT_PLAYER == player_2:
        CURRENT_PLAYER = player_1


def is_full():
    global GAME_ON
    if "   " not in positions:
        print("The board is full, game over.")
        GAME_ON = False


def is_winning():
    global GAME_ON, CURRENT_PLAYER
    if (positions[0] == positions[1] == positions[2] != "   " or
            positions[0] == positions[3] == positions[6] != "   " or
            positions[3] == positions[4] == positions[5] != "   " or
            positions[1] == positions[4] == positions[7] != "   " or
            positions[6] == positions[7] == positions[8] != "   " or
            positions[2] == positions[5] == positions[8] != "   " or
            positions[0] == positions[4] == positions[8] != "   " or
            positions[2] == positions[4] == positions[6] != "   "):
        winner = CURRENT_PLAYER
        print(f"The winner is {winner}.")
        GAME_ON = False


print("Welcome to tic tac toe!")
print_board(positions)

while GAME_ON:
    place_mark(CURRENT_PLAYER)
    is_full()
    is_winning()
    switch_player()

