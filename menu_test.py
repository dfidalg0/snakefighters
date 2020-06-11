from game import pg, Screen, InterfaceObject, GameEngine, MainMenu
from game.constants import gunity
from game.assets import maps

screen = Screen()
menu = MainMenu(screen)
config = menu.menu_loop()

n = config['player_number']
sprites = config['players']['sprites']
orientations = config['players']['orientations']
positions = config['players']['positions']
controls = config['players']['controls']

if n > 0:
    background = pg.transform.scale(pg.image.load('assets/img/background.jpg'), (60 * gunity, 30 * gunity))
    arena = InterfaceObject(screen, background)
    game = GameEngine(screen,arena,maps['lines'])

    for i in range(n):
        game.add_player(sprites[i],orientations[i],*positions[i],controls[i])

    game.game_loop()
