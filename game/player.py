from game import pg, Screen, GameObject, gspeed
from pygame.math import Vector2


class Player:
    def __init__(self, screen, imgset, x, y, orient):
        self.__screen = screen
        self.__imgset = imgset
        if orient == 1:
            self.__imghead = imgset['HEAD_R']
            self.__imgbody = imgset['BODY_R']
            self.__imgtail = imgset['TAIL_R']
        elif orient == -1:
            self.__imghead = imgset['HEAD_L']
            self.__imgbody = imgset['BODY_L']
            self.__imgtail = imgset['TAIL_L']
        head = GameObject(screen, self.__imghead, x, y, gspeed * orient, 0)
        body = GameObject(screen, self.__imgbody, x - 45 * orient, y, gspeed * orient, 0)
        tail = GameObject(screen, self.__imgtail, x - 45 * orient * 2, y, gspeed * orient, 0)
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

            if new_spd == Vector2(0, -gspeed):
                self.__imgbody = self.__imgset['BODY_U']
            elif new_spd == Vector2(0, gspeed):
                self.__imgbody = self.__imgset['BODY_D']
            elif new_spd == Vector2(-gspeed, 0):
                self.__imgbody = self.__imgset['BODY_L']
            elif new_spd == Vector2(gspeed, 0):
                self.__imgbody = self.__imgset['BODY_R']

            new_node = GameObject(self.__screen, self.__imgbody, *new_pos, *new_spd)

            self.__nodes.insert(1, new_node)
        else:
            for i in range(len(self.__nodes) - 1, 0, -1):
                new_spd = self.__nodes[i - 1].get_spd()

                if i != len(self.__nodes) - 1:
                    if self.__nodes[i+1].get_spd() == self.__nodes[i-1].get_spd():
                        if new_spd == Vector2(0, -gspeed):
                            self.__nodes[i].set_img(self.__imgset['BODY_U'])
                        elif new_spd == Vector2(0, gspeed):
                            self.__nodes[i].set_img(self.__imgset['BODY_D'])
                        elif new_spd == Vector2(-gspeed, 0):
                            self.__nodes[i].set_img(self.__imgset['BODY_L'])
                        elif new_spd == Vector2(gspeed, 0):
                            self.__nodes[i].set_img(self.__imgset['BODY_R'])
                    else:
                        if ((self.__nodes[i + 1].get_spd() == Vector2(0, gspeed) and
                            self.__nodes[i - 1].get_spd() == Vector2(gspeed, 0)) or
                            (self.__nodes[i + 1].get_spd() == Vector2(-gspeed, 0) and
                             self.__nodes[i - 1].get_spd() == Vector2(0, -gspeed))):
                            self.__nodes[i].set_img(self.__imgset['TURN_RU'])
                        elif ((self.__nodes[i + 1].get_spd() == Vector2(0, -gspeed) and
                              self.__nodes[i - 1].get_spd() == Vector2(gspeed, 0)) or
                              (self.__nodes[i + 1].get_spd() == Vector2(-gspeed, 0) and
                               self.__nodes[i - 1].get_spd() == Vector2(0, gspeed))):
                            self.__nodes[i].set_img(self.__imgset['TURN_RD'])
                        elif ((self.__nodes[i + 1].get_spd() == Vector2(0, gspeed) and
                              self.__nodes[i - 1].get_spd() == Vector2(-gspeed, 0)) or
                              (self.__nodes[i + 1].get_spd() == Vector2(gspeed, 0) and
                               self.__nodes[i - 1].get_spd() == Vector2(0, -gspeed))):
                            self.__nodes[i].set_img(self.__imgset['TURN_LU'])
                        elif ((self.__nodes[i + 1].get_spd() == Vector2(0, -gspeed) and
                              self.__nodes[i - 1].get_spd() == Vector2(-gspeed, 0)) or
                              (self.__nodes[i + 1].get_spd() == Vector2(gspeed, 0) and
                               self.__nodes[i - 1].get_spd() == Vector2(0, gspeed))):
                            self.__nodes[i].set_img(self.__imgset['TURN_LD'])

                else:
                    if new_spd == Vector2(0, -gspeed):
                        self.__nodes[i].set_img(self.__imgset['TAIL_U'])
                    elif new_spd == Vector2(0, gspeed):
                        self.__nodes[i].set_img(self.__imgset['TAIL_D'])
                    elif new_spd == Vector2(-gspeed, 0):
                        self.__nodes[i].set_img(self.__imgset['TAIL_L'])
                    elif new_spd == Vector2(gspeed, 0):
                        self.__nodes[i].set_img(self.__imgset['TAIL_R'])

                self.__nodes[i].update()
                self.__nodes[i].set_spd(new_spd)

        self.__nodes[0].update()

    def up(self):
        if self.__nodes[0].get_spd() != Vector2(0, gspeed):
            self.__nodes[0].set_spd((0, -gspeed))
            self.__nodes[0].set_img(self.__imgset['HEAD_U'])

    def down(self):
        if self.__nodes[0].get_spd() != Vector2(0, -gspeed):
            self.__nodes[0].set_spd((0, gspeed))
            self.__nodes[0].set_img(self.__imgset['HEAD_D'])

    def left(self):
        if self.__nodes[0].get_spd() != Vector2(gspeed, 0):
            self.__nodes[0].set_spd((-gspeed, 0))
            self.__nodes[0].set_img(self.__imgset['HEAD_L'])

    def right(self):
        if self.__nodes[0].get_spd() != Vector2(-gspeed, 0):
            self.__nodes[0].set_spd((gspeed, 0))
            self.__nodes[0].set_img(self.__imgset['HEAD_R'])
