from game import pg,Screen,InterfaceObject,imgbutton
from pygame.math import Vector2
from pygame.time import Clock


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


class MainMenu(InterfaceObject):
    def __init__(self, master, x=0, y=0):
        self.__pos = Vector2(x, y)
        self.__master = master
        self.__img = pg.image.load('assets/img/menu_background.png');
        self.__slaves = []
        self.__rect = Vector2(self.__img.get_rect().size)
        self.__config = {"players": []}
        self.__menuState = 0;           # state -1 = quit , state 0 = main_menu , state 1 = num jogadores

        master.add_slave(self)

    def update(self):
        if self.__menuState == 1:
            ## single player
            if self.__slaves[0].check_hover() == True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__menuState = 5;

            ##multiplayer
            elif self.__slaves[1].check_hover()== True:
               self.multijogadores();
            ##opcoes
            elif self.__slaves[2].check_hover()== True:
              print("menu opcoes")
            ## extras ?
            elif self.__slaves[3].check_hover()== True:
              print("pq coloquei extras")
            ## encerrar
            elif self.__slaves[4].check_hover()== True:
                self.__menuState = -1;

        ## menu multiplayer
        if self.__menuState == 2:
            if self.__slaves[0].check_hover() == True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__config["players"].append([pg.K_w, pg.K_a, pg.K_s, pg.K_d])
                self.__menuState = 5;
                print("dois jogadores")
            elif self.__slaves[1].check_hover()== True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__config["players"].append([pg.K_w, pg.K_a, pg.K_s, pg.K_d])
                self.__config["players"].append([pg.K_y, pg.K_g, pg.K_h, pg.K_j])
                self.__menuState = 5;
                print("tres jogadores")
            elif self.__slaves[2].check_hover()== True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__config["players"].append([pg.K_w, pg.K_a, pg.K_s, pg.K_d])
                self.__config["players"].append([pg.K_y, pg.K_g, pg.K_h, pg.K_j])
                self.__config["players"].append([pg.K_KP8, pg.K_KP4, pg.K_KP5, pg.K_KP6])
                self.__menuState = 5;

                print("quatro jogadores")
            elif self.__slaves[3].check_hover()== True:
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

        jogador_unicoImg = pg.image.load('assets/img/buttons/jogador_unico.png')
        jogador_unicoImg2 = pg.image.load('assets/img/buttons/jogador_unico2.png')
        jogador_unicoImg3 = pg.image.load('assets/img/buttons/jogador_unico3.png')
        jogador_unico = Button(self, imgbutton["jogador_unico"], self.__rect[0]*0.019,self.__rect[1]*0.13)

        multijogadorImg = pg.image.load('assets/img/buttons/multijogadores.png')
        multijogadorImg2 = pg.image.load('assets/img/buttons/multijogadores2.png')
        multijogadorImg3 = pg.image.load('assets/img/buttons/multijogadores3.png')
        multijogador = Button(self, imgbutton["multijogadores"], self.__rect[0] * 0.015, self.__rect[1] * 0.29)

        opcoesImg = pg.image.load('assets/img/buttons/opcoes.png')
        opcoesImg2 = pg.image.load('assets/img/buttons/opcoes2.png')
        opcoesImg3 = pg.image.load('assets/img/buttons/opcoes3.png')
        opcoes = Button(self, imgbutton["opcoes"], self.__rect[0]*0.045,self.__rect[1]*0.43)

        extraImg = pg.image.load('assets/img/buttons/extra.png')
        extraImg2 = pg.image.load('assets/img/buttons/extra2.png')
        extraImg3 = pg.image.load('assets/img/buttons/extra3.png')
        extra = Button(self, imgbutton["extra"], self.__rect[0]*0.0475,self.__rect[1]*0.595)

        encerrarImg = pg.image.load('assets/img/buttons/encerrar.png')
        encerrarImg2 = pg.image.load('assets/img/buttons/encerrar2.png')
        encerrarImg3 = pg.image.load('assets/img/buttons/encerrar3.png')
        encerrar = Button(self, imgbutton["encerrar"], self.__rect[0]*0.035,self.__rect[1]*0.745)

    def multijogadores(self):

        del self.__slaves[0:5]

        self.__menuState = 2;

        dois_jogadoresImg = pg.image.load('assets/img/buttons/dois_jogadores.png')
        dois_jogadoresImg2 = pg.image.load('assets/img/buttons/dois_jogadores2.png')
        dois_jogadoresImg3 = pg.image.load('assets/img/buttons/dois_jogadores3.png')
        dois_jogadores = Button(self, imgbutton["dois_jogadores"], self.__rect[0] * 0.035, self.__rect[1] * 0.13)

        tres_jogadoresImg = pg.image.load('assets/img/buttons/tres_jogadores.png')
        tres_jogadoresImg2 = pg.image.load('assets/img/buttons/tres_jogadores2.png')
        tres_jogadoresImg3 = pg.image.load('assets/img/buttons/tres_jogadores3.png')
        tres_jogadores = Button(self, imgbutton["tres_jogadores"], self.__rect[0] * 0.031, self.__rect[1] * 0.29)

        quatro_jogadoresImg = pg.image.load('assets/img/buttons/quatro_jogadores.png')
        quatro_jogadoresImg2 = pg.image.load('assets/img/buttons/quatro_jogadores2.png')
        quatro_jogadoresImg3 = pg.image.load('assets/img/buttons/quatro_jogadores3.png')
        quatro_jogadores = Button(self, imgbutton["quatro_jogadores"], self.__rect[0] * 0.019, +self.__rect[1] *0.43)

        voltarImg = pg.image.load('assets/img/buttons/voltar.png')
        voltarImg2 = pg.image.load('assets/img/buttons/voltar2.png')
        voltarImg3 = pg.image.load('assets/img/buttons/voltar3.png')
        voltar = Button(self, imgbutton["voltar"], self.__rect[0] * 0.072, self.__rect[1] * 0.745)


    def menu_loop(self):
        clock = Clock()
        self.main();

        while self.__menuState != -1:
            self.update();
            clock.tick(30)
            self.__master.update();

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__menuState = -1
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.__menuState = -1
            if self.__menuState == 5 :
                return self.__config;