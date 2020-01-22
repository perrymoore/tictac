def display_board(board):
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("\n" * 2)

def player_input():
    xOro = ''
    while not xOro == 'x' or xOro == 'o':
        xOro = input("Will you be X or O?: ").upper()
        if xOro == 'X':
            return ('X', 'O')
            break
        elif xOro == 'O':
            return ('O', 'X')
            break
        else:
            continue


def place_marker(board, xOro, spot):
    board[spot] = xOro


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' ' or board[position] == ''


def full_board_check(board):
    for marker in board:
        if ' ' in board or '' in board:
            return False
        else:
            return True


def player_choice(board):
    spot = 0
    while spot not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        spot = int(input("Enter your next position: "))
        if space_check(board, spot):
            return spot
        else:
            return 'Already full try another'

def replay():
    return input('Play again?: (Yes or No) ').lower() == "yes"


print("Welcome to Tic Tac Toe!")
while True:
    game_board = [' ']*10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to play? (Yes or No): ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_mark, position)
            if win_check(game_board,player1_mark):
                display_board(game_board)
                print("Player 1 Wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    print("Draw, play again!")
                    game_on = False
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_mark, position)
            if win_check(game_board, player2_mark):
                display_board(game_board)
                print("Player 2 Wins!")
            else:
                if full_board_check(game_board):
                    print("Draw, play again!")
                    game_on = False
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break