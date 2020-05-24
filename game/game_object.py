from game import pg
from game.interface_object import InterfaceObject
from pygame.math import Vector2


class GameObject(InterfaceObject):
    def __init__(self, master, img, x=0, y=0, vx=0, vy=0):
        super().__init__(master, img, x, y)
        self.__spd = Vector2(vx, vy)

    def update(self):
        self.set_pos(self.get_pos() + self.__spd)

    def get_spd(self):
        return self.__spd

    def set_spd(self, spd):
        self.__spd = Vector2(spd)

    def collision(self, other):
        return False
