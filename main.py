import pygame
import sys
from random import randint
from settings import *
from HomeScreen.PlayButton import PlayButton
from HomeScreen.SettingButton import SettingButton
from HomeScreen.GreetingText import GreetingText

from settingScreen.Screen import SettingScreen
from levelScreen.Screen import LevelScreen
from levelScreen.Screen import Level

pygame.init()

window_screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


# Background
background = pygame.transform.scale(pygame.image.load(
    IMAGES["background1"]).convert(), WINDOW_SIZE)
overlay = pygame.Surface((WINDOW_SIZE))
overlay.fill("black")
overlay.set_alpha(160)

# Home menu
play_button = PlayButton()
setting_button = SettingButton()
greeting_text = GreetingText()
screen_menu = pygame.sprite.Group()
screen_menu.add(play_button, setting_button, greeting_text)

# Background music
pygame.mixer.music.load(SOUNDS[0])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(DEFAULT_VOLUME/10)


# Setting menu
setting_screen = SettingScreen()
level_screen = LevelScreen()


def main():
    # game loop
    running = True
    status = "Home_Screen"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                sys.exit()

            # Mouse Setting
            mouse_pos = pygame.mouse.get_pos()
            play_button.hovered = play_button.rect.collidepoint(mouse_pos)
            play_button.show = not setting_screen.show
            setting_button.hovered = setting_button.rect.collidepoint(
                mouse_pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button.rect.collidepoint(mouse_pos):
                    setting_screen.show = True
                else:
                    setting_screen.show = False

                if play_button.rect.collidepoint(mouse_pos):
                    level_screen.show = True

        window_screen.fill("#ffffff")
        window_screen.blit(background, (0, 0))
        window_screen.blit(overlay, (0, 0))

        if status == 'Home_Screen':
            screen_menu.draw(window_screen)
            screen_menu.update()
            # setting_screen.draw(window_screen)
            level_screen.draw(window_screen)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
