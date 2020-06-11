from game import pg, Screen, GameObject, InterfaceObject, Player, GameEngine
from game.assets import imgsetb, imgsety, maps, imgwall
from game.constants import gspeed, gunity


screen = Screen()
background = pg.transform.scale(pg.image.load('assets/img/background.jpg'), (60 * gunity, 30 * gunity))
arena = InterfaceObject(screen, background)
game = GameEngine(screen, arena)

game.load_map(maps['lines'])

game.add_player(imgsety, 1, -200, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])
game.add_player(imgsetb, -1, 200, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])

game.game_loop()
