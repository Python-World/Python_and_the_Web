import random
import sys
import time

import pygame
from numpy import loadtxt
from pygame.locals import *

##################################
# Enter the name of the music file
music_file = "panther.mp3"

##################################


a = input("EASY : 1    HARD : 2 ")
if a == "1":
    g = 10
else:
    g = 1

# Constants for the game
pygame.mixer.init(44100, -16, 2, 4096)
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255)  # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255)  # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255)  # RED
ENEMY_COLOR = pygame.Color(0, 128, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
TOP = (0, -1)
LEFT = (-1, 0)
NONE = (0, 0)

pygame.mixer.music.load(music_file)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# else:
# 	pygame.mixer.music.load('panther.mp3')


# Draws a rectangle for the wall
def draw_wall(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, WALL_COLOR, [pixels, (25, 25)])


# Draws a rectangle for the player
def draw_pacman(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])


# Draws a rectangle for the coin
def draw_coin(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, COIN_COLOR, [pixels, (25, 25)])


def draw_enemy(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, ENEMY_COLOR, [pixels, (WIDTH, HEIGHT)])


# Uitlity functions
def add_to_pos(pos, pos2):
    return (pos[0] + pos2[0], pos[1] + pos2[1])


def pixels_from_points(pos):
    return (pos[0] * WIDTH, pos[1] * HEIGHT)


# Initializing pygame
pygame.init()
screen = pygame.display.set_mode((650, 520), 0, 32)
background = pygame.surface.Surface((650, 520)).convert()


# Initializing variables
layout = loadtxt("layout.txt", dtype=str)
rows, cols = layout.shape
pacman_position = (1, 1)
background.fill((0, 0, 0))
enemy_pos1 = (13, 1)
enemy_pos2 = (15, 10)
enemy_pos3 = (11, 13)

wall = []
for col in range(cols):
    for row in range(rows):
        value = layout[row][col]
        pos = (col, row)
        if value == "w":
            wall.append(pos)

coin = []
for col in range(cols):
    for row in range(rows):
        value = layout[row][col]
        pos = (col, row)
        if value == "c":
            coin.append(pos)
coin_len = len(coin)

# Main game loop
gap = 0
score = 0
while True:
    screen.blit(background, (0, 0))
    gap += 1
    move_enemy1 = (0, 0)
    move_enemy2 = (0, 0)
    move_enemy3 = (0, 0)
    if gap % g == 0:
        x = [RIGHT, LEFT, TOP, DOWN]
        move_enemy1 = random.choice(x)
        move_enemy2 = random.choice(x)
        move_enemy3 = random.choice(x)
    e1 = add_to_pos(enemy_pos1, move_enemy1)
    e2 = add_to_pos(enemy_pos2, move_enemy2)
    e3 = add_to_pos(enemy_pos3, move_enemy3)

    if e1 in wall:
        draw_enemy(screen, enemy_pos1)
    else:
        enemy_pos1 = add_to_pos(enemy_pos1, move_enemy1)
        draw_enemy(screen, enemy_pos1)
    if e2 in wall:
        draw_enemy(screen, enemy_pos2)
    else:
        enemy_pos2 = add_to_pos(enemy_pos2, move_enemy2)
        draw_enemy(screen, enemy_pos2)
    if e3 in wall:
        draw_enemy(screen, enemy_pos3)
    else:
        enemy_pos3 = add_to_pos(enemy_pos3, move_enemy3)
        draw_enemy(screen, enemy_pos3)

    move_direction = NONE
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_direction = RIGHT
                pac_pos = add_to_pos(pacman_position, move_direction)

                for col in range(cols):
                    for row in range(rows):
                        value = layout[pac_pos[1]][pac_pos[0]]
                        if value in (".", "c"):
                            move_direction = RIGHT
                        else:
                            move_direction = NONE

            if event.key == pygame.K_LEFT:
                move_direction = LEFT
                pac_pos = add_to_pos(pacman_position, move_direction)

                for col in range(cols):
                    for row in range(rows):
                        value = layout[pac_pos[1]][pac_pos[0]]
                        if value in (".", "c"):
                            move_direction = LEFT
                        else:
                            move_direction = NONE

            if event.key == pygame.K_UP:
                move_direction = TOP
                pac_pos = add_to_pos(pacman_position, move_direction)

                for col in range(cols):
                    for row in range(rows):
                        value = layout[pac_pos[1]][pac_pos[0]]
                        if value in (".", "c"):
                            move_direction = TOP
                        else:
                            move_direction = NONE

            if event.key == pygame.K_DOWN:
                move_direction = DOWN
                pac_pos = add_to_pos(pacman_position, move_direction)

                for col in range(cols):
                    for row in range(rows):
                        value = layout[pac_pos[1]][pac_pos[0]]
                        if value in (".", "c"):
                            move_direction = DOWN
                        else:
                            move_direction = NONE

    # Draw board from the 2d layout array.
    # In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
    for col in range(cols):
        for row in range(rows):
            value = layout[row][col]
            pos = (col, row)
            if value == "w":
                draw_wall(screen, pos)
            elif value == "c":
                draw_coin(screen, pos)
            elif value == "e":
                draw_enemy(screen, pos)
            if value == "c" and pacman_position == pos:
                layout[row][col] = "."
                score += 10
                coin_len -= 1
    # Draw the player
    draw_pacman(screen, pacman_position)

    # TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
    # Update player position based on movement.
    pacman_position = add_to_pos(pacman_position, move_direction)

    # TODO: Check if player ate any coin, or collided with the wall by using the layout array.
    # player should stop when colliding with a wall
    # coin should dissapear when eating, i.e update the layout array

    # Update the display
    pygame.display.update()

    # Wait for a while, computers are very fast.
    time.sleep(0.01)

    if (
        (pacman_position == enemy_pos1)
        or (pacman_position == enemy_pos2)
        or (pacman_position == enemy_pos3)
        or coin_len == 0
    ):
        pygame.QUIT()

    pygame.display.set_caption("PACMAN  ::  SCORE  " + str(score))
