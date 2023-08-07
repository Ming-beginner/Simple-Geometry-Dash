import pygame
from settings import *


class GreetingText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGES["greeting_text"])
        self.rect = self.image.get_rect(midbottom=(WIDTH/2, 300))
