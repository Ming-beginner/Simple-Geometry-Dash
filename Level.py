import pygame
from support import click
from pytmx.util_pygame import load_pygame
from settings import *
from SettingScreen import SettingScreen
from Player import Player


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            surf.convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.rect.x -= 8


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
            midbottom=(WIDTH/2-100, HEIGHT*5/6-20))
        self.play_button = pygame.transform.scale(pygame.image.load(
            IMAGES["playing_button"]).convert_alpha(), (100, 100))
        self.play_button_rect = self.play_button.get_rect(
            midbottom=(WIDTH/2+100, HEIGHT*5/6-20))
        self.return_home = False

    def draw(self, window):
        if(self.show):
            window.blit(self.surface, (WIDTH/6, HEIGHT/6))
            window.blit(self.text_surf, self.text_rect)
            window.blit(self.play_button, self.play_button_rect)
            window.blit(self.home_button, self.home_button_rect)
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if self.play_button_rect.collidepoint(mouse_pos):
                    self.show = False
                    pygame.mixer.music.unpause()
                if self.home_button_rect.collidepoint(mouse_pos):
                    self.return_home = True
                    self.show = False
                    pygame.mixer.music.stop()


class SumarizeScreen(PauseScreen):
    def __init__(self):
        super().__init__()
        self.result = "lose"
        self.title = "YOU LOST!!!"
        self.text_surf = self.font.render(
            self.title, False, "#ffffff")
        self.text_rect = self.text_surf.get_rect(
            center=(WIDTH/2, HEIGHT/6+100))
        self.home = pygame.transform.scale(pygame.image.load(
            IMAGES["home_button"]).convert_alpha(), (120, 120))
        self.home_rect = self.home.get_rect(
            center=(WIDTH/2, HEIGHT/2+160))

    def update_title(self):
        self.title = "YOU WON!!!" if self.result == "win" else "YOU LOST!!!"
        self.text_surf = self.font.render(
            self.title, False, "#ffffff")

    def draw(self, window):
        if self.show:
            window.blit(self.surface, (WIDTH/6, HEIGHT/6))
            window.blit(self.text_surf, self.text_rect)
            window.blit(self.home, self.home_rect)
            if click(self.home_rect):
                self.return_home = True
                self.show = False
                pygame.mixer.music.stop()


class Level(pygame.sprite.Sprite):
    def __init__(self, data):
        self.path = data["terrain"]
        self.tile_group = pygame.sprite.Group()
        self.object_group = pygame.sprite.Group()
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
        self.sumarize_screen = SumarizeScreen()

    def start_game(self):
        pygame.mixer.music.load(SOUNDS[self.data["id"]-1])
        pygame.mixer.music.play()
        tmx_data = load_pygame(self.path)
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    if surf:
                        pos = (x*TILE_SIZE, y*TILE_SIZE)
                        if(self.data["id"]-1 == 1):
                            pos = (x*TILE_SIZE*4, y*TILE_SIZE*4)
                        Tile(pos, surf, self.tile_group)
        for obj in tmx_data.objects:
            pos = (obj.x, obj.y)
            if(self.data["id"]-1 == 1):
                pos = (obj.x, obj.y)
            print(pos)
            surf = obj.image
            if surf:
                Object(pos, surf, self.object_group)

    def draw(self, window):
        if self.playing:
            window.blit(self.surface, self.rect)
            window.blit(self.pause_button, self.pause_button_rect)
            self.tile_group.draw(window)
            self.object_group.draw(window)
            self.player.draw(window)
        if self.player.win:
            self.pause = True
            self.sumarize_screen.result = "win"
            self.sumarize_screen.update_title()
            self.sumarize_screen.show = True
            self.sumarize_screen.draw(window)
        if self.player.died:
            self.pause = True
            self.sumarize_screen.result = "lose"
            self.sumarize_screen.show = True
            self.sumarize_screen.draw(window)
            pygame.mixer.music.stop()
        else:
            self.pause_screen.draw(window)
        if not self.pause:
            self.tile_group.update()
            self.object_group.update()
            self.player.update(window)
            self.player.collide(self.player.vel.y, self.tile_group)
            self.player.collide(0, self.tile_group)
            for obj in self.object_group:
                if self.player.rect.x >= obj.rect.x:
                    self.player.win = True
            keys = pygame.key.get_pressed()
            if (click(self.pause_button_rect)) or keys[pygame.K_ESCAPE]:
                self.pause_screen.show = True
                pygame.mixer.music.pause()
        self.pause = self.pause_screen.show and not self.sumarize_screen.show
        self.playing = not self.pause_screen.return_home and not self.sumarize_screen.return_home
