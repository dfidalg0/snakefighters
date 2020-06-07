from game import pg, Screen, InterfaceObject, GameEngine, MainMenu
from game.assets import imgsety, imgsetb, imgseto, imgsetp
from game.constants import gspeed, gunity

sprites_list = [imgsety,imgsetb,imgseto,imgsetp]

screen = Screen()
menu = MainMenu(screen)
config = menu.menu_loop()

# menu.wait_to_init();
# se pá é melhor dar mais informações pra config e fazer um loop mais bonitinho kk
n = len(config["players"])

if n > 0:
    background = pg.transform.scale(pg.image.load('assets/img/background.jpg'), (60 * gunity, 30 * gunity))
    arena = InterfaceObject(screen, background)
    game = GameEngine(screen,arena)

    menu.wait_to_init()
    for i in range(n):
        game.add_player(sprites_list[i], 1, -200 , -200+100*i, config["players"][i])

    screen.remove_slave(menu)

    game.game_loop()
