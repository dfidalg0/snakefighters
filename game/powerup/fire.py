from game import pg
from game.assets import imgpowerup, sndpowerup
from game.constants import fps, gunity
from game.powerup.powerup_meta import PowerUpMeta

fwid = 3
flen = 5

imgfire_on = pg.transform.scale(pg.image.load('assets/img/fire_on.png'), (fwid * gunity, flen * gunity))
imgfire_off = pg.transform.scale(pg.image.load('assets/img/fire_off.png'), (fwid * gunity, flen * gunity))

fon = {
    'up': imgfire_on,
    'right': pg.transform.rotate(imgfire_on, 270),
    'down': pg.transform.rotate(imgfire_on, 180),
    'left': pg.transform.rotate(imgfire_on, 90)
}

foff = {
    'up': imgfire_off,
    'right': pg.transform.rotate(imgfire_off, 270),
    'down': pg.transform.rotate(imgfire_off, 180),
    'left': pg.transform.rotate(imgfire_off, 90)
}


def get_code(spd):
    if spd.x > 0:
        return 'right'
    elif spd.x < 0:
        return 'left'
    elif spd.y > 0:
        return 'down'
    elif spd.y < 0:
        return 'up'


class Fire(PowerUpMeta):
    def __init__(self, master, x=0, y=0):
        super().__init__(master, imgpowerup['FIRE'], x, y)

    def catch(self, player, engine):
        player.clear_effect()

        sound = sndpowerup['BURN']
        sound.set_volume(0.6)

        head = player.get_head()
        spd = head.get_spd()

        pos = (flen + 1) / 2 * spd

        fire = engine.add_obstacle(
            master=head,
            img=fon[get_code(spd)],
            x=pos.x,
            y=pos.y
        )

        timer = 0
        timer_end = 7 * fps

        def flame(end=False):
            nonlocal timer, timer_end
            if end:
                engine.remove_obstacle(fire)
            elif timer >= timer_end:
                player.clear_effect()
            else:
                spd = player.get_head().get_spd()
                pos = (flen + 1) / 2 * spd
                fire.set_pos(pos)
                f = fon if timer % 2 == 0 else foff
                fire.set_img(f[get_code(spd)])
                timer += 1

        player.add_effect(flame, sound)
