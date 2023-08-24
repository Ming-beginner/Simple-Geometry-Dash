import pygame
from settings import *
from support import click
from Button import Button
from support import load_button_image


class SettingScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((WIDTH*2/3, HEIGHT*2/3))
        self.surface.fill("#080907")
        self.show = False
        self.close_button = Button(
            WIDTH/6 + 100, HEIGHT/6 + 100, 75, 75, 'close_button')
        self.increase_volume_button = Button(
            WIDTH/2 + 200, 400, 100, 100, 'increase_volume')
        self.decrease_volume_button = Button(
            WIDTH/2 - 200, 400, 100, 100, 'decrease_volume')
        # Setting background music
        self.volume = DEFAULT_VOLUME

        self.font = pygame.font.Font(FONT, 70)
        self.volume_surf = self.font.render(str(self.volume), False, "#ffffff")
        self.volume_rect = self.volume_surf.get_rect(center=(WIDTH/2, 400))
        self.text_surf = self.font.render("SOUND", False, "#ffffff")
        self.text_rect = self.text_surf.get_rect(center=(WIDTH/2, HEIGHT/6+50))

        self.state = False

    def increase_volume(self):
        if self.volume < 10:
            self.updateVolume(self.volume+1)
        else:
            self.updateVolume(10)

    def decrease_volume(self):
        if self.volume > 0:
            self.updateVolume(self.volume-1)
        else:
            self.updateVolume(0)

    def updateVolume(self, volume):
        self.volume = volume
        self.volume_surf = self.font.render(
            str(round(self.volume)), False, "#ffffff")
        self.volume_rect = self.volume_surf.get_rect(center=(WIDTH/2, 400))
        pygame.mixer.music.set_volume(round(self.volume/10, 1))

    def draw(self, window_screen):
        if self.state:
            window_screen.blit(self.surface, (WIDTH/6, HEIGHT/6))
            window_screen.blit(self.volume_surf, self.volume_rect)
            window_screen.blit(self.text_surf, self.text_rect)
            self.close_button.draw(window_screen)
            self.increase_volume_button.draw(window_screen)
            self.decrease_volume_button.draw(window_screen)
