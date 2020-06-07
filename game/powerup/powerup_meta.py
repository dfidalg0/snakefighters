from game import pg
from game import GameObject
from pygame.math import Vector2
from abc import ABC,abstractmethod


class PowerUpMeta(GameObject,ABC):
    def __init__(self, master, img, x=0, y=0):
        super().__init__(master, img, x, y, 0, 0)

    @abstractmethod
    def catch(self,player,engine):
        pass
