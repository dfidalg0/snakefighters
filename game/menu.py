from game import pg,Screen,InterfaceObject,Button
from game.assets import imgsety, imgsetb, imgseto, imgsetp
from game.assets import imgbutton, img_menu_background
from game.assets import maps
from game.constants import left, right, gunity
from pygame.math import Vector2
from pygame.time import Clock
from random import choice

QUIT = 0
MAIN = 1
MULTIPLAYER = 2
MAP_SELECTION = 3

default_sprites = [imgsety, imgsetb, imgseto, imgsetp]
default_orientations = [1,-1,1,-1]
default_positions = [
    (-10 * gunity, -5 * gunity),
    (+10 * gunity, -5 * gunity),
    (-10 * gunity, +5 * gunity),
    (+10 * gunity, +5 * gunity)
]
default_controls = [
    [pg.K_w, pg.K_a, pg.K_s, pg.K_d],
[pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT],
    [pg.K_y, pg.K_g, pg.K_h, pg.K_j],
    [pg.K_KP8, pg.K_KP4, pg.K_KP5, pg.K_KP6]
]

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
                'sprites': [],
                'orientations': [],
                'positions': [],
                'controls': []
            }
        }

        self.main()

    def get_screen(self):
        return self.__screen

    def main (self):
        self.__state = MAIN

        self.clear_buttons()

        labels = ['jogar','modo_pratica','opcoes','extra']

        x = -self.__bound[0] * 0.66
        y = -self.__bound[1] * 0.70

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.307

        Button(self, imgbutton['encerrar'], -self.__bound[0] * 0.665, y)

    def multijogadores(self):
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
        self.__state = MAP_SELECTION

        self.clear_buttons()

        Button(self, imgbutton['menu_sec'], -self.__bound[0] * 0.088, self.__bound[1] * 0)

        Button(self, imgbutton['mapa_aleatorio'],-self.__bound[0] * 0.655, -self.__bound[1] * 0.70)

        labels = ['eights', 'cross_and_borders','lines']

        x = self.__bound[0] * 0.05
        y = -self.__bound[1] * 0.6

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.58


        Button(self, imgbutton['voltar'], -self.__bound[0] * 0.67, +self.__bound[1] * 0.528)



    def update(self):
        if self.__state == MAIN:
            # multiplayer
            if self.__buttons[0].check_hover():
                self.multijogadores()

            # single player
            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 1
                self.__config['players']['sprites'].append(default_sprites[0])
                self.__config['players']['orientations'].append(default_orientations[0])
                self.__config['players']['positions'].append(default_positions[0])
                self.__config['players']['controls'].append(default_controls[0])
                self.map_selection()

            # opcoes
            elif self.__buttons[2].check_hover():
                print("opcoes")
            # extras ?
            elif self.__buttons[3].check_hover():
                print("extras")
            # encerrar
            elif self.__buttons[4].check_hover():
                self.__state = QUIT

        if self.__state == MULTIPLAYER:
            if self.__buttons[0].check_hover():
                self.__config['player_number'] = 2
                for i in range(2):
                    self.__config['players']['sprites'].append(default_sprites[i])
                    self.__config['players']['orientations'].append(default_orientations[i])
                    self.__config['players']['positions'].append(default_positions[i])
                    self.__config['players']['controls'].append(default_controls[i])
                self.map_selection()


            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 3
                for i in range(3):
                    self.__config['players']['sprites'].append(default_sprites[i])
                    self.__config['players']['orientations'].append(default_orientations[i])
                    self.__config['players']['positions'].append(default_positions[i])
                    self.__config['players']['controls'].append(default_controls[i])
                self.map_selection()


            elif self.__buttons[2].check_hover():
                self.__config['player_number'] = 4
                for i in range(4):
                    self.__config['players']['sprites'].append(default_sprites[i])
                    self.__config['players']['orientations'].append(default_orientations[i])
                    self.__config['players']['positions'].append(default_positions[i])
                    self.__config['players']['controls'].append(default_controls[i])
                self.map_selection()


            elif self.__buttons[3].check_hover():
                self.main()

        if self.__state == MAP_SELECTION:

            #mapa aleatorio
            if self.__buttons[1].check_hover():
                self.__config['map'] = choice(list(maps.values()))
                self.__state = QUIT
            #eights
            elif self.__buttons[2].check_hover():
                self.__config['map'] = maps['eights']
                self.__state = QUIT
            #cross and borders
            elif self.__buttons[3].check_hover():
                self.__config['map'] = maps['cross_and_borders']
                self.__state = QUIT
            #lines
            elif self.__buttons[4].check_hover():
                self.__config['map'] = maps['lines']
                self.__state = QUIT
            elif self.__buttons[5].check_hover():

                self.__config['players']['sprites'].clear()
                self.__config['players']['orientations'].clear()
                self.__config['players']['positions'].clear()
                self.__config['players']['controls'].clear()
                self.__config['player_number'] = 0
                self.multijogadores()

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
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.__state = QUIT

        self.clear_buttons()
        self.__background.destroy()
        return self.__config
