import math
import sys
from tkinter import *

import numpy as np
import pygame

BLACK = (33, 33, 33)
GREY = (235, 235, 235)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

player_names = []


# adding players
def submit():
    player_names.append(player_one.get())
    player_names.append(player_two.get())
    root.destroy()


# creating connect 4 board 6 X 7 common board size
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                screen,
                BLACK,
                (
                    c * SQUARESIZE,
                    r * SQUARESIZE + SQUARESIZE,
                    SQUARESIZE,
                    SQUARESIZE,
                ),
            )
            pygame.draw.circle(
                screen,
                GREY,
                (
                    int(c * SQUARESIZE + SQUARESIZE / 2),
                    int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                ),
                RADIUS,
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        height - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )
            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        height - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )
    pygame.display.update()


try:
    root = Tk()
    root.resizable(0, 0)
    player_one = StringVar(master=root)
    player_two = StringVar(master=root)
    root.geometry("500x300")
    root.title("Connect 4 Game")
    Label(
        master=root, text="Connect 4 Game", font=("Poppins", 30, "normal")
    ).place(x=80, y=20)
    Label(master=root, text="Enter player 1 name: ").place(x=120, y=100)
    Entry(
        master=root, textvariable=player_one, font=("calibre", 10, "normal")
    ).place(x=250, y=100)
    Label(master=root, text="Enter player 2 name: ").place(x=120, y=140)
    Entry(
        master=root, textvariable=player_two, font=("calibre", 10, "normal")
    ).place(x=250, y=140)
    Button(master=root, text="ADD", width=10, command=submit).place(
        x=210, y=190
    )
    root.mainloop()

    if player_names[0] != "" and player_names[1] != "":
        board = create_board()

        game_over = False
        turn = 0

        pygame.init()

        SQUARESIZE = 100

        width = COLUMN_COUNT * SQUARESIZE
        height = (ROW_COUNT + 1) * SQUARESIZE

        size = (width, height)

        RADIUS = int(SQUARESIZE / 2 - 5)

        screen = pygame.display.set_mode(size)
        draw_board(board)
        pygame.display.update()

        myfont = pygame.font.SysFont("monospace", 30)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, GREY, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(
                            screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS
                        )
                    else:
                        pygame.draw.circle(
                            screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS
                        )
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, GREY, (0, 0, width, SQUARESIZE))

                    # Ask for Player 1 Input
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARESIZE))

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 1)
                            turn += 1
                            turn = turn % 2

                            if winning_move(board, 1):
                                label = myfont.render(
                                    player_names[0] + " wins the game", 1, RED
                                )
                                screen.blit(label, (40, 10))
                                game_over = True

                    # # Ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARESIZE))

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 2)
                            turn += 1
                            turn = turn % 2

                            if winning_move(board, 2):
                                label = myfont.render(
                                    player_names[1] + " wins the game",
                                    1,
                                    YELLOW,
                                )
                                screen.blit(label, (40, 10))
                                game_over = True

                    draw_board(board)

                    if game_over:
                        pygame.time.wait(3000)

except IndexError:
    print("Game closed")
