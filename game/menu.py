from game import pg,Screen,InterfaceObject,Button

from game.assets import imgsety, imgsetb, imgseto, imgsetp ,imgsnake
from game.assets import crown ,menu_sec , imgsnake_small,jogador_titulo
from game.assets import imgbutton, img_menu_background ,img_ending_screen
from game.assets import maps, img_wait_background
from game.assets import imgkeyboard, imgkeyboard2, imgkeyboard3

from game.constants import left, right, gunity

from pygame.math import Vector2
from pygame.time import Clock

from random import choice

QUIT = 0
MAIN = 1
MULTIPLAYER = 2
MAP_SELECTION = 3
ENDING_SCREEN = 4
CONTROLS = 5

def get_key():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            if event.type == pg.KEYDOWN:
                return event.key

class MainMenu():
    def __init__(self, screen, x=0, y=0):
        self.__pos = Vector2(x, y)
        self.__screen = screen
        self.__background = InterfaceObject(screen, img_menu_background)
        self.__buttons = []
        self.__rect = Vector2(img_menu_background.get_rect().size)
        self.__bound = self.__rect/2
        self.__config = {
            'player_number': 0,
            'players': {
                'sprites': [imgsety, imgsetb, imgseto, imgsetp],
                'controls': [
                    [pg.K_w, pg.K_a, pg.K_s, pg.K_d],
                    [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT],
                    [pg.K_y, pg.K_g, pg.K_h, pg.K_j],
                    [pg.K_KP8, pg.K_KP4, pg.K_KP5, pg.K_KP6]
                ]
            },
            'map': choice(list(maps.values()))
        }

        self.__state = QUIT
        self.main()

    def get_screen(self):
        return self.__screen

    def main (self):
        self.__last_state = self.__state
        self.__state = MAIN

        if self.__last_state in [QUIT, ENDING_SCREEN]:
            pg.mixer.music.load('assets/sounds/intro.wav')
            pg.mixer.music.play(-1)

        self.clear_buttons()

        labels = ['jogar','modo_pratica','controles']

        x = -self.__bound[0] * 0.66
        y = -self.__bound[1] * 0.70

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.307

        y += self.__bound[1] * 0.307

        Button(self, imgbutton['encerrar'], -self.__bound[0] * 0.665, y)

    def multijogadores(self):
        self.__last_state = self.__state
        self.__state = MULTIPLAYER

        self.clear_buttons()

        labels = ['dois_jogadores','tres_jogadores']

        x = -self.__bound[0] * 0.655
        y = -self.__bound[1] * 0.70

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.307

        Button(self, imgbutton['quatro_jogadores'],-self.__bound[0] * 0.664 , -self.__bound[1] * 0.086)
        Button(self, imgbutton['voltar'], -self.__bound[0] * 0.67, +self.__bound[1] * 0.528)

    def map_selection(self):
        self.__last_state = self.__state
        self.__state = MAP_SELECTION

        self.clear_buttons()

        self.__menu_barra = InterfaceObject(self.__background,menu_sec , -self.__bound[0] * 0.088, self.__bound[1] * 0)

        Button(self, imgbutton['mapa_aleatorio'],-self.__bound[0] * 0.655, -self.__bound[1] * 0.70)

        labels = ['eights', 'cross_and_borders','lines']

        x = self.__bound[0] * 0.05
        y = -self.__bound[1] * 0.6

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.58

        Button(self, imgbutton['voltar'], -self.__bound[0] * 0.67, +self.__bound[1] * 0.528)

    def ending_screen(self,winners):
        pg.mixer.music.load('assets/sounds/ending.wav')
        pg.mixer.music.play(0)
        self.__last_state = self.__state
        self.__state = ENDING_SCREEN

        self.__background = InterfaceObject(self.__screen,img_ending_screen)

        x = -self.__rect[0] * 0.1
        y = -self.__rect[1] * 0.24
        delta_y = + self.__rect[1]*0.56/(self.__config['player_number'] + 1)

        for i in range(self.__config['player_number']):
            y = y + delta_y
            InterfaceObject(self.__background,imgsnake[i],x,y)

        x = self.__rect[1]*0.25
        for player_id in winners:
            InterfaceObject(self.__background,crown,x,-self.__rect[1] * 0.24 + (player_id + 1)*delta_y)

        Button(self, imgbutton['menu_principal'], -self.__rect[0] * 0.1, self.__rect[1]*0.365)
        Button(self, imgbutton['encerrar_w'], +self.__rect[0] * 0.15, self.__rect[1]*0.365)

        self.menu_loop()

    def controls(self):
        self.__last_state = self.__state
        self.__state = CONTROLS

        self.clear_buttons()

        self.__menu_barra = InterfaceObject(self.__background, menu_sec,-self.__bound[0] * 0.088, self.__bound[1] * 0)

        inc = 2 * gunity
        incs = [(0, 0), (-inc, +inc), (0, +inc), (+inc, +inc)]

        pos0 = Vector2(-self.__rect[0]*0.35, -self.__rect[1]*0.24)

        Inc = Vector2(self.__rect[0]*0.358, self.__rect[1]*0.38)
        Incs = [(0,0),(Inc[0],0),(0,Inc[1]),Inc]

        playerkeys = self.__config['players']['controls']
        for i in range(4):
            pos1 = pos0 + Incs[i]
            InterfaceObject(self.__background, imgsnake_small[i], *pos1 + Vector2(-self.__rect[0]*0.11,0))
            InterfaceObject(self.__background, jogador_titulo[i], *pos1 + Vector2(0,-self.__rect[1]*0.15))
            for j in range(4):
                pos = pos1 + incs[j]
                imgs = [imgkeyboard[playerkeys[i][j]],imgkeyboard2[playerkeys[i][j]],imgkeyboard3[playerkeys[i][j]]]
                Button(self, imgs, *pos)

        Button(self, imgbutton['voltar'], -self.__rect[0]*0.35, self.__rect[1]*0.37)

    def update(self):
        if self.__state == MAIN:
            # multiplayer
            if self.__buttons[0].check_hover():
                self.multijogadores()

            # single player
            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 1
                self.map_selection()

            # controles
            elif self.__buttons[2].check_hover():
                self.controls()
            # encerrar
            elif self.__buttons[3].check_hover():
                self.__state = QUIT

        elif self.__state == MULTIPLAYER:
            if self.__buttons[0].check_hover():
                self.__config['player_number'] = 2
                self.map_selection()

            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 3
                self.map_selection()

            elif self.__buttons[2].check_hover():
                self.__config['player_number'] = 4
                self.map_selection()

            elif self.__buttons[3].check_hover():
                self.main()

        elif self.__state == MAP_SELECTION:
            # mapa aleatorio
            if self.__buttons[0].check_hover():
                self.__config['map'] = choice(list(maps.values()))
                self.__state = QUIT
            # eights
            elif self.__buttons[1].check_hover():
                self.__config['map'] = maps['eights']
                self.__state = QUIT
            # cross and borders
            elif self.__buttons[2].check_hover():
                self.__config['map'] = maps['cross_and_borders']
                self.__state = QUIT
            # lines
            elif self.__buttons[3].check_hover():
                self.__config['map'] = maps['lines']
                self.__state = QUIT
            # voltar
            elif self.__buttons[4].check_hover():
                self.__config['player_number'] = 0
                self.__menu_barra.destroy()
                if self.__last_state == MULTIPLAYER:
                    self.multijogadores()
                elif self.__last_state == MAIN:
                    self.main()

        elif self.__state == ENDING_SCREEN:
            # menu principal
            if self.__buttons[0].check_hover():
                self.__config['player_number'] = 0
                self.__config['map'] = choice(list(maps.values()))
                self.__background.destroy()
                self.__background = InterfaceObject(self.__screen, img_menu_background)
                self.main()
            # encerrar
            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 0
                self.__state = QUIT

        elif self.__state == CONTROLS:
            if self.__buttons[16].check_hover():
                self.__background.remove_all_slaves()
                self.main()
            else:
                for i in range(16):
                    if self.__buttons[i].check_hover():
                        n = i//4
                        k = i % 4
                        controls = self.__config['players']['controls']
                        key = get_key()
                        assigned = False

                        for a in range(len(controls)):
                            for b in range(4):
                                if key == controls[a][b]:
                                    assigned = True
                                    n1 = a
                                    k1 = b

                        if not key:
                            self.__config['player_number'] = 0
                            self.__state = QUIT
                        elif assigned:
                            key1 = controls[n][k]
                            controls[n1][k1] = key1
                            imgs = [imgkeyboard[key1],imgkeyboard2[key1],imgkeyboard3[key1]]
                            self.__buttons[n1*4 + k1].set_imglist(imgs)

                            controls[n][k] = key
                            imgs = [imgkeyboard[key],imgkeyboard2[key],imgkeyboard3[key]]
                            self.__buttons[i].set_imglist(imgs)
                        elif key in imgkeyboard.keys():
                            controls[n][k] = key
                            imgs = [imgkeyboard[key],imgkeyboard2[key],imgkeyboard3[key]]
                            self.__buttons[i].set_imglist(imgs)

    def add_button(self, button):
        self.__buttons.append(button)

    def clear_buttons(self):
        for button in self.__buttons:
            button.destroy()
        self.__buttons.clear()

    def menu_loop(self):
        clock = Clock()

        while self.__state != QUIT:
            self.update()
            clock.tick(30)
            self.__screen.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__config['player_number'] = 0
                    self.__state = QUIT

        self.clear_buttons()
        self.__background.destroy()
        return self.__config
