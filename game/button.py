from game import pg,Screen,InterfaceObject
from game.assets import imgbutton
from pygame.math import Vector2


class Button(InterfaceObject):
    def __init__(self, master,imglist, abs_x=0, abs_y=0):
        self.__abs_pos = Vector2(abs_x, abs_y)
        self.__master = master
        self.__imglist = imglist;
        self.__img = imglist[0]
        self.__rect = Vector2(imglist[0].get_rect().size)
        self.__buttonState = 0;            ## 0 : unpressed and unhovered 1 : unpressed and hovered 2 : pressed

        master.add_slave(self)

    def get_abs_position(self):
        return self.__abs_pos;

    def get_img(self):
        return self.__img

    def get_blit(self):
        return  [(self.get_img(), self.get_abs_position())]

    def check_hover(self):

        self.__img = self.__imglist[0];
        mouse = pg.mouse.get_pos();
        if self.__abs_pos[0] < mouse[0] < self.__abs_pos[0] + self.__rect[0] and self.__abs_pos[1] < mouse[1] < self.__abs_pos[1] + self.__rect[1]:
            click = pg.mouse.get_pressed();
            if click[0] == 1:
                self.__img = self.__imglist[2];
                self.__buttonState = 2;
            else:
                self.__img = self.__imglist[1];
            if click[0] == 0 and self.__buttonState == 2:
                self.__buttonState = 0;
                return True;
        else:
            self.__buttonState = 0;
        return False;
