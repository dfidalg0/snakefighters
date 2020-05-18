from game import pg
from pygame.math import Vector2

class InterfaceObject:
    def __init__ (self, master, img, x=0, y=0):
        self.__pos = Vector2(x,y)
        self.__master = master
        self.__img = img
        self.__slaves = set()
        self.__rect = Vector2(img.get_rect().size)

        master.add_slave(self)

    def update (self):
        pass

    def get_blit(self):
        ret = [(self.get_img(), self.get_screen_position())]
        for slave in self.get_slaves():
            ret = ret + slave.get_blit()

        return ret

    def get_screen_position(self):
        return self.__master.get_screen_position() + self.__pos - self.__rect/2

    def get_position (self):
        return self.__pos

    def set_position (self, pos):
        self.__pos = Vector2(pos)

    def get_img(self):
        return self.__img

    def set_img(self,img):
        self.__img = img

    def get_slaves(self):
        return self.__slaves

    def add_slave(self, slave):
        self.__slaves.add(slave)
