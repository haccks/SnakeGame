import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, game_obj, obj_color=(255, 0, 0)):
        super().__init__()
        self.food = pygame.Surface((10, 10))
        self.rect = self.food.get_rect()
        self.food.fill(obj_color)

    def update(self):
        pass

    def render(self):
        pass
