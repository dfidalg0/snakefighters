from game import pg, Screen, GameObject, Player, imgpowerup, Food, SecondChance, Invencibility
from pygame.math import Vector2
from pygame.time import Clock
import random


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

    def powerup_factory(self, nfood):
        boundx = (self.__screen.get_resolution()[0] - 100) / 2
        boundy = (self.__screen.get_resolution()[1] - 100) / 2
        xf = random.randint(-boundx, boundx)
        yf = random.randint(-boundy, boundy)
        xl = random.randint(-boundx, boundx)
        yl = random.randint(-boundy, boundy)
        if nfood <= 3:
            Food(self.__screen, imgpowerup['FOOD'], xf, yf)
            nfood = nfood + 1
        i = random.randint(1, 1000)
        if i < 10:
            SecondChance(self.__screen, imgpowerup['LIFE'], xl, yl)
        if i > 990:
            Invencibility(self.__screen, imgpowerup['INVI'], xl, yl)
        return nfood

    def game_loop(self):
        from math import inf
        running = True
        nfood = 0
        while running:
            self.__screen.update()
            self.__clock.tick(15)  # 15 FPS parece ser adequado
            nfood = self.powerup_factory(nfood)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    # Pode ser feito checando event.key in self.__command.keys()
                    try:
                        self.__command[event.key]()
                    except KeyError:
                        pass  # Chave não associada a nenhum comando

            dead_players = []
            for player in self.__player:
                head = player.get_head()
                for other in self.__player:
                    if other.collision(head):
                        player.dec_health()

                if player.get_health() <= 0:
                    dead_players.append(player)

            for player in self.__player:
                player.update()

            for player in dead_players:
                player.destroy()
                self.__player.remove(player)
