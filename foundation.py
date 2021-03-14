import pygame
import os


from settings import Settings, Colors


class Foundation:
    """
    A base class to store general settings and methods for the game.
    """

    def __init__(self, caption=None, icon=None):
        """
        Initialize the game
        :param size:        Screen size
        :param bg_color:    Background screen color
        :param caption:     Display caption
        :param icon:        Display icon
        """

        # super().__init__(size, bg_color)
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
        )
        self.font = pygame.font.SysFont("ibm3270", 25, True)
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen.fill(Settings.BG_COLOR)

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        if caption:
            pygame.display.set_caption(caption)
        if icon:
            pygame.display.set_icon(pygame.image.load(icon))

        # pygame.display.flip()

    def handle_events(self):
        """
        helper method to handle all the user events.
        :return: None
        """

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

    def game_loop(self):
        """
        This function will start the game and will continue until user quit.
        :return: None
        """

        while self.running:
            self.handle_events()
            self.update_game_state()
            self.render_objects()
            self.clock.tick(Settings.FPS)

        pygame.quit()
