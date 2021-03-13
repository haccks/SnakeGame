import pygame
from pygame import mixer
import os


from settings import Settings


class Sound:
    def __init__(self, sound_file):
        self.sound_file = sound_file
        self.sound = None

    def load_sound(self):
        class NoneSound:
            def play(self): pass

        if not pygame.mixer:
            return NoneSound()
        fullname = os.path.join(Settings.MEDIA_SOUNDS, self.sound_file)
        # print(fullname)
        try:
            self.sound = pygame.mixer.Sound(fullname)
        except pygame.error as message:
            print('Cannot load sound:', fullname)
            raise SystemExit(message)

    def play_sound(self, loops=0, vol=1.0):
        self.load_sound()
        self.sound.set_volume(vol)
        self.sound.play(loops)

