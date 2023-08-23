import pygame
from settings import *
from support import load_button_image

class Button(pygame.sprite.Sprite):
    hovered: bool
    def __init__(self, input_x, input_y, input_width, input_height, type):
        super().__init__()
        self.type = type
        self.image = pygame.transform.scale(pygame.image.load(IMAGES[self.type]).convert_alpha(), (input_width, input_height))
        self.rect = self.image.get_rect(center = (input_x, input_y))
        
    def check_hover_button(self):
        if self.is_hovered() and (self.type != "close_button") and (self.type != "increase_volume") and ( self.type != "decrease_volume"):
            self.image = pygame.transform.scale(pygame.image.load(IMAGES[self.type]).convert_alpha(), (self.rect.width+10, self.rect.height+10))
        else:
            self.image = pygame.transform.scale(pygame.image.load(IMAGES[self.type]).convert_alpha(), (self.rect.width-10, self.rect.width-10))
            
    def is_hovered(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.x <= x <= self.rect.x + self.rect.width and self.rect.y <= y <= self.rect.y + self.rect.height
        
    def draw(self, window_screen):
        self.check_hover_button()
        window_screen.blit(self.image, (self.rect.x, self.rect.y))


