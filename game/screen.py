from game import pg, gunity
from pygame.math import Vector2


class Screen:
    def __init__(self, resolution=(1280, 720), color=(0, 0, 0)):
        self.__screen = pg.display.set_mode(resolution)
        self.__pos = Vector2(resolution[0] / 2, resolution[1] / 2)
        self.__color = color
        self.__resolution = Vector2(resolution)
        self.__slaves = []
        background = pg.image.load('assets/img/background.jpg')
        self.__background = pg.transform.scale(background,resolution)

    def update(self):
        self.__screen.blit(self.__background, (0, 0))
        for slave in self.__slaves:
            for img, screen_pos in slave.get_blit():
                self.__screen.blit(img, screen_pos)

        pg.display.update()

    def get_screen_position(self):
        return Vector2(0, 0)

    def get_resolution(self):
        return self.__resolution

    def aux_abs_pos(self):
        return self.__pos

    def add_slave(self, slave):
        self.__slaves.append(slave)

    def remove_slave(self, slave):
        self.__slaves.remove(slave)
