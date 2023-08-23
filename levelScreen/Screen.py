import pygame
from settings import *
from support import click, play_bg_music
from random import randint
from .LevelButton import LevelButton
from .Level import Level


class LevelScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.show = False
        self.image = pygame.transform.scale(pygame.image.load(
            IMAGES["background1"]).convert(), WINDOW_SIZE)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.return_button = pygame.transform.scale(pygame.image.load(IMAGES["return_button"]).convert_alpha(), (50, 50))
        self.return_button_rect = self.return_button.get_rect(topleft=(0, 0))
        self.overlay = pygame.Surface((WINDOW_SIZE))
        self.overlay.fill("#111111")
        self.overlay.set_alpha(160)
        self.font = pygame.font.Font(FONT, 90)
        self.text = self.font.render("Levels", False, "#ffffff")
        self.text_rect = self.text.get_rect(center=(WIDTH/2, 200))
        self.image.blit(self.overlay, (0, 0))
        self.image.blit(self.return_button, self.return_button_rect)
        self.image.blit(self.text, self.text_rect)
        self.tile_groups = pygame.sprite.Group()
        self.game_play = None

    def draw(self, window):
        if self.show and not self.game_play:
            if click(self.return_button_rect):
                self.show = False
                # play_bg_music()
            for level in LEVELS:
                level_button = LevelButton(level["id"])
                level_button.draw(self.image)
                if click(level_button.rect):
                    pygame.mixer.music.stop()
                    self.game_play = Level(level)
            window.blit(self.image, self.rect)
        if self.game_play:
            self.game_play.draw(window)
            if not self.game_play.playing:
                self.game_play = None
                play_bg_music()
