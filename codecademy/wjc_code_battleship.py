#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

from random import randint

board = []

for i in range(5):
    board.append(["O"] * 5)


def print_board(lists):
    for row in lists:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)

print("Let's play Battleship!")
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    guess_row = int(input('Guess Row: '))
    guess_col = int(input("Guess Col: "))

    print("Ship Row: %s" % ship_row)
    print("Ship Col: %s" % ship_col)

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    elif guess_row == ship_row or guess_col == ship_col:
        print("You guessed that one already.")
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        # elif board[guess_row][guess_col] == "X":
        #     print("You guessed that one already.")
        else:
            print("You missed my battleship! battleship here!")
    board[guess_row][guess_col] = "X"
    print(turn + 1)
    print(print_board(board))
    if turn == 3:
        print("Game Over")
