from game import pg, Screen, GameObject, InterfaceObject, Player, GameEngine
from game.assets import imgsetb, imgsety, maps
from game.constants import gspeed, gunity


screen = Screen()
background = pg.transform.scale(pg.image.load('assets/img/background.jpg'), (60 * gunity, 30 * gunity))
arena = InterfaceObject(screen, background)
game = GameEngine(screen, arena)

WALL = pg.transform.scale(pg.image.load('assets/img/parede.png'), (gunity, gunity))

game.load_map(maps['eights'])

for x in range(-30 * gunity, +30 * gunity + 1, gunity):
    InterfaceObject(arena, WALL, x, +15 * gunity)
    InterfaceObject(arena, WALL, x, -15 * gunity)

for y in range(-14 * gunity, +14 * gunity + 1, gunity):
    InterfaceObject(arena, WALL, +30 * gunity, y)
    InterfaceObject(arena, WALL, -30 * gunity, y)

game.add_player(imgsety, 1, -200, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
game.add_player(imgsetb, -1, 200, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])

game.game_loop()
