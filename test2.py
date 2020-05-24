from game import pg, Screen, GameObject, Player, GameEngine, gspeed
from time import sleep

screen = Screen()
game = GameEngine(screen)
SNAKE_FIG = pg.image.load('assets/img/snake_test.png')

imgset = (SNAKE_FIG, SNAKE_FIG, SNAKE_FIG)

game.add_player(imgset, 1, -200, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
game.add_player(imgset, -1, 200, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])

game.game_loop()
