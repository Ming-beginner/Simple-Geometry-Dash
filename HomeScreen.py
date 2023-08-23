import pygame
from settings import *
from support import load_button_image
from Button import Button
from GreetingText import GreetingText


class HomeScreen(pygame.sprite.Sprite):
    global screen_state

    def __init__(self):
        self.playing_button = Button(
            WIDTH / 2, 500, 150, 150, 'playing_button')
        self.setting_button = Button(
            WIDTH/2 + 200, 500, 110, 110, 'setting_button')
        self.greeting_text = GreetingText()
        self.background = pygame.transform.scale(
            pygame.image.load(IMAGES["background1"]).convert(), WINDOW_SIZE)

        self.screen = pygame.sprite.Group()
        self.screen.add(self.greeting_text,
                        self.setting_button, self.playing_button)

        self.state = True

    def draw(self, window_screen):
        if self.state:
            window_screen.fill("black")
            window_screen.blit(self.background, (0, 0))
            self.screen.draw(window_screen)
            self.playing_button.draw(window_screen)
            self.setting_button.draw(window_screen)
