import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
