from game import pg, GameObject
from pygame.math import Vector2
from abc import ABC,abstractmethod


class PowerUpMeta(GameObject,ABC):
    def __init__(self, master, img, x=0, y=0):
        super().__init__(master, img, x, y, 0, 0)
        self.__timer = 0

    def get_timer(self):
        return self.__timer

    def inc_timer(self):
        self.__timer += 1

    @abstractmethod
    def catch(self,player,engine):
        pass
