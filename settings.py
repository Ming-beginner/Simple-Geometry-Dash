WIDTH = 1280
HEIGHT = 720
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


vertical_tile_number = 15
tile_size = 64

screen_height = vertical_tile_number * tile_size
screen_width = 1280 


