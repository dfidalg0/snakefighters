from game import pg, imgpowerup, max_health
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2
from math import inf


class SecondChance(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['LIFE'], x, y)

    def catch(self,player,engine):
        health = player.get_health()
        if health == inf:
            player.inc_health(1j)
        elif health < max_health:
            player.inc_health()
