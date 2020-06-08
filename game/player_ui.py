from game import pg, InterfaceObject
from game.assets import dummy_surface, skull, heart
from game.constants import gunity, max_health
from math import inf

padding = 2
size = 3*gunity//2

skull = pg.transform.scale(skull,(size,size))
heart = pg.transform.scale(heart,(size,size))

class PlayerUI (InterfaceObject):
    def __init__(self,master,player,x,y):
        dummy_surface.convert()
        dummy_surface.set_alpha(0)
        super().__init__(master, dummy_surface, x, y)
        self.__player = player
        self.__sign = -1 if player.get_id() % 2 == 1 else +1

        s1 = size + 2*padding
        self.__pbox = pg.Surface((s1,size + 2*padding))
        s2 = max_health*size + (max_health+1)*padding
        self.__hbox = pg.Surface((s2,size + 2*padding))
        self.__hbox.set_colorkey((0,0,0))

        self.__avatar = InterfaceObject(self,self.__pbox)
        self.__hearts = InterfaceObject(self,self.__hbox,self.__sign*(s1+s2)//2)

        self.update()

    def update(self):
        if self.__player.get_health() > 0:
            img_avatar = self.__player.get_head().get_img()
            img_avatar = pg.transform.scale(img_avatar,(size,size))
        else:
            img_avatar = skull
        self.__pbox.fill((43, 45, 43))
        self.__pbox.blit(img_avatar,(padding,padding))

        self.__avatar.set_img(self.__pbox)

        health = self.__player.get_health()
        if health == inf:
            health = self.__player.get_virtual_health()
            health = int(health)

        self.__hbox.fill((0,0,0))

        for i in range(health):
            x0 = 0 if self.__sign == 1 else (max_health-1)*size + max_health*padding
            self.__hbox.blit(heart,(x0 + i*self.__sign*(size+padding),padding))

        self.__hearts.set_img(self.__hbox)
