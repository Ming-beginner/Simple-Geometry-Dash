import pygame
from settings import SOUNDS
from random import randint


def click(rect):
    return pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos())


def play_bg_music():
    pygame.mixer.music.load(SOUNDS[2])
    pygame.mixer.music.play(-1)
