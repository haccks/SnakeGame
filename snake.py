from game import Game
import pygame
from pygame.math import Vector2


class Snake(Game):
    def __init__(self, speed=5, obj_color=(255, 255, 255)):
        super().__init__()
        self.snake = pygame.Surface((10, 10))
        self.rect = self.snake.get_rect()
        self.snake.fill(obj_color)
        self.location = Vector2(
            self.screen_width/2,
            self.screen_height/2
        )
        self.speed = speed
        self.move_snake = Vector2(0, 0)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        pass

    def update_game_state(self):
        # if self.move_right:
        #     self.location.x += self.speed
        # elif self.move_left:
        #     self.location.x -= self.speed
        # elif self.move_down:
        #     self.location.y += self.speed
        # elif self.move_up:
        #     self.location.y -= self.speed

        self.location += self.move_snake

        if self.location.x < 0:
            self.location.x = 0
        if self.location.x > self.screen_width - self.rect.width:
            self.location.x = self.screen_width - self.rect.width
        if self.location.y < 0:
            self.location.y = 0
        if self.location.y > self.screen_height - self.rect.height:
            self.location.y = self.screen_height - self.rect.height

        print(self.location)

        # Continuous movement of snake will stop and it will move only on key
        # event
        # self.move_snake.x = 0
        # self.move_snake.y = 0

        # if self.move_right:
        #     self.rect.move_ip(self.speed, 0)
        # elif self.move_left:
        #     self.rect.move_ip(-self.speed, 0)
        # elif self.move_down:
        #     self.rect.move_ip(0, self.speed)
        # elif self.move_up:
        #     self.rect.move_ip(0, -self.speed)
        #
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > self.screen_width - self.snake.get_width():
        #     self.rect.right = self.screen_width - self.snake.get_width()
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= self.screen_height - self.snake.get_height():
        #     self.rect.bottom = self.screen_height - self.snake.get_height()

        # self.rect.move_ip(self.position)

    def render_objects(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.snake, self.location)
        # self.rect.move_ip(self.location)
        # print(self.rect)
        pygame.display.flip()
        pass

    def handle_keydown_events(self, event):
        self.move_snake = Vector2(0, 0)

        if event.key == pygame.K_RIGHT:
            self.move_snake.x = self.speed
        elif event.key == pygame.K_LEFT:
            self.move_snake.x = -self.speed
        elif event.key == pygame.K_DOWN:
            self.move_snake.y = self.speed
        elif event.key == pygame.K_UP:
            self.move_snake.y = -self.speed
        elif event.key == pygame.K_ESCAPE:
            self.running = False

        # print(self.move_snake)

        # if event.key == pygame.K_RIGHT:
        #     self.move_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.move_left = True
        # elif event.key == pygame.K_DOWN:
        #     self.move_down = True
        # elif event.key == pygame.K_UP:
        #     self.move_up = True
        # elif event.key == pygame.K_ESCAPE:
        #     self.running = False

    def handle_keyup_events(self, event):
        # if event.key == pygame.K_RIGHT:
        #     self.move_right = False
        # elif event.key == pygame.K_LEFT:
        #     self.move_left = False
        # elif event.key == pygame.K_DOWN:
        #     self.move_down = False
        # elif event.key == pygame.K_UP:
        #     self.move_up = False

        # if event.key == pygame.K_RIGHT:
        #     self.move_snake.x = 0
        # elif event.key == pygame.K_LEFT:
        #     self.move_snake.x = 0
        # elif event.key == pygame.K_DOWN:
        #     self.move_snake.y = 0
        # elif event.key == pygame.K_UP:
        #     self.move_snake.y = 0
        pass

s = Snake()
s.game_loop(60)
