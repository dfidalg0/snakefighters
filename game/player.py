from game import pg, Screen, GameObject
from game.constants import gspeed, gunity
from pygame.math import Vector2


class Player:
    def __init__(self, screen, imgset, x, y, orient):
        self.__screen = screen
        self.__imgset = imgset
        if orient == 1:
            imghead = imgset['HEAD_R']
            imgbody = imgset['BODY_R']
            imgtail = imgset['TAIL_R']
        elif orient == -1:
            imghead = imgset['HEAD_L']
            imgbody = imgset['BODY_L']
            imgtail = imgset['TAIL_L']
        head = GameObject(screen, imghead, x, y, gspeed * orient, 0)
        body = GameObject(screen, imgbody, x - gunity * orient, y, gspeed * orient, 0)
        tail = GameObject(screen, imgtail, x - gunity * orient * 2, y, gspeed * orient, 0)
        self.__nodes = [head, body, tail]
        self.__grow = False
        self.__health = 1
        self.__effect = None

    def get_nodes(self):
        return self.__nodes

    def get_head(self):
        return self.__nodes[0]

    def get_controls(self):
        return [self.up, self.left, self.down, self.right]

    def grow_size(self):
        self.__grow = True

    def get_imgset(self):
        return self.__imgset

    def set_imgset(self,imgset):
        self.__imgset = imgset

    def get_health(self):
        return self.__health.real

    def get_virtual_health(self):
        return self.__health.imag

    def set_health(self,health):
        self.__health = health

    def inc_health(self,inc=1):
        self.__health += inc

    def dec_health(self,dec=1):
        self.__health -= dec

    def update(self):
        if self.__effect:
            self.__effect()

        if self.__grow:
            self.__grow = False

            old_spd = self.__nodes[1].get_spd()
            new_spd = self.__nodes[0].get_spd()

            new_pos = self.__nodes[0].get_pos()

            new_img = self.__get_img_body(old_spd, new_spd)

            new_node = GameObject(self.__screen, new_img, *new_pos, *new_spd)

            self.__nodes.insert(1, new_node)
        else:
            new_spd = self.__nodes[-2].get_spd()

            new_img = self.__get_img_tail(new_spd)

            self.__nodes[-1].set_img(new_img)
            self.__nodes[-1].update()
            self.__nodes[-1].set_spd(new_spd)

            for i in range(len(self.__nodes) - 2, 0, -1):
                new_spd = self.__nodes[i - 1].get_spd()
                old_spd = self.__nodes[i].get_spd()

                new_img = self.__get_img_body(old_spd, new_spd)

                self.__nodes[i].update()
                self.__nodes[i].set_img(new_img)
                self.__nodes[i].set_spd(new_spd)

        new_spd = self.__nodes[0].get_spd()
        new_img = self.__get_img_head(new_spd)
        self.__nodes[0].update()
        self.__nodes[0].set_img(new_img)

    def up(self):
        if self.__nodes[0].get_spd().y == 0:
            self.__nodes[0].set_spd((0, -gspeed))

    def down(self):
        if self.__nodes[0].get_spd().y == 0:
            self.__nodes[0].set_spd((0, gspeed))

    def left(self):
        if self.__nodes[0].get_spd().x == 0:
            self.__nodes[0].set_spd((-gspeed, 0))

    def right(self):
        if self.__nodes[0].get_spd().x == 0:
            self.__nodes[0].set_spd((gspeed, 0))

    def collision(self,obj):
        i0 = 4 if self.__nodes[0] == obj else 0
        for i in range(i0,len(self.__nodes)):
            if self.__nodes[i].collision(obj):
                return True

        return False

    def destroy(self):
        for i in range(len(self.__nodes)):
            self.__nodes[i].destroy()

    def add_effect(self,effect):
        self.__effect = effect

    def clear_effect(self):
        if self.__effect:
            self.__effect(end=True)

        self.__effect = None

    # Funções auxiliares da classe
    def __get_img_body(self, old_spd, new_spd):
        if old_spd == new_spd:
            if new_spd.y < 0:
                img = self.__imgset['BODY_U']
            elif new_spd.y > 0:
                img = self.__imgset['BODY_D']
            elif new_spd.x < 0:
                img = self.__imgset['BODY_L']
            elif new_spd.x > 0:
                img = self.__imgset['BODY_R']
        else:
            if (old_spd.y > 0 and new_spd.x > 0) or (old_spd.x < 0 and new_spd.y < 0):
                img = self.__imgset['TURN_RU']
            elif (old_spd.y < 0 and new_spd.x > 0) or (old_spd.x < 0 and new_spd.y > 0):
                img = self.__imgset['TURN_RD']
            elif (old_spd.y > 0 and new_spd.x < 0) or (old_spd.x > 0 and new_spd.y < 0):
                img = self.__imgset['TURN_LU']
            elif (old_spd.y < 0 and new_spd.x < 0) or (old_spd.x > 0 and new_spd.y > 0):
                img = self.__imgset['TURN_LD']

        return img

    def __get_img_head(self, new_spd):
        if new_spd.y < 0:
            img = self.__imgset['HEAD_U']
        elif new_spd.y > 0:
            img = self.__imgset['HEAD_D']
        elif new_spd.x < 0:
            img = self.__imgset['HEAD_L']
        elif new_spd.x > 0:
            img = self.__imgset['HEAD_R']

        return img

    def __get_img_tail(self, new_spd):
        if new_spd.y < 0:
            img = self.__imgset['TAIL_U']
        elif new_spd.y > 0:
            img = self.__imgset['TAIL_D']
        elif new_spd.x < 0:
            img = self.__imgset['TAIL_L']
        elif new_spd.x > 0:
            img = self.__imgset['TAIL_R']

        return img
