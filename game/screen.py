from game import pg
from game.constants import gunity, resolution
from game.assets import img_icon
from pygame.math import Vector2


class Screen:
    def __init__(self, color=(0, 0, 0)):
        self.__pos = Vector2(resolution[0] / 2, resolution[1] / 2)
        self.__color = color
        self.__resolution = Vector2(resolution)
        self.__slaves = []

        self.__screen = pg.display.set_mode(resolution)
        pg.display.set_icon(img_icon)
        pg.display.set_caption('Snake Fighters')

    def update(self):
        self.__screen.fill(self.__color)
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
