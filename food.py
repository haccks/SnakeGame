import pygame
from pygame import Vector2
import random


from foundation import Settings

BLOCK_SIZE = 15


class Food(pygame.sprite.Sprite):
    def __init__(self, obj_color=(255, 0, 0)):
        super().__init__()
        self.settings = Settings()
        self.food = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.food.get_rect()
        self.block_size = BLOCK_SIZE
        self.position = Vector2(0, 0)
        self.food.fill(obj_color)

    def update(self):
        self.position.x = random.randint(
            0,
            self.settings.screen_width-self.block_size
        )

        self.position.y = random.randint(
            0,
            self.settings.screen_height-self.block_size
        )

    def render(self, screen):
        screen.blit(self.food, self.position)
