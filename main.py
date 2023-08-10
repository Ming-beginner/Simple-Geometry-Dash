import pygame
import sys
from random import randint
from settings import *
from homeScreen.PlayButton import PlayButton
from homeScreen.SettingButton import SettingButton
from homeScreen.GreetingText import GreetingText
from settingScreen.Screen import SettingScreen
from levelScreen.Screen import LevelScreen
from levelScreen.Screen import Level


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


# Background
background = pygame.transform.scale(
    pygame.image.load(IMAGES["background1"]).convert(), WINDOW_SIZE)
overlay = pygame.Surface((WINDOW_SIZE))
overlay.fill("#111111")
overlay.set_alpha(160)

# Home menu
play_button = PlayButton()
setting_button = SettingButton()
greeting_text = GreetingText()
screen_menu = pygame.sprite.Group()
screen_menu.add(play_button, setting_button, greeting_text)

# Background music
pygame.mixer.music.load(SOUNDS[randint(0, len(SOUNDS) - 1)])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(DEFAULT_VOLUME/10)

# Setting menu
setting_screen = SettingScreen()
level_screen = LevelScreen()
tile_groups = pygame.sprite.Group()
level1 = Level(LEVELS[0], tile_groups)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        play_button.hovered = play_button.rect.collidepoint(mouse_pos)
        play_button.show = not setting_screen.show
        setting_button.hovered = setting_button.rect.collidepoint(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if setting_button.rect.collidepoint(mouse_pos):
                setting_screen.show = True
            if play_button.rect.collidepoint(mouse_pos):
                #level_screen.show = True
                pass
    screen.fill("#ffffff")
    screen.blit(background, (0, 0))
    screen.blit(overlay, (0, 0))
    # screen_menu.draw(screen)
    # screen_menu.update()
    # setting_screen.draw(screen)
    # level_screen.draw(screen)
    tile_groups.draw(screen)
    tile_groups.update()
    pygame.display.update()
    clock.tick(FPS)
 