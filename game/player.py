from game import pg, Screen, GameObject
from pygame.math import Vector2


class Player:
    def __init__(self, screen, imgh, imgb, imgt, x=0, y=0):
        self.__screen = screen
        self.__imghead = imgh
        self.__imgbody = imgb
        self.__imgtail = imgt
        head = GameObject(screen, imgh, x, y)
        body = GameObject(screen, imgb, x - 100, y)
        tail = GameObject(screen, imgt, x - 200, y)
        self.__nodes = [head, body, tail]

    def get_nodes(self):
        return self.__nodes

    def grow_size(self, x, y):
        self.__nodes[0].set_img(self.__imgbody)
        node = GameObject(self.__screen, self.__imghead, x, y)
        node.set_spd(self.__nodes[0].get_spd())
        self.__nodes = [node] + self.__nodes

    def up(self):
        if self.__nodes[0].get_spd() != Vector2(0,1):
            speed = Vector2(0, -1)
            for node in self.__nodes:
                speedaux = node.get_spd()
                node.set_spd(speed)
                speed = speedaux

    def down(self):
        if self.__nodes[0].get_spd() != Vector2(0, -1):
            speed = Vector2(0, 1)
            for node in self.__nodes:
                speedaux = node.get_spd()
                node.set_spd(speed)
                speed = speedaux

    def left(self):
        if self.__nodes[0].get_spd() != Vector2(1, 0):
            speed = Vector2(-1, 0)
            for node in self.__nodes:
                speedaux = node.get_spd()
                node.set_spd(speed)
                speed = speedaux

    def right(self):
        if self.__nodes[0].get_spd() != Vector2(-1, 0):
            speed = Vector2(1, 0)
            for node in self.__nodes:
                speedaux = node.get_spd()
                node.set_spd(speed)
                speed = speedaux
