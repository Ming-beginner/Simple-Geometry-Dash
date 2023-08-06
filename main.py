import pygame
import sys
from settings import *


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("hello")
            running = False
            sys.exit()
    screen.fill("#ffffff")
    pygame.display.update()
    clock.tick(FPS)
