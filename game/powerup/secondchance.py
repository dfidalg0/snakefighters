from game import pg, imgpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2


class SecondChance(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['LIFE'], x, y)

    def catch(self,player,engine):
        if player.get_health() < 3:
            player.inc_health()
