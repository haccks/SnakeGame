import pygame
from pygame import Vector2
import random


from settings import Settings, Colors


class Food(pygame.sprite.Sprite):
    def __init__(self, obj_color=Colors.RED.value):
        super().__init__()
        self.food = pygame.Surface((Settings.BLOCK_SIZE, Settings.BLOCK_SIZE))
        self.rect = self.food.get_rect()
        self.block_size = Settings.BLOCK_SIZE
        self.position = Vector2(0, 0)
        self.prev_pos = Vector2(0, 0)
        self.dirty_rects = [self.rect]
        self.food.fill(obj_color)

    def update(self):
        self.prev_pos.x = self.position.x
        self.prev_pos.y = self.position.y
        self.position.x = random.randint(
            0,
            Settings.SCREEN_WIDTH-self.block_size
        )

        self.position.y = random.randint(
            0,
            Settings.SCREEN_HEIGHT-self.block_size
        )
        rect_pos = pygame.Rect(self.position.x, self.position.y,
                               self.block_size,
                               self.block_size)
        self.dirty_rects.append(rect_pos)
        # print(self.prev_pos, self.position)

    def render(self, screen):
        # Erase the previous food sprite
        self.food.fill(Settings.BG_COLOR)
        screen.blit(self.food, self.prev_pos)

        # Draw the food sprite at now position
        self.food.fill(Colors.RED.value)
        screen.blit(self.food, self.position)
        print(len(self.dirty_rects))
        # Update only the parts of the screen that has been changed since the
        # last frame updated.
        pygame.display.update(self.dirty_rects)
