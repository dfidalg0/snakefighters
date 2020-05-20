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
        self.__grow = False

    def get_nodes(self):
        return self.__nodes

    def grow_size(self, x, y):
        self.__grow = True

    def update (self):
        if self.__grow:
            self.__grow = False

            new_spd = self.__nodes[0].get_spd()
            new_pos = self.__nodes[0].get_pos()
            new_node = GameObject(self.__screen, self.__imgbody, *new_pos, *new_spd)

            self.__nodes.insert(1,new_node)
        else:
            for i in range(len(self.__nodes__)-1, 0, -1):
                self.__nodes[i].update()
                new_spd = self.__nodes[i-1].get_spd()
                self.__nodes[i].set_spd(new_spd)

        self.__nodes[0].update()

    def up(self):
        if self.__nodes[0].get_spd() != Vector2(0,1):
            self.__nodes[0].set_spd((0,-1))

    def down(self):
        if self.__nodes[0].get_spd() != Vector2(0, -1):
            self.__nodes[0].set_spd((0,1))

    def left(self):
        if self.__nodes[0].get_spd() != Vector2(1, 0):
            self.__nodes[0].set_spd((-1,0))

    def right(self):
        if self.__nodes[0].get_spd() != Vector2(-1, 0):
            self.__nodes[0].set_spd((1,0))
