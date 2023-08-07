import pygame
from settings import *


class PlayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = (WIDTH/2, 500)
        self.image = pygame.transform.scale(
            pygame.image.load(IMAGES["play_button"]), (200, 200))
        self.rect = self.image.get_rect(center=self.pos)
        self.hovered = False
        self.show = True

    def update(self):
        if(self.hovered and self.show):
            self.image = pygame.transform.scale(
                pygame.image.load(IMAGES["play_button"]), (210, 210))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(IMAGES["play_button"]), (200, 200))
