import pygame
from settings import * 
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.transform.scale(
            pygame.image.load(PLAYER), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(midbottom=pos)
        self.win = False
        self.died = False
        self.on_ground = False
        self.vel = Vector2(0, 0)
        self.offset = 100
        self.jump_amount = 12

    def jump(self):
        self.vel.y = -self.jump_amount

    def collide(self, yvel, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if yvel > 0:
                    self.rect.bottom = tile.rect.top
                    self.vel.y = 0
                    self.on_ground = True
                elif yvel < 0:
                    self.rect.top = tile.rect.bottom
                    self.died = True
                else:
                    self.vel.x = 0
                    self.rect.right = tile.rect.left
                    self.died = True

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.jump()
        if self.rect.bottom >= HEIGHT:
            self.died = True
        if not self.on_ground:
            self.vel += GRAVITY
            if self.vel.y > 100:
                self.vel.y = 100
        self.rect.top += self.vel.y
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        self.on_ground = False

    def draw(self, window):
        window.blit(self.image, self.rect)