import random
import sys
from math import *

import pygame

pygame.init()

width = 600
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong!")
clock = pygame.time.Clock()

background = (27, 38, 49)
white = (236, 240, 241)
red = (203, 67, 53)
blue = (52, 152, 219)
yellow = (244, 208, 63)

top = white
bottom = white
left = white
right = white

margin = 4

scoreLeft = 0
scoreRight = 0
maxScore = 20

font = pygame.font.SysFont("Small Fonts", 30)
largeFont = pygame.font.SysFont("Small Fonts", 60)


# Draw the Boundary of Board
def boundary():
    global top, bottom, left, right
    pygame.draw.rect(display, left, (0, 0, margin, height))
    pygame.draw.rect(display, top, (0, 0, width, margin))
    pygame.draw.rect(display, right, (width - margin, 0, margin, height))
    pygame.draw.rect(display, bottom, (0, height - margin, width, margin))

    l = 25

    pygame.draw.rect(display, white, (width / 2 - margin / 2, 10, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 60, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 110, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 160, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 210, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 260, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 310, margin, l))
    pygame.draw.rect(display, white, (width / 2 - margin / 2, 360, margin, l))


# Paddle Class
class Paddle:
    def __init__(self, position, color):
        self.w = 10
        self.h = self.w * 8
        self.paddleSpeed = 6

        if position == -1:
            self.x = 1.5 * margin
        else:
            self.x = width - 1.5 * margin - self.w

        self.y = height / 2 - self.h / 2

    # Show the Paddle
    def show(self, color):
        pygame.draw.rect(display, color, (self.x, self.y, self.w, self.h))

    # Move the Paddle
    def move(self, ydir):
        self.y += self.paddleSpeed * ydir
        if self.y < 0:
            self.y -= self.paddleSpeed * ydir
        elif self.y + self.h > height:
            self.y -= self.paddleSpeed * ydir


leftPaddle = Paddle(-1, red)
rightPaddle = Paddle(1, blue)


# Ball Class
class Ball:
    def __init__(self, color):
        self.r = 20
        self.x = width / 2 - self.r / 2
        self.y = height / 2 - self.r / 2
        self.color = color
        self.angle = random.randint(-75, 75)
        if random.randint(0, 1):
            self.angle += 180

        self.speed = 8

    # Show the Ball
    def show(self):
        pygame.draw.ellipse(
            display, self.color, (self.x, self.y, self.r, self.r)
        )

    # Move the Ball
    def move(self):
        global scoreLeft, scoreRight
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))
        if self.x + self.r > width - margin:
            scoreLeft += 1
            self.angle = 180 - self.angle
        if self.x < margin:
            scoreRight += 1
            self.angle = 180 - self.angle
        if self.y < margin:
            self.angle = -self.angle
        if self.y + self.r >= height - margin:
            self.angle = -self.angle

    # Check and Reflect the Ball when it hits the padddle
    def checkForPaddle(self):
        if self.x < width / 2:
            if leftPaddle.x < self.x < leftPaddle.x + leftPaddle.w:
                if (
                    leftPaddle.y < self.y < leftPaddle.y + 10
                    or leftPaddle.y < self.y + self.r < leftPaddle.y + 10
                ):
                    self.angle = -45
                if (
                    leftPaddle.y + 10 < self.y < leftPaddle.y + 20
                    or leftPaddle.y + 10 < self.y + self.r < leftPaddle.y + 20
                ):
                    self.angle = -30
                if (
                    leftPaddle.y + 20 < self.y < leftPaddle.y + 30
                    or leftPaddle.y + 20 < self.y + self.r < leftPaddle.y + 30
                ):
                    self.angle = -15
                if (
                    leftPaddle.y + 30 < self.y < leftPaddle.y + 40
                    or leftPaddle.y + 30 < self.y + self.r < leftPaddle.y + 40
                ):
                    self.angle = -10
                if (
                    leftPaddle.y + 40 < self.y < leftPaddle.y + 50
                    or leftPaddle.y + 40 < self.y + self.r < leftPaddle.y + 50
                ):
                    self.angle = 10
                if (
                    leftPaddle.y + 50 < self.y < leftPaddle.y + 60
                    or leftPaddle.y + 50 < self.y + self.r < leftPaddle.y + 60
                ):
                    self.angle = 15
                if (
                    leftPaddle.y + 60 < self.y < leftPaddle.y + 70
                    or leftPaddle.y + 60 < self.y + self.r < leftPaddle.y + 70
                ):
                    self.angle = 30
                if (
                    leftPaddle.y + 70 < self.y < leftPaddle.y + 80
                    or leftPaddle.y + 70 < self.y + self.r < leftPaddle.y + 80
                ):
                    self.angle = 45
        else:
            if rightPaddle.x + rightPaddle.w > self.x + self.r > rightPaddle.x:
                if (
                    rightPaddle.y < self.y < leftPaddle.y + 10
                    or leftPaddle.y < self.y + self.r < leftPaddle.y + 10
                ):
                    self.angle = -135
                if (
                    rightPaddle.y + 10 < self.y < rightPaddle.y + 20
                    or rightPaddle.y + 10
                    < self.y + self.r
                    < rightPaddle.y + 20
                ):
                    self.angle = -150
                if (
                    rightPaddle.y + 20 < self.y < rightPaddle.y + 30
                    or rightPaddle.y + 20
                    < self.y + self.r
                    < rightPaddle.y + 30
                ):
                    self.angle = -165
                if (
                    rightPaddle.y + 30 < self.y < rightPaddle.y + 40
                    or rightPaddle.y + 30
                    < self.y + self.r
                    < rightPaddle.y + 40
                ):
                    self.angle = 170
                if (
                    rightPaddle.y + 40 < self.y < rightPaddle.y + 50
                    or rightPaddle.y + 40
                    < self.y + self.r
                    < rightPaddle.y + 50
                ):
                    self.angle = 190
                if (
                    rightPaddle.y + 50 < self.y < rightPaddle.y + 60
                    or rightPaddle.y + 50
                    < self.y + self.r
                    < rightPaddle.y + 60
                ):
                    self.angle = 165
                if (
                    rightPaddle.y + 60 < self.y < rightPaddle.y + 70
                    or rightPaddle.y + 60
                    < self.y + self.r
                    < rightPaddle.y + 70
                ):
                    self.angle = 150
                if (
                    rightPaddle.y + 70 < self.y < rightPaddle.y + 80
                    or rightPaddle.y + 70
                    < self.y + self.r
                    < rightPaddle.y + 80
                ):
                    self.angle = 135


# Show the Score
def showScore():
    leftScoreText = font.render("Score : " + str(scoreLeft), True, red)
    rightScoreText = font.render("Score : " + str(scoreRight), True, blue)

    display.blit(leftScoreText, (3 * margin, 3 * margin))
    display.blit(rightScoreText, (width / 2 + 3 * margin, 3 * margin))


# Game Over
def gameOver():
    if maxScore in (scoreLeft, scoreRight):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_r:
                        reset()
            if scoreLeft == maxScore:
                playerWins = largeFont.render(
                    "Red wins!Press R to reset!", True, red
                )
                display.blit(playerWins, (40, height / 2))
            elif scoreRight == maxScore:
                playerWins = largeFont.render(
                    "Blue wins! Press R to reset!", True, blue
                )
                display.blit(playerWins, (30, height / 2))
            pygame.display.update()


def reset():
    global scoreLeft, scoreRight
    scoreLeft = 0
    scoreRight = 0
    board()


def close():
    pygame.quit()
    sys.exit()


def board():
    loop = True
    leftChange = 0
    rightChange = 0
    ball = Ball(yellow)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()  # add pause functionality after here if possible
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_w:
                    leftChange = -1
                if event.key == pygame.K_s:
                    leftChange = 1
                if event.key == pygame.K_UP:
                    rightChange = -1
                if event.key == pygame.K_DOWN:
                    rightChange = 1
            if event.type == pygame.KEYUP:
                leftChange = 0
                rightChange = 0

        leftPaddle.move(leftChange)
        rightPaddle.move(rightChange)
        ball.move()
        ball.checkForPaddle()

        display.fill(background)
        showScore()

        ball.show()
        leftPaddle.show(red)
        rightPaddle.show(blue)

        boundary()

        gameOver()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    board()
