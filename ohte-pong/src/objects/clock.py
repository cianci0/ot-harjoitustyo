import pygame

class Clock:
    """Clock class to monitor time in game loop
       
       Attributes:
       clock: pygame.time.Clock object
    """
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()