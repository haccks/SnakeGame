import pygame
from pygame.math import Vector2
from foundation import Settings
import copy

INITIAL_NUM_BLOCKS = 3
BLOCK_SIZE = 15


class SnakeBlock(pygame.sprite.Sprite):
    def __init__(self, factor, obj_color=(255, 255, 255)):
        """
        Constructor to initiate a snake block.
        :param factor:
        :param obj_color: Color the block
        """
        super().__init__()
        self.settings = Settings()
        self.block = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.block.get_rect()
        self.block.fill(obj_color)

        self.start_pos = Vector2(
            self.settings.screen_width - self.rect.width*factor,
            self.settings.screen_height / 2
        )


class Snake:
    step = BLOCK_SIZE

    def __init__(self):
        """
        Constructor to initiate snake object.
        """
        super().__init__()
        self.settings = Settings()
        self.snake = pygame.sprite.Group()
        self.create_snake()
        self.blocks_pos = [block.start_pos for block in self.snake]
        self.head_move = Vector2(0, 0)
        self.head_direction = None

    def create_snake(self):
        """
        Creates the initial snake from snake blocks.
        :return: None
        """

        for i in range(INITIAL_NUM_BLOCKS, 0, -1):
            self.snake.add(SnakeBlock(i))

    def move_right(self):
        """
        Updates the position for snake's head to move in right direction.
        :return: None
        """

        self.head_move.x = self.step
        self.head_move.y = 0

    def move_left(self):
        """
        Updates the position for snake's head to move in left direction.
        :return: None
        """

        self.head_move.x = -self.step
        self.head_move.y = 0

    def move_down(self):
        """
        Updates the position for snake's head to move in downward direction.
        :return: None
        """

        self.head_move.x = 0
        self.head_move.y = self.step

    def move_up(self):
        """
        Updates the position for snake's head to move in upward direction.
        :return: None
        """

        self.head_move.x = 0
        self.head_move.y = -self.step

    def update_head(self):
        """
        Updates the position of the snake's head. Insert new head to the body.
        :return: None
        """

        self.blocks_pos.insert(0, self.blocks_pos[0] + self.head_move)
        # old = copy.deepcopy(self.blocks_location)
        # self.blocks_location[1:] = old[:-1]
        # self.blocks_location[0] += move_snake

        # self.__reset_head_move()

    def update_body(self):
        """
        Updates the body of the snake. Pop out the last block.
        :return:
        """

        block_pos = self.blocks_pos.pop()
        # self.snake.remove(block_pos)

    def check_boundary(self):
        """
        Checks if snake move out of the screen. Normalizes position so that
        snake always moves back to the main screen.
        :return:
        """

        self.blocks_pos[0].x = self.blocks_pos[0].x % self.settings.screen_width
        self.blocks_pos[0].y = self.blocks_pos[0].y % self.settings.screen_height
        # print(self.blocks_pos)

    def update(self):
        """
        Updates the state of the snake object.
        :return: None
        """

        if self.head_direction == 'Right':
            self.move_right()
        elif self.head_direction == 'Left':
            self.move_left()
        elif self.head_direction == 'Down':
            self.move_down()
        elif self.head_direction == 'Up':
            self.move_up()

        if self.head_move.magnitude():
            self.update_head()
            self.update_body()
            self.check_boundary()

        self.snake.update()

    def render(self, screen):
        """
        Draws all the blocks of snake to the main screen.
        :param screen:
        :return: None
        """

        for idx, sn in enumerate(self.snake.sprites()):
            screen.blit(sn.block, self.blocks_pos[idx])
        # pygame.display.update(self.blocks_pos)

    def __reset_head_move(self):
        """
        This function should be used only for debugging purposes. Continuous
        movement of snake will stop and it will move only on key events.
        :return: None
        """

        self.head_move.x = 0
        self.head_move.y = 0
        self.head_direction = None

