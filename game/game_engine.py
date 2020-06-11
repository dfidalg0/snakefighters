from game import InterfaceObject, PlayerUI
from game import pg, Screen, GameObject, Player, Food, powerup_list
from game.constants import fps, prob_pup, gunity, max_food, resolution
from game.assets import imgwall, img_wait_background, font_barbarian, font_snake, imgkeyboard
from pygame.math import Vector2
from pygame import mixer
from pygame.time import Clock
from random import randint, random, choice
from collections import deque

SHRINK_ARENA = pg.USEREVENT

ui_positions = [
    (-resolution[0] // 2 + 40, -335),
    (+resolution[0] // 2 - 40, -335),
    (-resolution[0] // 2 + 40, +335),
    (+resolution[0] // 2 - 40, +335),
]


class GameEngine:
    def __init__(self, screen, gamebox):
        self.__screen = screen
        self.__gamebox = gamebox
        self.__command = {}
        self.__players = []
        self.__playerkeys = {}
        self.__playeruis = []
        self.__obstacles = []
        self.__effects = []
        self.__powerups = deque()
        self.__foods = []
        self.__nfood = 0
        self.__bound = self.__gamebox.get_rect() // 2 - (gunity, gunity)

        self.__walls = [deque() for i in range(4)]

    def shrink_arena(self):
        if not (self.__bound.elementwise() > 2 * gunity):
            pg.time.set_timer(SHRINK_ARENA, 0)
            return

        gbox = self.__gamebox
        img = gbox.get_img()
        rect = img.get_rect()
        rect[0] += gunity
        rect[1] += gunity
        rect[2] -= 2 * gunity
        rect[3] -= 2 * gunity
        img = img.subsurface(rect)

        for wallset in self.__walls:
            wallset.popleft().destroy()
            wallset.pop().destroy()

        gbox.set_img(img)

        self.__bound = gbox.get_rect() // 2 - (gunity, gunity)

        incs = [Vector2(0, -1), Vector2(0, +1), Vector2(-1, 0), Vector2(+1, 0)]
        for i in range(4):
            for wall in self.__walls[i]:
                wall.set_pos(wall.get_pos() + incs[i] * gunity)

        destroy = []
        for food in self.__foods:
            abs_pos = abs(food.get_pos().elementwise())
            if abs_pos[0] > self.__bound[0] or abs_pos[1] > self.__bound[1]:
                food.destroy()
                destroy.append(food)
                self.__nfood -= 1
        for food in destroy:
            self.__foods.remove(food)

        destroy = []
        for pup in self.__powerups:
            abs_pos = abs(pup.get_pos().elementwise())
            if abs_pos[0] > self.__bound[0] or abs_pos[1] > self.__bound[1]:
                pup.destroy()
                destroy.append(pup)
        for pup in destroy:
            self.__powerups.remove(pup)

    def add_player(self, imgset, orient, x, y, keyset):
        id = imgset['id']
        pos = ui_positions[id]

        self.__playerkeys[id] = keyset

        newplayer = Player(self.__gamebox, imgset, x, y, orient)
        newui = PlayerUI(self.__screen, newplayer, *pos)

        self.__players.append(newplayer)
        self.__playeruis.append(newui)

        controls = newplayer.get_controls()

        self.__command.update(zip(keyset, controls))

    def remove_player(self, player):
        player.destroy()
        self.__players.remove(player)

    def add_obstacle(self, **kwargs):
        if 'master' not in kwargs.keys():
            kwargs['master'] = self.__gamebox

        obj = GameObject(**kwargs)
        self.__obstacles.append(obj)

        return obj

    def remove_obstacle(self, obj):
        obj.destroy()
        self.__obstacles.remove(obj)

    def clear_obstacles(self):
        for obstacle in self.__obstacles:
            obstacle.destroy()

        self.__obstacles.clear()

    def add_effect(self, effect):
        self.__effects.append(effect)

    def remove_effect(self, effect):
        effect(end=True)
        self.__effects.remove(effect)

    def load_map(self, map):
        for wall in map['walls']:
            params = {
                'img': imgwall[wall[0]],
                'x': wall[1] * gunity,
                'y': wall[2] * gunity
            }
            self.add_obstacle(**params)

        for x in range(-30 * gunity, +30 * gunity + 1, gunity):
            w1 = InterfaceObject(self.__gamebox, imgwall['H1'], x, +15 * gunity)
            w2 = InterfaceObject(self.__gamebox, imgwall['H1'], x, -15 * gunity)
            self.__walls[0].append(w1)
            self.__walls[1].append(w2)

        for y in range(-14 * gunity, +14 * gunity + 1, gunity):
            w1 = InterfaceObject(self.__gamebox, imgwall['H1'], +30 * gunity, y)
            w2 = InterfaceObject(self.__gamebox, imgwall['H1'], -30 * gunity, y)
            self.__walls[2].append(w1)
            self.__walls[3].append(w2)

    def generate_powerups(self):
        if self.__nfood < max_food:
            self.__nfood += 1
            pup = self.place_power_up(Food)
            self.__foods.append(pup)

        if random() < prob_pup:
            NewPowerUp = choice(powerup_list)
            pup = self.place_power_up(NewPowerUp)
            self.__powerups.append(pup)

    def place_power_up(self, PowerUp):
        collide = True
        while collide:
            collide = False

            x = randint(-self.__bound.x // gunity, self.__bound.x // gunity) * gunity
            y = randint(-self.__bound.y // gunity, self.__bound.y // gunity) * gunity

            pup = PowerUp(self.__gamebox, x, y)

            for obstacle in self.__obstacles:
                if obstacle.collision(pup):
                    pup.destroy()
                    collide = True
                    break

            if collide:
                continue

            for powerup in self.__powerups:
                if powerup.collision(pup):
                    pup.destroy()
                    collide = True
                    break

            if collide:
                continue

            for food in self.__foods:
                if food.collision(pup):
                    pup.destroy()
                    collide = True
                    break

            if collide:
                continue

            for player in self.__players:
                if player.collision(pup):
                    pup.destroy()
                    collide = True
                    break

        return pup

    def exibit_time(self):
        font = font_snake
        message = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        timer = 0

        time = font.render(message[0], True, (0, 177, 11))
        timeup = InterfaceObject(self.__screen, time, 0, -330)
        timedw = InterfaceObject(self.__screen, time, 0, 330)

        def print_message(end=False):
            nonlocal timer
            if end:
                timeup.destroy()
                timedw.destroy()

            elif timer >= 10 * fps:
                self.remove_effect(print_message)

            else:
                newtime = font.render(message[timer // fps], True, (0, 177, 11))
                timeup.set_img(newtime)
                timedw.set_img(newtime)
                timer += 1

        self.add_effect(print_message)

    def game_loop(self):
        pg.init()
        pg.mouse.set_visible(False)

        background = img_wait_background.convert()
        background.set_alpha(180)
        background = InterfaceObject(self.__screen, background, 0, 0)

        inc = 2 * gunity
        incs = [(0, 0), (-inc, +inc), (0, +inc), (+inc, +inc)]

        pos0 = -self.__bound / 2 - (0, inc)
        order = [0, 1, 3, 2]
        for i in range(4):
            if order[i] in self.__playerkeys.keys():
                for j in range(4):
                    InterfaceObject(background, imgkeyboard[self.__playerkeys[order[i]][j]], *(pos0 + incs[j]))

            pos0[i % 2] *= -1

        mixer.music.load('assets/music.wav')
        mixer.music.play(-1)

        font = font_barbarian

        messages = ['Ready>', 'Set..>', 'Fight>']

        for i in range(3):
            segundosIMG = font.render(messages[i], True, (134, 177, 11))
            segundosIMG = InterfaceObject(self.__screen, segundosIMG, 0, 0)
            self.__screen.update()
            pg.time.wait(1000)
            segundosIMG.destroy()

        background.destroy()

        del background, pos0, inc, incs, font, messages, i, segundosIMG

        pg.time.set_timer(SHRINK_ARENA, 90000)

        pg.key.get_pressed()
        for player in self.__players:
            player.clear_command_queue()

        running = True
        clock = Clock()
        while running:

            self.__screen.update()
            clock.tick(fps)
            self.generate_powerups()

            # Resolução da fila de eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    try:
                        self.__command[event.key]()
                    except KeyError:
                        pass  # Chave não associada a nenhum comando
                if event.type == SHRINK_ARENA:
                    self.exibit_time()
                    pg.time.set_timer(SHRINK_ARENA, 10000)
                    self.shrink_arena()
            # Fila de eventos

            # Efeitos na tela
            for effect in self.__effects:
                effect()

            # Checagem de colisões fatais
            dead_players = []
            for player in self.__players:
                head = player.get_head()
                for other in self.__players:
                    if other.collision(head):
                        player.dec_health()

                for obstacle in self.__obstacles:
                    if obstacle.collision(head):
                        player.dec_health()

                pos = head.get_pos()
                abs_pos = abs(pos.elementwise())
                if abs_pos.x > self.__bound.x + gunity or abs_pos.y > self.__bound.y + gunity:
                    player.set_health(0)
                elif abs_pos.x > self.__bound.x or abs_pos.y > self.__bound.y:
                    player.dec_health()
                    player.clear_command_queue()

                    spd = head.get_spd()
                    angle = choice([90, -90])
                    pos = pos + spd.rotate(angle)
                    abs_pos = abs(pos.elementwise())

                    if (
                            abs_pos.elementwise() > self.__bound or
                            abs_pos.x > self.__bound.x + gunity or
                            abs_pos.y > self.__bound.y + gunity
                    ):
                        head.set_spd(spd.rotate(-angle))
                    else:
                        head.set_spd(spd.rotate(angle))

                if player.get_health() <= 0:
                    dead_players.append(player)

            for player in dead_players:
                self.remove_player(player)

                if len(self.__players) <2:
                    if len(self.__players) == 1:
                        winner = self.__players[0].get_id()
                    else:
                        maior = 0
                        for player in dead_players:
                            if player.get_pontos() > maior:
                                maior = player.get_pontos()
                        for player in dead_players:
                            if player.get_pontos() == maior:
                                winner = player.get_id()
                    running = False

            # Colisões fatais

            # Atualização das posições dos jogadores remanescentes
            for player in self.__players:
                player.update()

            # Atualização das interfaces dos jogadores
            for UI in self.__playeruis:
                UI.update()

            # Checagem de coleta de power-ups
            catched_pups = []
            catched_foods = []
            for player in self.__players:
                head = player.get_head()
                for pup in self.__powerups:
                    if pup.collision(head):
                        pup.catch(player, self)
                        catched_pups.append(pup)
                for food in self.__foods:
                    if food.collision(head):
                        food.catch(player, self)
                        catched_foods.append(food)

            for pup in catched_pups:
                pup.destroy()
                self.__powerups.remove(pup)

            for food in catched_foods:
                food.destroy()
                self.__foods.remove(food)
                self.__nfood -= 1
            # Coleta de power-ups

            # Checagem de timer de power-ups
            for pup in self.__powerups:
                pup.inc_timer()

            if self.__powerups and self.__powerups[0].get_timer() == 10 * fps:
                self.__powerups.popleft().destroy()
            # Timer de power-ups
