from game import pg
from game.constants import max_health
from game.assets import imgpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2
from math import inf


class Death(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['WALL'], x, y)

    def catch(self, player, engine):
        health = player.get_health()
        if health != inf:
            player.dec_health()
