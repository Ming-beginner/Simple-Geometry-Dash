import pygame
from settings import *
from .LevelButton import LevelButton


class LevelScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.show = False
        self.image = pygame.transform.scale(pygame.image.load(
            IMAGES["background1"]).convert(), WINDOW_SIZE)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.return_button = pygame.transform.scale(
            pygame.image.load(IMAGES["return_button"]).convert_alpha(), (50, 50))
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

    def draw(self, window):
        if self.show:
            if pygame.mouse.get_pressed()[0]:
                if self.return_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.show = False
            for level in LEVELS:
                level_button = LevelButton(level["id"])
                level_button.draw(self.image)
            window.blit(self.image, self.rect)
