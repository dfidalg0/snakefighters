from game import pg, Screen, GameObject, Player
from pygame.math import Vector2
from time import sleep


class GameEngine:
    def __init__(self, screen):
        self.__player = []
        self.__screen = screen
        self.__command = {}

    def add_player(self, imgset, x, y, vx=0, vy=0):
        newplayer = Player(self.__screen, imgset, x, y, vx, vy)
        self.__player.append(newplayer)

        if len(self.__player) >= 1:
            self.__command.update({
                pg.K_UP: self.__player[0].up,
                pg.K_DOWN: self.__player[0].down,
                pg.K_LEFT: self.__player[0].left,
                pg.K_RIGHT: self.__player[0].right
            })

    def game_loop(self):
        running = True
        while running:
            self.__screen.update()
            sleep(0.001)
            for player in self.__player:
                player.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    self.__command[event.key]()
