from game import pg,Screen,InterfaceObject
from game.assets import imgbutton
from pygame.math import Vector2

UNP_UNH = 0  # Unpressed and unhovered
UNP_HOV = 1  # Unpressed and hovered
PRESSED = 2  # Pressed

class Button(InterfaceObject):
    def __init__(self, menu,imglist, x=0, y=0):
        master = menu.get_screen()
        super().__init__(master,imglist[0],x,y)
        self.__abs_pos = self.get_abs_position()
        self.__imglist = imglist
        self.__state = UNP_UNH

        menu.add_button(self)

    def set_imglist(self,imglist):
        self.__imglist = imglist
        self.set_img(imglist[UNP_UNH])

    def check_hover(self):
        rect = self.get_rect()
        self.set_img(self.__imglist[UNP_UNH])
        mouse = pg.mouse.get_pos()
        mouse = Vector2(mouse)
        if self.__abs_pos < mouse.elementwise() < self.__abs_pos + rect:
            click = pg.mouse.get_pressed()[0]
            if click:
                self.set_img(self.__imglist[PRESSED])
                self.__state = PRESSED
            elif self.__state == PRESSED:
                self.__state = UNP_UNH
                return True
            else:
                self.set_img(self.__imglist[UNP_HOV])
        else:
            self.__state = 0
        return False
