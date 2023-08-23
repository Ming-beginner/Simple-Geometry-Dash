import pygame
import sys
from random import randint
from settings import *
# from HomeScreen.PlayButton import PlayButton
# from HomeScreen.SettingButton import SettingButton
# from HomeScreen.GreetingText import GreetingText

from settingScreen.Screen import SettingScreen
from levelScreen.Screen import LevelScreen
from levelScreen.Screen import Level

from HomeScreen import HomeScreen

pygame.init()

window_screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


# Background
background = pygame.transform.scale(pygame.image.load(IMAGES["background1"]).convert(), WINDOW_SIZE)
overlay = pygame.Surface((WINDOW_SIZE))
overlay.fill("black")
overlay.set_alpha(160)

# Home menu
# play_button = PlayButton()
# setting_button = SettingButton()
# greeting_text = GreetingText()
# home_screen = pygame.sprite.Group()
# home_screen.add(play_button, setting_button, greeting_text)

# Background music
pygame.mixer.music.load(SOUNDS[2])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(DEFAULT_VOLUME/10)



# Setting menu
setting_screen = SettingScreen()
level_screen = LevelScreen()
home_screen = HomeScreen()



def main():
    # game loop
    is_running = True
    status = "Home_Screen"
    
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button.rect.collidepoint(mouse_pos):
                    # status = "setting_screen"
                    setting_screen.show = True
                    
                if play_button.rect.collidepoint(mouse_pos):
                    # status = "level_screen"
                    level_screen.show = True

                    
        
        
        if status == 'Home_Screen':
            home_screen.draw(window_screen)
            home_screen.update()
            # setting_screen.draw(window_screen)
            level_screen.draw(window_screen)
        
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()