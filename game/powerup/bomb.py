from game import pg
from game.constants import fps
from game.assets import imgpowerup, imgexplosion
from game.powerup.powerup_meta import PowerUpMeta


class Bomb(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['BOMB'], x, y)

    def catch(self, player, engine):
        pos = self.get_pos()

        sound = pg.mixer.Sound('assets/sounds/explosion.wav')
        sound.set_volume(0.3)
        sound.play()

        explosion = engine.add_obstacle(x=pos[0], y=pos[1], img=imgexplosion)

        timer = 0

        def explode(end=False):
            nonlocal timer, explosion
            if end:
                engine.remove_obstacle(explosion)
            elif timer >= fps // 2:
                engine.remove_effect(explode)
            else:
                timer += 1

        engine.add_effect(explode)
