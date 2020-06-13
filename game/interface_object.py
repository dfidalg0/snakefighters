from game import pg
from pygame.math import Vector2


class InterfaceObject:
    def __init__(self, master, img, x=0, y=0):
        self.__pos = Vector2(x, y)
        self.__master = master
        self.__img = img
        self.__slaves = []
        self.__rect = Vector2(img.get_rect().size)

        master.add_slave(self)

    # Função de atualização de comportamento
    def update(self):
        pass

    def get_rect(self):
        return self.__rect

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
        return self.aux_abs_pos() - self.__rect / 2

    def aux_abs_pos(self):
        return self.__master.aux_abs_pos() + self.__pos

    # Posição do objeto em relação ao mestre
    def get_pos(self):
        return self.__pos

    def set_pos(self, pos):
        self.__pos = Vector2(pos)

    def get_img(self):
        return self.__img

    def set_img(self, img):
        self.__img = img
        self.__rect = Vector2(img.get_rect().size)

    def get_slaves(self):
        return self.__slaves

    def add_slave(self, slave):
        self.__slaves.append(slave)

    def remove_slave(self, slave):
        self.__slaves.remove(slave)

    def remove_all_slaves(self):
        del self.__slaves[:]

    def destroy(self):
        for slave in self.__slaves:
            slave.destroy()

        self.__master.remove_slave(self)
