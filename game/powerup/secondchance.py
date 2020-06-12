from game import pg
from game.assets import imgpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2
from math import inf


class SecondChance(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['LIFE'], x, y)

    def catch(self,player,engine):
        health = player.get_health()

        sound = pg.mixer.Sound('assets/sounds/heal.wav')
        sound.set_volume(0.5)
        sound.play()

        if health == inf:
            player.inc_virtual_health()
        else:
            player.inc_health()
