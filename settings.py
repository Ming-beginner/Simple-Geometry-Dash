import pygame
VERTICLE_TILE_NUMBER = 12
TILE_SIZE = 64

HEIGHT = 720
WIDTH = 1280

WINDOW_SIZE = (WIDTH, VERTICLE_TILE_NUMBER*TILE_SIZE)


FPS = 60


IMAGES = {
    "background1": "Graphics/backgrounds/background1.png",
    "playing_button": "Graphics/buttons/play.png",
    "setting_button": "Graphics/buttons/setting.png",
    "greeting_text": "Graphics/texts/greeting.png",
    "close_button": "Graphics/buttons/close.png",
    "increase_volume": "Graphics/buttons/volume_increase.png",
    "decrease_volume": "Graphics/buttons/volume_decrease.png",
    "level_button": "Graphics/buttons/level.png",
    "return_button": "Graphics/buttons/return.png",
    "pause_button": "Graphics/buttons/pause.png",
    "home_button": "Graphics/buttons/home.png",
}

SOUNDS = [
    "audio/pygame_soundtrack_1.wav",
    "audio/pygame_soundtrack_2.wav",
    "audio/pygame_soundtrack_3.wav"
]

DEFAULT_VOLUME = 5
FONT = "font/font.ttf"
LEVELS = [
    {
        "id": 1,
        "name": "Level 1",
        'terrain': 'levelData/level1/level_1.tmx',
    },
    {
        "id": 2,
        "name": "Level 2",
        'terrain': 'levelData/level2/level_2.tmx'
    },
    {
        "id": 3,
        "name": "Level 3",
        'terrain': 'levelData/level3/level_3.tmx'
    },
]
PLAYER = "Graphics/player/player.png"
GRAVITY = pygame.math.Vector2(0, 0.86)
