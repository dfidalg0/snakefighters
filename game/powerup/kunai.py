from game import pg
from game.assets import imgpowerup
from game.constants import fps, gunity
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2
from math import inf

imgkunai = pg.transform.scale(pg.image.load('assets/img/kunai.png'),(24,64))

class Kunai(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['WEAP'], x, y)

    def catch(self,player,engine):
        player.clear_effect()

        head = player.get_head()
        kunai = engine.add_obstacle(master=head,x=0,y=-70,w=30,img=imgkunai)

        timer = 0
        timer_end = 7 * fps

        def spin(end=False):
            nonlocal timer,timer_end
            if end:
                engine.remove_obstacle(kunai)
            elif timer >= timer_end:
                player.clear_effect()
            else:
                kunai.update()
                timer += 1

        player.add_effect(spin)
