import pygame
from settings import *


class SettingButton(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = (WIDTH/2+200, 500)
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(IMAGES["setting_button"]), (125, 125))
        self.rect = self.image.get_rect(center=self.pos)
        self.hovered = False

    def update(self):
        if(self.hovered):
            self.image = pygame.transform.scale(
                pygame.image.load(IMAGES["setting_button"]), (130, 130))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(IMAGES["setting_button"]), (125, 125))
