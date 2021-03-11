import pygame
from pygame.math import Vector2
from foundation import Settings
import copy

INITIAL_NUM_UNITS = 3
RIGHT = 1
LEFT = -1
DOWN = 2
UP = -2


class SnakeUnit(pygame.sprite.Sprite):
    def __init__(self, factor, obj_color=(255, 255, 255)):
        super().__init__()
        self.unit = pygame.Surface((10, 10))
        self.rect = self.unit.get_rect()
        self.unit.fill(obj_color)
        self.settings = Settings()
        self.direction_flag = 0

        self.start_pos = Vector2(
            self.settings.screen_width - self.rect.width*factor,
            self.settings.screen_height / 2
        )


class Snake:
    def __init__(self, obj_color=(255, 255, 255)):
        super().__init__()
        # self.settings = Settings()
        self.snake = pygame.sprite.Group()
        self.create_snake()
        self.unit_locations = [entity.start_pos for entity in self.snake]

    def create_snake(self):
        for i in range(INITIAL_NUM_UNITS, 0, -1):
            self.snake.add(SnakeUnit(i))

        # s1 = SnakeUnit(3)
        # print(s1.rect.topleft, s1.rect.topright, s1.rect)

    def update(self, move_snake, speed, move_direction):
        old = copy.deepcopy(self.unit_locations)
        # old = list(self.unit_locations)
        # print(old, self.unit_locations)
        self.unit_locations[0] += move_snake

        if move_direction[0]:
            pass

        for idx, loc in enumerate(self.unit_locations, 0):
            if idx < len(self.unit_locations)-1:
                x = self.unit_locations[idx].x - (move_snake.x / speed) * 10
                y = self.unit_locations[idx].y - (move_snake.y / speed) * 10

                if self.unit_locations[idx].x < 0:
                    self.unit_locations[idx].x = 640 - speed
                if self.unit_locations[idx].x > 640 - speed:
                    self.unit_locations[idx].x = 0
                if self.unit_locations[idx].y < 0:
                    self.unit_locations[idx].y = 480 - speed
                if self.unit_locations[idx].y > 480 - speed:
                    self.unit_locations[idx].y = 0

                self.unit_locations[idx+1] = Vector2(x, y)
        print(self.unit_locations)
        self.snake.update()

    def render(self, screen, new_locations):
        for idx, sn in enumerate(self.snake.sprites()):
            screen.blit(sn.unit, self.unit_locations[idx])
