import pygame
import os


class Game(pygame.sprite.Sprite):
    """
    A base class to store general settings and methods for the game.
    """

    def __init__(self, size=(640, 480), bg_color=(0, 0, 0), caption=None,
                 icon=None):
        """
        Initialize the game
        :param size:        Screen size
        :param bg_color:         Background screen color
        :param caption:     Display caption
        :param icon:        Display icon
        """

        super().__init__()
        # pygame.sprite.Sprite.__init__(self)

        pygame.init()
        self.screen_width = size[0]
        self.screen_height = size[1]
        self.bg_color = bg_color
        self.running = True
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        self.clock = pygame.time.Clock()

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        if caption:
            pygame.display.set_caption("My game")
        if icon:
            pygame.display.set_icon(pygame.image.load("icon.png"))

        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.handle_keyup_events(event)

    def update_game_state(self):
        """
        This method Should be implemented in child class
        """
        pass

    def render_objects(self):
        """
        This method Should be implemented in child class
        """
        pass

    def handle_keydown_events(self, event):
        """
        This method Should be implemented in child class
        """
        pass

    def handle_keyup_events(self, event):
        """
        This method Should be implemented in child class
        """
        pass

    def game_loop(self, fps):
        while self.running:
            self.handle_events()
            self.update_game_state()
            self.render_objects()
            self.clock.tick(fps)
