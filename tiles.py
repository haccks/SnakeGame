import pygame


from settings import Settings, Colors


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size=Settings.BLOCK_SIZE):
        super().__init__()
        self.pos = pos
        self.tile = pygame.Surface((size, size))
        self.rect = self.tile.get_rect(topleft=pos)


class Tiles:
    def __init__(self):
        self.tile_sprite = pygame.sprite.Group()

    def create_tiles(self):
        bs = Settings.BLOCK_SIZE
        h = Settings.SCREEN_HEIGHT
        w = Settings.SCREEN_WIDTH
        colors = [(220, 220, 220), Colors.WHITE.value]
        for row in range(0, w, bs):
            for col in range(0, h, bs):
                # print(col, row)
                if not (row + col) / bs % 2:
                    color = colors[1]
                else:
                    color = colors[0]
                tile = Tile((row, col))
                tile.tile.fill(color)
                self.tile_sprite.add(tile)
        print(self.tile_sprite)

    def update(self):
        self.tile_sprite.update()

    def render(self, screen):
        # self.tile_sprite.draw(screen)

        for sprite in self.tile_sprite.sprites():
            screen.blit(sprite.tile, sprite.rect)
