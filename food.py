import pygame
from pygame import Vector2


from settings import Settings, Colors
from utility import RandomPoint


class Food(pygame.sprite.Sprite):
    def __init__(self, obj_color=Colors.RED.value):
        super().__init__()
        self.food = pygame.Surface((Settings.BLOCK_SIZE, Settings.BLOCK_SIZE))
        self.block_size = Settings.BLOCK_SIZE
        self.got_eaten = False
        self.position = Vector2(self.random_position())
        self.prev_pos = Vector2(0, 0)
        self.rect = self.food.get_rect(topleft=self.position)
        self.dirty_rects = [self.rect]
        self.food.fill(obj_color)

    # def random_position(self):
    #     x = random.randrange(0, Settings.SCREEN_WIDTH, self.block_size)
    #     y = random.randrange(0, Settings.SCREEN_HEIGHT, self.block_size)
    #
    #     return x, y
    def random_position(self):
        return RandomPoint(0, self.block_size).point

    def update(self):
        self.prev_pos.x = self.position.x
        self.prev_pos.y = self.position.y

        self.position = Vector2(self.random_position())

        # rect_pos = pygame.Rect(self.position.x, self.position.y,
        #                        self.block_size,
        #                        self.block_size)
        # self.dirty_rects.append(rect_pos)
        # print(self.prev_pos, self.position)

    def render(self, screen):
        # # Erase the previous food sprite
        # self.food.fill(Settings.BG_COLOR)
        # screen.blit(self.food, self.prev_pos)
        #
        # # Draw the food sprite at now position
        # self.food.fill(Colors.RED.value)
        screen.blit(self.food, self.position)
        # print(len(self.dirty_rects))
        # Update only the parts of the screen that has been changed since the
        # last frame updated.
        # pygame.display.update(self.dirty_rects)
