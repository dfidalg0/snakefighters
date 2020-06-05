from game import pg,Screen,InterfaceObject,imgbutton,Button
from pygame.math import Vector2
from pygame.time import Clock


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

            elif self.__slaves[1].check_hover()== True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__config["players"].append([pg.K_w, pg.K_a, pg.K_s, pg.K_d])
                self.__config["players"].append([pg.K_y, pg.K_g, pg.K_h, pg.K_j])
                self.__menuState = 5;

            elif self.__slaves[2].check_hover()== True:
                self.__config["players"].append([pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
                self.__config["players"].append([pg.K_w, pg.K_a, pg.K_s, pg.K_d])
                self.__config["players"].append([pg.K_y, pg.K_g, pg.K_h, pg.K_j])
                self.__config["players"].append([pg.K_KP8, pg.K_KP4, pg.K_KP5, pg.K_KP6])
                self.__menuState = 5;

            elif self.__slaves[3].check_hover()== True:
              self.main();


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

        jogador_unico = Button(self, imgbutton["jogador_unico"], self.__rect[0]*0.019,self.__rect[1]*0.13)

        multijogador = Button(self, imgbutton["multijogadores"], self.__rect[0] * 0.015, self.__rect[1] * 0.29)

        opcoes = Button(self, imgbutton["opcoes"], self.__rect[0]*0.045,self.__rect[1]*0.43)

        extra = Button(self, imgbutton["extra"], self.__rect[0]*0.0475,self.__rect[1]*0.595)

        encerrar = Button(self, imgbutton["encerrar"], self.__rect[0]*0.035,self.__rect[1]*0.745)

    def multijogadores(self):

        del self.__slaves[0:5]

        self.__menuState = 2;

        dois_jogadores = Button(self, imgbutton["dois_jogadores"], self.__rect[0] * 0.035, self.__rect[1] * 0.13)

        tres_jogadores = Button(self, imgbutton["tres_jogadores"], self.__rect[0] * 0.031, self.__rect[1] * 0.29)

        quatro_jogadores = Button(self, imgbutton["quatro_jogadores"], self.__rect[0] * 0.019, +self.__rect[1] *0.43)

        voltar = Button(self, imgbutton["voltar"], self.__rect[0] * 0.072, self.__rect[1] * 0.745)


    ## obs.: acho que essa função deveria ficar na game_engine e pausar enquanto da pra enxergar os players e o mapa
    ## fonte provisória pq provavelmente vai ficar na game engine dps
    def wait_to_init(self,tempo_s):
        del self.__slaves[0:5]
        self.__img = pg.image.load('assets/img/waiting_screen.png')

        pg.font.init()
        fonte = pg.font.SysFont('tahoma',65)
        jogo_comecIMG = fonte.render("Jogo começa em ",True,(255,255,255))
        jogo_comec = InterfaceObject(self,jogo_comecIMG,0,-self.__rect[1]*0.1)
        print(pg.font.get_fonts());

        for i in range(tempo_s,0,-1):
            segundosIMG = fonte.render(str(i) +" segundos...",True,(255,255,255))
            segundosIMG = InterfaceObject(self,segundosIMG,0,self.__rect[1]*0.08)
            self.__master.update();
            pg.time.wait(1000);
            segundosIMG.destroy();


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