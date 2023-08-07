import pygame


class LevelButton(pygame.sprite.Sprite):
    def __init__(self, level, isOpen):
        super().__init__()
        self.level = level
        self.isOpen = isOpen
