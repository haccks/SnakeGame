import pygame
from pygame.math import Vector2
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

    def update_game_state(self):
        """
        Update states of the game objects.
        :return: None
        """

        self.snake.update()
        self.food.update()

    def render_objects(self):
        """
        Draw all the game objects to the main game window/screen
        :return: None
        """

        self.screen.fill(Settings.BG_COLOR)
        self.snake.render(self.screen)
        if self.play:
            self.food.render(self.screen)
        # pygame.display.flip()  # Updates the entire screen

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
