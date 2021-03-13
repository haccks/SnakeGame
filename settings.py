from enum import Enum


class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)


class Settings:
    """
    A class for basic game settings.
    """
    FPS = 10
    BLOCK_SIZE = 20
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    BG_COLOR = Colors.BLACK.value
    MEDIA_SOUNDS = "media/sounds"
    MEDIA_SPRITES = "media/sprites"

