from game import pg,Screen,InterfaceObject
from pygame.math import Vector2


class Button(InterfaceObject):
    def __init__(self, master, img, x=0, y=0):
        super().__init__(master, img, x, y)

    def update(self):
        imag = self.get_img();
        self.__rect = Vector2(imag.get_rect().size)
        limite = self.get_abs_position();
        # screen = self.get_master().get_master().get_screen();
        # pos = self.get_abs_position()

        # pg.draw.rect(screen,(0, 0, 0), (pos[0],pos[1],self.__rect[0],self.__rect[1]))


        mouse = pg.mouse.get_pos();
        if limite[0] < mouse[0] < limite[0] + self.__rect[0] and limite[1] < mouse[1] < limite[1] + self.__rect[1]:
            click = pg.mouse.get_pressed();
            if click[0] == 1:
                return True;
        return False;


class MainMenu(InterfaceObject):
    def __init__(self, master, x=0, y=0):
        self.__pos = Vector2(x, y)
        self.__master = master
        self.__img = pg.image.load('assets/img/menu_background.png');
        self.__slaves = []
        self.__rect = Vector2(self.__img.get_rect().size)
        self.__menuState = 0;

        master.add_slave(self)

    def update(self):
        if self.__menuState == 1:
            if self.__slaves[0].update == True:
                print("game init")
            elif self.__slaves[1].update()== True:
               self.multijogadores();
            elif self.__slaves[2].update()== True:
              print("menu opcoes")
            elif self.__slaves[3].update()== True:
              print("pq coloquei extras")
            elif self.__slaves[4].update()== True:
              print("calma mano,jogo mo bom")
        if self.__menuState == 2:
            if self.__slaves[0].update == True:
                print("dois jogadores")
            elif self.__slaves[1].update()== True:
                print("tres jogadores")
            elif self.__slaves[2].update()== True:
              print("quatro jogadores")
            elif self.__slaves[3].update()== True:
              self.main();


    # Função de atualização de comportamento
    def get_img(self):
        return self.__img

    def aux_abs_pos(self):
        return self.__master.aux_abs_pos() + self.__pos;

    def get_abs_position(self):
        return self.aux_abs_pos() - self.__rect / 2

    def get_slaves(self):
        return self.__slaves

    def add_slave(self, slave):
        self.__slaves.append(slave)

    def remove_slave(self, slave):
        self.__slaves.remove(slave)

    def main(self):

        del self.__slaves[0:5]

        self.__menuState = 1;

        jogador_unicoImg = pg.image.load('assets/img/jogador_unico.png')
        jogador_unico = Button(self,jogador_unicoImg,-self.__rect[0]*0.34,-self.__rect[1]*0.3)

        multijogadorImg = pg.image.load('assets/img/multijogadores.png')
        multijogador = Button(self, multijogadorImg, -self.__rect[0] * 0.34, -self.__rect[1] * 0.15)

        opcoesImg = pg.image.load('assets/img/opcoes.png')
        opcoes = Button(self, opcoesImg, -self.__rect[0] * 0.34, +self.__rect[1] * 0)

        extraImg = pg.image.load('assets/img/extra.png')
        extra = Button(self, extraImg, -self.__rect[0] * 0.34, +self.__rect[1] * 0.15)

        encerrarImg = pg.image.load('assets/img/encerrar.png')
        encerrar = Button(self, encerrarImg, -self.__rect[0] * 0.34, +self.__rect[1] * 0.3)

    def multijogadores(self):

        del self.__slaves[0:5]

        self.__menuState = 2;

        dois_jogadoresImg = pg.image.load('assets/img/dois_jogadores.png')
        dois_jogadores = Button(self, dois_jogadoresImg, -self.__rect[0] * 0.34, -self.__rect[1] * 0.3)

        tres_jogadoresImg = pg.image.load('assets/img/tres_jogadores.png')
        tres_jogadores = Button(self, tres_jogadoresImg, -self.__rect[0] * 0.34, -self.__rect[1] * 0.15)

        quatro_jogadoresImg = pg.image.load('assets/img/quatro_jogadores.png')
        quatro_jogadores = Button(self, quatro_jogadoresImg, -self.__rect[0] * 0.34, +self.__rect[1] * 0)

        voltarImg = pg.image.load('assets/img/voltar.png')
        voltar = Button(self, voltarImg, -self.__rect[0] * 0.34, +self.__rect[1] * 0.30)


    def get_master(self):
        return self.__master

    def options(self):
        pass