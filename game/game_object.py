from game import pg
from game import InterfaceObject
from pygame.math import Vector2


class GameObject(InterfaceObject):
    def __init__(self, master, img, x=0, y=0, vx=0, vy=0, w=0):
        super().__init__(master, img, x, y)
        self.__img0 = img
        self.__spd = Vector2(vx, vy)
        self.__ang_spd = w
        self.__angle = 0
        self.__axis = Vector2(0,1)

    def update(self):
        self.set_pos(self.get_pos() + self.__spd)
        self.rotate(self.__ang_spd)

    def rotate(self,phi):
        if self.__ang_spd != 0:
            new_pos = self.get_pos().rotate(phi)
            self.set_pos(new_pos)
            self.__angle = (self.__angle + phi) % 360
            new_img = pg.transform.rotate(self.__img0,-self.__angle)
            self.set_img(new_img)
            self.__axis.rotate(phi)

    def get_spd(self):
        return self.__spd

    def set_spd(self, spd):
        self.__spd = Vector2(spd)

    def get_ang_spd(self):
        return self.__ang_spd

    def set_ang_spd(self,w):
        self.__ang_spd = w

    def collision(self, other):
        return False
