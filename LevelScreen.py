import pygame
from settings import *
from support import click, play_bg_music
from random import randint
from Button import Button
from LevelButton import LevelButton
from Level import Level


class LevelScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.background = pygame.transform.scale(pygame.image.load(IMAGES["background1"]).convert(), WINDOW_SIZE)
        self.rect = self.image.get_rect(topleft=(0, 0))
        
        self.return_button = Button(30, 30, 60, 60, 'return_button')
    
        self.overlay = pygame.Surface((WINDOW_SIZE))
        self.overlay.fill("#111111")
        self.overlay.set_alpha(160)
        
        self.font = pygame.font.Font(FONT, 90)
        self.text = self.font.render("Levels", False, "#ffffff").get_rect(center=(WIDTH/2, 200))
        # self.text_rect = self.text.get_rect(center=(WIDTH/2, 200))
        
        self.background.blit(self.overlay, (0, 0))
        self.background.blit(self.text)
        # self.tile_groups = pygame.sprite.Group()
        self.game_play = None
        self.state = False

    def draw(self, window_screen):
        if self.state: 
            if not self.game_play:
                self.return_button.draw(window_screen)
                for level in LEVELS:
                    level_button = LevelButton(level["id"])
                    level_button.draw(self.image)
                    if click(level_button.rect):
                        pygame.mixer.music.stop()
                        self.game_play = Level(level)
                window_screen.blit(self.image)
                
            else:
                self.game_play.draw(window_screen)
                if not self.game_play.playing:
                    self.game_play = None
                    play_bg_music()
