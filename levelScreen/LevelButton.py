import pygame
from math import ceil
from settings import *


class LevelButton(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = pygame.image.load(IMAGES["level_button"]).convert_alpha()
        self.font = pygame.font.Font(FONT, 80)
        self.rect = self.image.get_rect(
            center=(WIDTH/2+250*level-ceil(len(LEVELS)/2)*250, HEIGHT/2))
        self.level = self.font.render(str(level), False, "#ffffff")
        self.level_rect = self.level.get_rect(
            center=(self.rect.w/2, self.rect.h/2))

    def draw(self, window):
        self.image.blit(self.level, self.level_rect)
        window.blit(self.image, self.rect)
