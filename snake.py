import pygame
from pygame.math import Vector2
import copy


from settings import Settings, Colors
from utility import RandomPoint
INITIAL_NUM_BLOCKS = 1


class SnakeBlock(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), obj_color=Colors.BLACK.value):
        """
        Constructor to initiate a snake block.
        :param pos: Initial position of the block
        :param obj_color: Color the block
        """
        super().__init__()
        self.block = pygame.Surface((Settings.BLOCK_SIZE, Settings.BLOCK_SIZE))
        self.block.fill(obj_color)
        self.start_pos = Vector2(pos)
        self.rect = self.block.get_rect(topleft=pos)


class Snake:
    STEP = Settings.BLOCK_SIZE

    def __init__(self):
        """
        Constructor to initiate snake object.
        """
        super().__init__()
        self.snake = []
        self.blocks_pos = []
        self.create_snake()
        self.head_move = Vector2(0, 0)
        self.head_direction = None
        self.last_block_pos = Vector2(0, 0)
        self.length = INITIAL_NUM_BLOCKS
        # self.dirty_rects = [block.rect for block in self.snake]

    def create_snake(self):
        """
        Creates the initial snake from snake blocks.
        :return: None
        """
        point = RandomPoint(0, Settings.BLOCK_SIZE).point

        for i in range(INITIAL_NUM_BLOCKS):
            print(point)
            x = Settings.SCREEN_WIDTH #- (i + 1) * Settings.BLOCK_SIZE
            y = point[1]  # Same random y coordinate for all blocks
            self.snake.insert(0, SnakeBlock(pos=(x, y)))
            self.blocks_pos.insert(0, Vector2(x, y))

    def increase_snake_length(self):
        self.snake.insert(0, SnakeBlock(self.blocks_pos[0]))
        self.update_head()
        self.length += 1

    def move_right(self):
        """
        Updates the position for snake's head to move in right direction.
        :return: None
        """

        self.head_move.x = self.STEP
        self.head_move.y = 0

    def move_left(self):
        """
        Updates the position for snake's head to move in left direction.
        :return: None
        """

        self.head_move.x = -self.STEP
        self.head_move.y = 0

    def move_down(self):
        """
        Updates the position for snake's head to move in downward direction.
        :return: None
        """

        self.head_move.x = 0
        self.head_move.y = self.STEP

    def move_up(self):
        """
        Updates the position for snake's head to move in upward direction.
        :return: None
        """

        self.head_move.x = 0
        self.head_move.y = -self.STEP

    def update_head(self):
        """
        Updates the position of the snake's head. Insert new head to the body.
        :return: None
        """

        self.blocks_pos.insert(0, self.blocks_pos[0] + self.head_move)
        if self.length < 3:
            self.snake.insert(0, SnakeBlock(pos=self.blocks_pos[0]))

        # old = copy.deepcopy(self.blocks_location)
        # self.blocks_location[1:] = old[:-1]
        # self.blocks_location[0] += move_snake

        # self.__reset_head_move()

    def update_body(self):
        """
        Updates the body of the snake. Pop out the last block.
        :return:
        """
        if self.length < 3:
            return
        self.last_block_pos = self.blocks_pos.pop()
        print(self.blocks_pos)

    def check_boundary(self):
        """
        Checks if snake move out of the screen. Normalizes position so that
        snake always moves back to the main screen.
        :return:
        """

        self.blocks_pos[0].x = self.blocks_pos[0].x % Settings.SCREEN_WIDTH
        self.blocks_pos[0].y = self.blocks_pos[0].y % Settings.SCREEN_HEIGHT
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

    def render(self, screen):
        """
        Draws all the blocks of snake to the main screen.
        :param screen:
        :return: None
        """

        for idx, sn in enumerate(self.snake):
            # print(idx)
            screen.blit(sn.block, self.blocks_pos[idx])
        # for idx, sn in enumerate(self.snake.sprites()):
        #     screen.blit(sn.block, self.blocks_pos[idx])
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
