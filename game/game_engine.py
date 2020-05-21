from game import pg, Screen, GameObject, Player
from pygame.math import Vector2
from time import sleep
from pygame.time import Clock


class GameEngine:
    def __init__(self, screen):
        self.__player = []
        self.__screen = screen
        self.__command = {}
        self.__clock = Clock()

    def add_player(self, imgset, x, y, keyset, vx=0, vy=0):
        newplayer = Player(self.__screen, imgset, x, y, vx, vy)
        self.__player.append(newplayer)

        controls = newplayer.get_controls()

        self.__command.update(zip(keyset,controls))

    def game_loop(self):
        running = True
        while running:
            self.__screen.update()
            self.__clock.tick(10)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    try:
                        self.__command[event.key]()
                    except KeyError:
                        pass

            for player in self.__player:
                player.update()
