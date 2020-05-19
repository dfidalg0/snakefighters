from game import pg
from pygame.math import Vector2

class InterfaceObject:
    def __init__ (self, master, img, x=0, y=0):
        self.__pos = Vector2(x,y)
        self.__master = master
        self.__img = img
        self.__slaves = set()
        self.__rect = Vector2(img.get_rect().size)

        master.add_slave(self)

    # Função de atualização de comportamento
    def update (self):
        pass

    # Parâmetros para impressão de um objeto e todos os seus slaves na tela
    def get_blit(self):
        return_list = [(self.get_img(), self.get_abs_position())]
        for slave in self.get_slaves():
            return_list += slave.get_blit()

        return return_list

    # Posição do objeto em relação ao centro da tela
    def get_screen_position(self):
        return self.__master.get_screen_position() + self.__pos

    # Posição do início do retângulo do objeto no referencial absoluto do Pygame
    def get_abs_position(self):
        return self.__master.get_abs_position() + self.__pos - self.__rect/2

    # Posição do objeto em relação ao mestre
    def get_position (self):
        return self.__pos

    def set_position (self, pos):
        self.__pos = Vector2(pos)

    def get_img(self):
        return self.__img

    def set_img(self,img):
        self.__img = img

    def get_slaves(self):
        return self.__slaves

    def add_slave(self, slave):
        self.__slaves.add(slave)
