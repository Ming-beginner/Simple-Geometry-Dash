VERTICLE_TILE_NUMBER = 15
TILE_SIZE = 64

HEIGHT = VERTICLE_TILE_NUMBER * TILE_SIZE
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
}

SOUNDS = ["audio/pygame_soundtrack_1.wav",
          "audio/pygame_soundtrack_2.wav", "audio/pygame_soundtrack_3.wav"]
DEFAULT_VOLUME = 5
FONT = "font/font.ttf"
LEVELS = [
    {
        "id": 1,
        "name": "Level 1",
    },
    {
        "id": 2,
        "name": "Level 2",
    },
    {
        "id": 3,
        "name": "Level 3",
    }
]


LEVEL_1 = {
    'Layer_land': '../levels/1/level_1_Tiles 2.csv',
    'Spy': '../levels/1/level_1_Black triangle.csv',
    'Tree1': '../levels/1/level_1_Tree1.csv'
}
