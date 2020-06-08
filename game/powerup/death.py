from game import pg
from game.constants import max_health
from game.assets import imgpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2


class Death(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['WALL'], x, y)

    def catch(self, player, engine):
        player.dec_health()
