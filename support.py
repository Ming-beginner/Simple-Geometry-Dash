import pygame
from os.path import join
from settings import SOUNDS
# from random import randint


def click(rect):
    return pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos())


def play_bg_music():
    pygame.mixer.music.load(SOUNDS[2])
    pygame.mixer.music.play(-1)

def get_image(dir):
    pass
    
def load_button_image(name):
    fullname = join('graphics', 'buttons', name)
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map