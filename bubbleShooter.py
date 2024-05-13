#0 - start menu and 1 - gameover 2-in game 3 - store
import pygame
import random
import math

pygame.init()
win = pygame.display.set_mode((600, 700))
pygame.display.set_captain("PyShooter")
clock = pygame.time.Clock()

run = True

player_balls = []
balls = []
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
temp = []

score = 0
moves = 40
restart_btn = pygame.Rect(200, 400, 150, 75)

game_state = 2

class Ball():
    def __init__(self, x, y, color, Type):
        self.x = x
        self.y = y
        self.color = color
        self.x_vel = 0
        self.y_vel = 0
        self.type = Type