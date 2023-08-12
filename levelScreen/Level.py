import pygame
from support import click
from pytmx.util_pygame import load_pygame
from settings import *
from pygame.math import Vector2
from settingScreen.Screen import SettingScreen


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            surf.convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.rect.x -= 5


class Object(Tile):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.image = surf.convert_alpha()


class PauseScreen(SettingScreen):
    def __init__(self):
        super().__init__()
        self.home_button = pygame.transform.scale(pygame.image.load(
            IMAGES["home_button"]).convert_alpha(), (100, 100))
        self.home_button_rect = self.home_button.get_rect(
            midbottom=(WIDTH/2-100, HEIGHT*5/6))
        self.play_button = pygame.transform.scale(pygame.image.load(
            IMAGES["play_button"]).convert_alpha(), (100, 100))
        self.play_button_rect = self.play_button.get_rect(
            midbottom=(WIDTH/2+100, HEIGHT*5/6))
        self.return_home = False

    def draw(self, window):
        if(self.show):
            window.blit(self.surface, (WIDTH/6, HEIGHT/6))
            window.blit(self.volume_surf, self.volume_rect)
            window.blit(self.text_surf, self.text_rect)
            window.blit(self.play_button, self.play_button_rect)
            window.blit(self.home_button, self.home_button_rect)
            window.blit(self.increase_volume_button_surf,
                        self.increase_volume_button_rect)
            window.blit(self.decrease_volume_button_surf,
                        self.decrease_volume_button_rect)
            if click(self.increase_volume_button_rect):
                self.increase_volume()
            elif click(self.decrease_volume_button_rect):
                self.decrease_volume()
            elif click(self.play_button_rect):
                self.show = False
                pygame.mixer.music.unpause()
            elif click(self.home_button_rect):
                self.return_home = True
                self.show = False
                pygame.mixer.music.stop()


class SumarizeScreen(SettingScreen):
    def __init__(self, result):
        super().__init__()
        self.win = result == "win"


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
        self.jump_amount = 16

    def jump(self):
        self.vel.y = -self.jump_amount

    def collide(self, yvel, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                print(yvel)
                if yvel > 0:
                    self.rect.bottom = tile.rect.top
                    self.vel.y = 0
                    self.on_ground = True
                elif yvel < 0:
                    self.rect.top = tile.rect.bottom
                else:
                    self.vel.x = 0
                    self.rect.right = tile.rect.left

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.jump()
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.on_ground = True
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


class Level(pygame.sprite.Sprite):
    def __init__(self, data):
        self.path = data["terrain"]
        self.tile_group = pygame.sprite.Group()
        self.surface = pygame.transform.scale(
            pygame.image.load(IMAGES["background1"]), WINDOW_SIZE)
        self.rect = self.surface.get_rect(topleft=(0, 0))
        self.data = data
        self.player = Player((200, HEIGHT-320))
        self.start_game()
        self.pause = False
        self.playing = True
        self.pause_button = pygame.transform.scale(pygame.image.load(
            IMAGES["pause_button"]).convert_alpha(), (100, 100))
        self.pause_button_rect = self.pause_button.get_rect(
            topright=(WIDTH, 0))
        self.pause_screen = PauseScreen()

    def start_game(self):
        pygame.mixer.music.load(SOUNDS[self.data["id"]-1])
        pygame.mixer.music.play()
        tmx_data = load_pygame(self.path)
        for layer in tmx_data.visible_layers:
            print(layer)
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    if surf:
                        pos = (x*TILE_SIZE, y*TILE_SIZE)
                        Tile(pos, surf, self.tile_group)
        for obj in tmx_data.objects:
            pos = (obj.x, obj.y)
            surf = obj.image
            print(surf)
            if surf:
                Object(pos, surf, self.tile_group)

    def draw(self, window):
        if self.playing:
            window.blit(self.surface, self.rect)
            window.blit(self.pause_button, self.pause_button_rect)
            self.tile_group.draw(window)
            self.player.draw(window)
        self.pause_screen.draw(window)
        if not self.pause:
            self.tile_group.update()
            self.player.update()
            self.player.collide(self.player.vel.y, self.tile_group)
            self.player.collide(0, self.tile_group)
            keys = pygame.key.get_pressed()
            if (click(self.pause_button_rect)) or keys[pygame.K_ESCAPE]:
                self.pause_screen.show = True
                pygame.mixer.music.pause()
            if self.player.died:
                pygame.mixer.music.stop()
        self.pause = self.pause_screen.show
        self.playing = not self.pause_screen.return_home and not self.player.died
