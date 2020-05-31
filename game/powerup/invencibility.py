from game import pg, imgpowerup, imgsetp, fps, max_health
from game.powerup.powerup_meta import PowerUpMeta
from pygame.math import Vector2
from math import inf


class Invencibility(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['INVI'], x, y)

    def catch(self,player,engine):
        player.clear_effect()

        old_health = player.get_health()
        player.set_health(inf)
        timer = 0
        timer_end = 3 * fps

        imgset0 = player.get_imgset()

        current, aux = imgset0, imgsetp

        def effect(end=False):
            nonlocal timer, timer_end
            nonlocal imgset0, current, aux

            if end:
                new_health = old_health + player.get_virtual_health()
                new_health = min(max_health, new_health)

                player.set_health(new_health)
                player.set_imgset(imgset0)
            elif timer >= timer_end:
                player.clear_effect()
            else:
                if timer_end - timer <= timer_end//3:
                    if timer % 3 == 0:
                        current, aux = aux, current
                        player.set_imgset(current)
                else:
                    current, aux = aux, current
                    player.set_imgset(current)
                timer += 1

        player.add_effect(effect)
