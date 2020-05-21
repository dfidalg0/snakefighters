from game import pg, Screen, GameObject, Player, GameEngine
from time import sleep


screen = Screen()
game = GameEngine(screen)
SNAKE_FIG = pg.image.load('assets/img/snake_test.png')

imgset = (SNAKE_FIG, SNAKE_FIG, SNAKE_FIG)

game.add_player(imgset, 0, 0, 0, 0)

game.game_loop()

