from game import pg
from game import InterfaceObject, GameObject, PowerUp
from pygame.math import Vector2


class Food(PowerUp):
    def __init__(self, master, img, x=0, y=0):
        super().__init__(master, img, x, y)
