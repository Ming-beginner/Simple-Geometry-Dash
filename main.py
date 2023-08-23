import pygame
import sys
from random import randint
from settings import *
from SettingScreen import SettingScreen
from LevelScreen import LevelScreen
from HomeScreen import HomeScreen

pygame.init()
window_screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# Setting menu
setting_screen = SettingScreen()
level_screen = LevelScreen()
home_screen = HomeScreen()

pygame.mixer.music.load(SOUNDS[2])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(DEFAULT_VOLUME/10)


def main():
    # game loop
    is_running = True

    while is_running:
        window_screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                sys.exit()

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if home_screen.playing_button.rect.collidepoint(mouse_pos):
                    level_screen.state = True
                    home_screen.state = False
                if home_screen.setting_button.rect.collidepoint(mouse_pos):
                    setting_screen.state = True
                if setting_screen.close_button.rect.collidepoint(mouse_pos):
                    setting_screen.state = False
                if setting_screen.increase_volume_button.rect.collidepoint(mouse_pos):
                    setting_screen.increase_volume()
                if setting_screen.decrease_volume_button.rect.collidepoint(mouse_pos):
                    setting_screen.decrease_volume()
                if level_screen.return_button.rect.collidepoint(mouse_pos):
                    level_screen.state = False
                    home_screen.state = True

        home_screen.draw(window_screen)
        setting_screen.draw(window_screen)
        level_screen.draw(window_screen)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
