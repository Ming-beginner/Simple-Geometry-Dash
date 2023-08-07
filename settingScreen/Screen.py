import pygame
from settings import *
from random import randint
from math import ceil


class SettingScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface(
            (WIDTH*2/3, HEIGHT*2/3))
        self.surface.fill("#080907")
        self.show = False

        # Setting close button
        self.close_button_surf = pygame.transform.scale(
            pygame.image.load(IMAGES["close_button"]).convert_alpha(), (50, 50))
        self.close_button_rect = self.close_button_surf.get_rect(
            topleft=(WIDTH/6, HEIGHT/6))
        # Setting background music
        self.volume = 5
        self.background_music = pygame.mixer.Sound(SOUNDS[randint(0, 2)])
        self.background_music.play(-1)
        self.background_music.set_volume(self.volume/10)
        self.increase_volume_button_surf = pygame.transform.scale(pygame.image.load(
            IMAGES["increase_volume"]).convert_alpha(), (100, 100))
        self.increase_volume_button_rect = self.increase_volume_button_surf.get_rect(
            center=(WIDTH/2+200, 400))
        self.decrease_volume_button_surf = pygame.transform.scale(pygame.image.load(
            IMAGES["decrease_volume"]).convert_alpha(), (100, 100))
        self.decrease_volume_button_rect = self.decrease_volume_button_surf.get_rect(
            center=(WIDTH/2-200, 400))
        self.font = pygame.font.Font('font/OXYGENE1.TTF', 55)
        self.volume_surf = self.font.render(
            str(self.volume), False, "#ffffff")
        self.volume_rect = self.volume_surf.get_rect(center=(WIDTH/2, 400))
        self.text_surf = self.font.render(
            "SOUND", False, "#ffffff")
        self.text_rect = self.text_surf.get_rect(
            center=(WIDTH/2, HEIGHT/6+50))

    def updateVolume(self, volume):
        self.volume = volume
        self.volume_surf = self.font.render(
            str(round(self.volume)), False, "#ffffff")
        self.volume_rect = self.volume_surf.get_rect(center=(WIDTH/2, 400))
        self.background_music.set_volume(round(self.volume/10, 1))

    def increase_volume(self):
        if self.volume < 10:
            self.updateVolume(self.volume+0.05)
        else:
            self.updateVolume(10)

    def decrease_volume(self):
        if self.volume > 0:
            self.updateVolume(self.volume-0.05)
        else:
            self.updateVolume(0)

    def draw(self, window):
        if(self.show):
            window.blit(self.surface, (WIDTH/6, HEIGHT/6))
            window.blit(self.volume_surf, self.volume_rect)
            window.blit(self.text_surf, self.text_rect)
            window.blit(self.close_button_surf, self.close_button_rect)
            window.blit(self.increase_volume_button_surf,
                        self.increase_volume_button_rect)
            window.blit(self.decrease_volume_button_surf,
                        self.decrease_volume_button_rect)
            if pygame.mouse.get_pressed()[0]:
                if self.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.show = False
                elif self.increase_volume_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.increase_volume()
                elif self.decrease_volume_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.decrease_volume()
