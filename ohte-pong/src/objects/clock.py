import pygame as pg

class Clock:
    """Clock class to monitor time in game loop
       
       Attributes:
       clock: pg.time.Clock object

       Methods:
       tick(self, ms): Update clock
       get_ticks(self): Get number of milliseconds since pygame was initialized. Only used to test tick()-function
    """
    def __init__(self):
        self.clock = pg.time.Clock()

    def tick(self, ms):
        self.clock.tick(ms)

    def get_ticks(self):
        return pg.time.get_ticks()