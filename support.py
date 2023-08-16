import pygame
from settings import SOUNDS
from random import randint


def click(rect):
    return pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos())


def play_bg_music():
    pygame.mixer.music.load(
        SOUNDS[randint(0, len(SOUNDS))])
    pygame.mixer.music.play(-1)
