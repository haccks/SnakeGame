from foundation import Foundation
import pygame
from pygame.math import Vector2
from snake import Snake


class Game(Foundation):
    def __init__(self, speed=10, obj_color=(255, 255, 255)):
        super().__init__()
        self.snake = Snake()
        self.locations = self.snake.unit_locations
        # print(self.locations)
        self.move_snake = Vector2(0, 0)
        self.start = False
        self.speed = speed
        self.move_direction = [False, False, False, False]  # left, right, up, down

    def update_game_state(self):
        # self.location += self.move_snake
        # self.locations[0] += self.move_snake
        if self.move_snake.magnitude():
            self.snake.update(self.move_snake, self.speed, self.move_direction)

        # for idx, unit in enumerate(self.snake.snake):
        #     if self.locations[idx].x < 0:
        #         self.locations[idx].x = self.screen_width - unit.rect.width
        #     if self.locations[idx].x > self.screen_width - unit.rect.width:
        #         self.locations[idx].x = 0
        #     if self.locations[idx].y < 0:
        #         self.locations[idx].y = self.screen_height - unit.rect.height
        #     if self.locations[idx].y > self.screen_height - unit.rect.height:
        #         self.locations[idx].y = 0

        # print(self.locations)

        # Continuous movement of snake will stop and it will move only on key
        # event
        # self.move_snake.x = 0
        # self.move_snake.y = 0

    def render_objects(self):
        self.screen.fill(self.bg_color)
        self.snake.render(self.screen, self.locations)
        # self.screen.blit(self.snake.snake, self.location)
        pygame.display.flip()
        pass

    def handle_keydown_events(self, event):
        # self.move_snake = Vector2(0, 0)

        # if not self.start and event.key == pygame.K_SPACE:
        #     self.move_snake.x = -self.speed
        #     self.start = True

        if event.key == pygame.K_RIGHT and not self.move_direction[0]:
            self.move_snake = Vector2(0, 0)
            self.move_direction = [False]*4
            self.move_direction[1] = True
            self.move_snake.x = self.speed
        elif event.key == pygame.K_LEFT and not self.move_direction[1]:
            self.move_snake = Vector2(0, 0)
            self.move_direction = [False] * 4
            self.move_direction[0] = True
            self.move_snake.x = -self.speed
        elif event.key == pygame.K_DOWN and not self.move_direction[2]:
            self.move_snake = Vector2(0, 0)
            self.move_direction = [False] * 4
            self.move_direction[3] = True
            self.move_snake.y = self.speed
        elif event.key == pygame.K_UP and not self.move_direction[3]:
            self.move_snake = Vector2(0, 0)
            self.move_direction = [False] * 4
            self.move_direction[2] = True
            self.move_snake.y = -self.speed
        elif event.key == pygame.K_ESCAPE:
            self.running = False

    def handle_keyup_events(self, event):
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
s.game_loop(20)
