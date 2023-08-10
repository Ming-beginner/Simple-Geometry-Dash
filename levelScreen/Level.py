import pygame
from support import import_csv_layout
from pytmx.util_pygame import load_pygame
from settings import *
from math import sqrt

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
    
    def update(self):
        self.rect.x -= 10

class Level:
    def __init__(self, data, groups):
        self.path = data["terrain"]
        tmx_data = load_pygame(self.path)
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    if surf:
                        pos = (x*64, y*64+HEIGHT-TILE_SIZE*VERTICLE_TILE_NUMBER+64)
                        Tile(pos = pos, surf = surf, groups =  groups)
        
    def run(self):

        pass
