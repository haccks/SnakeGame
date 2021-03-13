import pygame
import time
from pygame import (
    K_RIGHT,
    K_LEFT,
    K_UP,
    K_DOWN,
    K_SPACE,
    K_ESCAPE,
    K_p
)


from foundation import Foundation
from snake import Snake
from food import Food
from settings import Colors, Settings
from sounds import Sound


class Game(Foundation):
    """
    A class that is responsible for running the game and handling all the
    game related activities.
    """
    def __init__(self, caption=None, icon=None):
        super().__init__(caption, icon)
        self.snake = Snake()
        self.food = Food()
        self.food_consumed_sound = Sound("consumed.wav")
        self.death_sound = Sound("death.mp3")
        self.bg_sound = Sound("background.mp3")
        self.play = False
        self.score = 0
        # self.bg = pygame.Surface((440, 440))

    def draw_grid(self):
        border = 0  # Settings.BLOCK_SIZE * 2 - 1
        h = Settings.SCREEN_HEIGHT - border
        w = Settings.SCREEN_WIDTH - border

        for row in range(border, h, Settings.BLOCK_SIZE):
            pygame.draw.line(self.screen, Colors.GREY.value, (border, row),
                             (w, row))

        for col in range(border, w, Settings.BLOCK_SIZE):
            pygame.draw.line(self.screen, Colors.GREY.value, (col, border),
                             (col, h))

    def play_game(self, key_pressed):
        """
        Start game on pressing the space bar key.
        :param key_pressed:
        :return: None
        """

        if key_pressed == K_SPACE and not self.play:
            self.snake.head_direction = 'Left'
            self.play = True
            # Setup the background sound but pause it by default
            self.bg_sound.play_sound(loops=-1, vol=0.01)
            self.bg_sound.pause_sound()
            self.draw_grid()

    def quit_game(self, key_pressed):
        """
        Quit game on pressing the escape key.
        :return: None
        """

        if key_pressed == K_ESCAPE:
            self.running = False

    def render_score(self):
        text = "Score: " + str(self.score)
        score_surf = self.font.render(text, True, (255, 0, 0))
        score_surf.set_alpha(100)
        self.screen.blit(score_surf, (0, 0))

    def snake_hit_food(self):
        head = self.snake.blocks_pos[0]
        if head == self.food.position:
            # print(self.food.position)
            self.food_consumed_sound.play_sound(vol=0.1)
            self.snake.increase_snake_length()
            self.score += 1
            return True
        return False

    def snake_hit_itself(self):
        head = self.snake.blocks_pos[0]
        if head in self.snake.blocks_pos[1:]:
            self.death_sound.play_sound(vol=0.3)
            time.sleep(1)
            self.running = False
            return True
        return False

    def update_game_state(self):
        """
        Update states of the game objects.
        :return: None
        """

        hit_food = self.snake_hit_food()
        hit_itself = self.snake_hit_itself()
        if not hit_food and not hit_itself:
            self.snake.update()
        # Update food position until food is not one of the snake block
        if hit_food and not hit_itself:
            while True:
                self.food.update()
                if self.food.position not in self.snake.blocks_pos:
                    break

    def render_objects(self):
        """
        Draw all the game objects to the main game window/screen
        :return: None
        """
        # grid_window = pygame.Rect((40, 40), (400, 400))
        # self.screen.fill((255, 255, 255), grid_window)
        self.screen.fill(Settings.BG_COLOR)
        if self.play:
            self.draw_grid()
            self.snake.render(self.screen)
            self.food.render(self.screen)
            self.render_score()
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
            elif event.key == K_p:
                self.bg_sound.pause_sound()

    def handle_keyup_events(self, event):
        """
        Handle all key release events.
        :param event: Event requested by user
        :return: None
        """

        pass


s = Game()
s.game_loop()
