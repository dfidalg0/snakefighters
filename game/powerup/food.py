from game import pg
from game.assets import imgpowerup, sndpowerup
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2


class Food(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['FOOD'], x, y)

    def catch(self,player,engine):
        player.grow_size()

        sound = sndpowerup['SWLL']
        sound.play()
