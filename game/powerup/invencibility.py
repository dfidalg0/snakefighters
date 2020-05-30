from game import pg, imgpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2


class Invencibility(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['INVI'], x, y)

    def catch(self,player,engine):
        pass
