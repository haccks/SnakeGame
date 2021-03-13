import pygame
from pygame import (
    K_RIGHT,
    K_LEFT,
    K_UP,
    K_DOWN,
    K_SPACE,
    K_ESCAPE,
)


from foundation import Foundation
from snake import Snake
from food import Food
from settings import Colors, Settings


class Game(Foundation):
    """
    A class that is responsible for running the game and handling all the
    game related activities.
    """
    def __init__(self, caption=None, icon=None):
        super().__init__(caption, icon)
        self.snake = Snake()
        self.food = Food()
        self.play = False
        self.score = 0

    def draw_grid(self):
        # TODO
        pass

    def play_game(self, key_pressed):
        """
        Start game on pressing the space bar key.
        :param key_pressed:
        :return: None
        """

        if key_pressed == K_SPACE and not self.play:
            self.snake.head_direction = 'Left'
            self.play = True

    def quit_game(self, key_pressed):
        """
        Quit game on pressing the escape key.
        :return: None
        """

        if key_pressed == K_ESCAPE:
            self.running = False

    def snake_hit_food(self):
        head = self.snake.blocks_pos[0]
        if head == self.food.position:
            print(self.food.position)
            self.snake.increase_snake_length()
            self.score += 1
            return True
        return False

    def snake_hit_itself(self):
        head = self.snake.blocks_pos[0]
        if head in self.snake.blocks_pos[1:]:
            self.running = False
            return False
        return True

    def update_game_state(self):
        """
        Update states of the game objects.
        :return: None
        """

        hit_food = self.snake_hit_food()
        hit_itself = self.snake_hit_itself()
        if not hit_food and hit_itself:
            self.snake.update()
        # Update food position until food is not one of the snake block
        if hit_food:
            while True:
                self.food.update()
                if self.food.position not in self.snake.blocks_pos:
                    break

    def render_objects(self):
        """
        Draw all the game objects to the main game window/screen
        :return: None
        """

        self.screen.fill(Settings.BG_COLOR)
        self.snake.render(self.screen)
        if self.play:
            self.food.render(self.screen)
        pygame.display.flip()  # Updates the entire screen

    def handle_keydown_events(self, event):
        """
        Handle all key press events.
        :param event: Event requested by user
        :return: None
        """

        self.play_game(event.key)
        self.quit_game(event.key)

        if self.play:
            if event.key == K_RIGHT and self.snake.head_direction != 'Left':
                self.snake.head_direction = 'Right'
            elif event.key == K_LEFT and self.snake.head_direction != 'Right':
                self.snake.head_direction = 'Left'
            elif event.key == K_DOWN and self.snake.head_direction != 'Up':
                self.snake.head_direction = 'Down'
            elif event.key == K_UP and self.snake.head_direction != 'Down':
                self.snake.head_direction = 'Up'

    def handle_keyup_events(self, event):
        """
        Handle all key release events.
        :param event: Event requested by user
        :return: None
        """
        # if event.key == pygame.K_RIGHT:
        #     self.move_snake.x = 0
        # elif event.key == pygame.K_LEFT:
        #     self.move_snake.x = 0
        # elif event.key == pygame.K_DOWN:
        #     self.move_snake.y = 0
        # elif event.key == pygame.K_UP:
        #     self.move_snake.y = 0
        pass


s = Game()
s.game_loop()
