from settings import *
import pygame

class SettingButton(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = (WIDTH/2+200, 500)
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(IMAGES["setting_button"]), (110, 110))
        self.rect = self.image.get_rect(center=self.pos)
        self.hovered = False

    def update(self):
        if(self.hovered):
            self.pos = (WIDTH/2+200 - 10, 500 - 10)
            self.image = pygame.transform.scale(pygame.image.load(IMAGES["setting_button"]), (115, 115))
        else:
            self.pos = (WIDTH/2+200 - 10, 500 - 10)
            self.image = pygame.transform.scale(pygame.image.load(IMAGES["setting_button"]), (110, 110))
