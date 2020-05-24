from game import pg, Screen, GameObject, Player
from pygame.math import Vector2
from pygame.time import Clock


class GameEngine:
    def __init__(self, screen):
        self.__player = []
        self.__screen = screen
        self.__command = {}
        self.__clock = Clock()

    def add_player(self, imgset, orient, x, y, keyset):
        newplayer = Player(self.__screen, imgset, x, y, orient)
        self.__player.append(newplayer)

        controls = newplayer.get_controls()

        self.__command.update(zip(keyset, controls))

    def game_loop(self):
        running = True
        while running:
            self.__screen.update()
            self.__clock.tick(15)  # 15 FPS parece ser adequado

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    # Pode ser feito checando event.key in self.__command.keys()
                    try:
                        self.__command[event.key]()
                    except KeyError:
                        pass  # Chave não associada a nenhum comando

            for player in self.__player:
                player.update()
