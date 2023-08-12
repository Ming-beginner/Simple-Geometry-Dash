import pygame
VERTICLE_TILE_NUMBER = 20
TILE_SIZE = 16

HEIGHT = 720
WIDTH = 1280

WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60


IMAGES = {
    "background1": "graphics/backgrounds/background1.png",
    "play_button": "graphics/buttons/play.png",
    "setting_button": "graphics/buttons/setting.png",
    "greeting_text": "graphics/texts/greeting.png",
    "close_button": "graphics/buttons/close.png",
    "increase_volume": "graphics/buttons/volume_increase.png",
    "decrease_volume": "graphics/buttons/volume_decrease.png",
    "level_button": "graphics/buttons/level.png",
    "return_button": "graphics/buttons/return.png",
    "pause_button": "graphics/buttons/pause.png",
    "home_button": "graphics/buttons/home.png",
}

SOUNDS = ["audio/pygame_soundtrack_1.wav",
          "audio/pygame_soundtrack_2.wav", "audio/pygame_soundtrack_3.wav"]
DEFAULT_VOLUME = 5
FONT = "font/font.ttf"
LEVELS = [
    {
        "id": 1,
        "name": "Level 1",
        'terrain': 'levelData/level1/level_1_(fix).tmx'
    },
    {
        "id": 2,
        "name": "Level 2",
        'terrain': 'levelData/level1/level_1.tmx'
    },
    {
        "id": 3,
        "name": "Level 3",
        'terrain': 'levelData/level1/level_1.tmx'
    }
]
PLAYER = "graphics/player/player.png"
GRAVITY = pygame.math.Vector2(0, 0.86)
