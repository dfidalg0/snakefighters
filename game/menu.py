from game import pg,Screen,InterfaceObject,Button
from game.assets import imgsety, imgsetb, imgseto, imgsetp
from game.assets import imgbutton, img_menu_background
from game.constants import left, right, gunity
from pygame.math import Vector2
from pygame.time import Clock


QUIT = 0
MAIN = 1
MULTIPLAYER = 2

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
    [pg.K_y, pg.K_g, pg.K_h, pg.K_j],
    [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT],
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

        labels = ['jogador_unico','multijogadores','opcoes','extra','encerrar']

        x = -self.__bound[0] * 0.65
        y = -self.__bound[1] * 0.70

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.3

    def multijogadores(self):
        self.__state = MULTIPLAYER

        self.clear_buttons()

        labels = ['dois_jogadores','tres_jogadores','quatro_jogadores','voltar']

        x = -self.__bound[0] * 0.65
        y = -self.__bound[1] * 0.70

        for label in labels:
            Button(self, imgbutton[label], x,y)
            y += self.__bound[1] * 0.3

    def update(self):
        if self.__state == MAIN:
            # single player
            if self.__buttons[0].check_hover():
                self.__config['player_number'] = 1
                self.__config['players']['sprites'].append(default_sprites[0])
                self.__config['players']['orientations'].append(default_orientations[0])
                self.__config['players']['positions'].append(default_positions[0])
                self.__config['players']['controls'].append(default_controls[0])
                self.__state = QUIT

            # multiplayer
            elif self.__buttons[1].check_hover():
                self.multijogadores()
            # opcoes
            elif self.__buttons[2].check_hover():
                print('menu opcoes')
            # extras ?
            elif self.__buttons[3].check_hover():
                print('pq coloquei extras')
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
                self.__state = QUIT

            elif self.__buttons[1].check_hover():
                self.__config['player_number'] = 3
                for i in range(3):
                    self.__config['players']['sprites'].append(default_sprites[i])
                    self.__config['players']['orientations'].append(default_orientations[i])
                    self.__config['players']['positions'].append(default_positions[i])
                    self.__config['players']['controls'].append(default_controls[i])
                self.__state = QUIT

            elif self.__buttons[2].check_hover():
                self.__config['player_number'] = 4
                for i in range(4):
                    self.__config['players']['sprites'].append(default_sprites[i])
                    self.__config['players']['orientations'].append(default_orientations[i])
                    self.__config['players']['positions'].append(default_positions[i])
                    self.__config['players']['controls'].append(default_controls[i])
                self.__state = QUIT

            elif self.__buttons[3].check_hover():
                self.main()

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
                    self.__state = QUIT
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.__state = QUIT

        self.clear_buttons()
        self.__background.destroy()
        return self.__config
