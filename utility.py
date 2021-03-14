import random
from settings import Settings
from pygame import Vector2

random.seed()


class RandomPoint:
    def __init__(self, start, step=0):
        self.start = start
        self.step = step
        self.width = Settings.SCREEN_WIDTH
        self.height = Settings.SCREEN_HEIGHT
        self.point = self.get_rand_point()

    def random_coordinate(self, stop):
        return random.randrange(self.start, stop, self.step)

    def get_rand_point(self):
        x = self.random_coordinate(self.width)
        y = self.random_coordinate(self.height)
        return x, y
