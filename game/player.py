from game import pg, Screen, GameObject, gspeed
from pygame.math import Vector2


class Player:
    # TODO: Modificar o construtor para atribuir velocidade corretamente
    def __init__(self, screen, imgset, x, y, orient):
        self.__screen = screen
        self.__imghead = pg.transform.scale(imgset[0], (45, 45))
        self.__imgbody = pg.transform.scale(imgset[1], (45, 45))
        self.__imgtail = pg.transform.scale(imgset[2], (45, 45))
        head = GameObject(screen, self.__imghead, x, y, gspeed*orient, 0)
        body = GameObject(screen, self.__imgbody, x - 45*orient, y, gspeed*orient, 0)
        tail = GameObject(screen, self.__imgtail, x - 45*orient * 2, y, gspeed*orient, 0)
        self.__nodes = [head, body, tail]
        self.__grow = False

    def get_nodes(self):
        return self.__nodes

    def get_head(self):
        return self.__nodes[0]

    def get_controls(self):
        return [self.up, self.left, self.down, self.right]

    def grow_size(self):
        self.__grow = True

    def update(self):
        if self.__grow:
            self.__grow = False

            new_spd = self.__nodes[0].get_spd()
            new_pos = self.__nodes[0].get_pos()
            new_node = GameObject(self.__screen, self.__imgbody, *new_pos, *new_spd)

            self.__nodes.insert(1, new_node)
        else:
            for i in range(len(self.__nodes) - 1, 0, -1):
                self.__nodes[i].update()
                new_spd = self.__nodes[i - 1].get_spd()
                self.__nodes[i].set_spd(new_spd)

        self.__nodes[0].update()

    def up(self):
        if self.__nodes[0].get_spd() != Vector2(0, gspeed):
            self.__nodes[0].set_spd((0, -45))

    def down(self):
        if self.__nodes[0].get_spd() != Vector2(0, -gspeed):
            self.__nodes[0].set_spd((0, 45))

    def left(self):
        if self.__nodes[0].get_spd() != Vector2(gspeed, 0):
            self.__nodes[0].set_spd((-45, 0))

    def right(self):
        if self.__nodes[0].get_spd() != Vector2(-gspeed, 0):
            self.__nodes[0].set_spd((45, 0))
