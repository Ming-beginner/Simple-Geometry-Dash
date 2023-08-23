import pygame
import random
from settings import *
from pygame.math import Vector2
from pygame.draw import rect


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.transform.scale(
            pygame.image.load(PLAYER), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(midbottom=pos)
        self.win = False
        self.died = False
        self.on_ground = True
        self.vel = Vector2(0, 0)
        self.offset = 100
        self.jump_amount = 12
        self.particles = []
        self.angle = 0

    def blit_rotate(self, surf, angle: float, pos, originpos):
        # get a rotated image
        w, h = TILE_SIZE, TILE_SIZE
        box = [Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]

        # make sure the player does not overlap, uses a few lambda functions(new things that we did not learn about number1)
        min_box = (min(box_rotate, key=lambda p: p[0])[
                   0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[
                   0], max(box_rotate, key=lambda p: p[1])[1])
        # calculate the translation of the pivot
        pivot = Vector2(originpos[0], -originpos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originpos[0] + min_box[0] - pivot_move[0],
                  pos[1] - originpos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        rotated_image = pygame.transform.rotozoom(self.image, angle, 1)
        self.image = rotated_image
        self.rect = self.image.get_rect(topleft=origin)
        # rotate and blit the image
        surf.blit(rotated_image, origin)

    def draw_particle_trail(self, x, y, window, color=(255, 255, 255)):
        """draws a trail of particle-rects in a line at random positions behind the player"""

        self.particles.append(
            [[x - 5, y - 8], [random.randint(0, 25) / 10 - 1, random.choice([0, 0])],
             random.randint(5, 8)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.5
            particle[1][0] -= 0.4
            rect(window, color,
                 ([int(particle[0][0]), int(particle[0][1])], [int(particle[2]) for i in range(2)]))
            if particle[2] <= 0:
                self.particles.remove(particle)

    def jump(self):
        self.vel.y = -self.jump_amount

    def collide(self, yvel, tiles, object=False):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if(object):
                    self.win = True

                elif yvel > 0:
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

    def update(self, window):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.jump()
        if self.rect.bottom >= HEIGHT:
            self.died = True
            pass
        if not self.on_ground:
            self.angle -= 10
            #self.blit_rotate(window, self.angle, self.rect.center, (32, 32))
            self.vel += GRAVITY
            if self.vel.y > 100:
                self.vel.y = 100
        self.rect.top += self.vel.y
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        self.on_ground = False
        self.draw_particle_trail(self.rect.left - 1, self.rect.bottom + 2,
                                 window)

    def draw(self, window):
        window.blit(self.image, self.rect)
