from game import pg, Screen, GameObject, Player, Food, powerup_list
from game.constants import fps, prob_pup, gunity
from game.assets import imgwall
from pygame.math import Vector2
from pygame.time import Clock
from random import randint, random, choice


class GameEngine:
    def __init__(self, screen, gamebox):
        self.__screen = screen
        self.__gamebox = gamebox
        self.__command = {}
        self.__players = []
        self.__obstacles = []
        self.__powerups = []
        self.__nfood = 0
        self.__bound = self.__gamebox.get_rect()//2 - (gunity,gunity)

    def add_player(self, imgset, orient, x, y, keyset):
        newplayer = Player(self.__gamebox, imgset, x, y, orient)
        self.__players.append(newplayer)

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

    def remove_obstacle(self,obj):
        obj.destroy()
        self.__obstacles.remove(obj)

    def clear_obstacles(self):
        for obstacle in self.__obstacles:
            obstacle.destroy()

        self.__obstacles.clear()

    def load_map(self,map):
        for wall in map:
            params = {
                'img' : imgwall[wall[0]],
                'x' : wall[1]*gunity,
                'y' : wall[2]*gunity
            }
            self.add_obstacle(**params)

    def generate_powerups(self):
        if self.__nfood <= 3:
            self.place_power_up(Food)
            self.__nfood += 1

        if random() < prob_pup:
            NewPowerUp = choice(powerup_list)
            self.place_power_up(NewPowerUp)

    def remove_food(self):
        self.__nfood -= 1

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

            for player in self.__players:
                if player.collision(pup):
                    pup.destroy()
                    collide = True
                    break

        self.__powerups.append(pup)

    def game_loop(self):
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
            # Fila de eventos

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
                if abs_pos.x > self.__bound.x or abs_pos.y > self.__bound.y:
                    player.dec_health()
                    player.clear_command_queue()

                    spd = head.get_spd()
                    angle = choice([90,-90])
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
            # Colisões fatais

            # Atualização das posições dos jogadores remanescentes
            for player in self.__players:
                player.update()

            # Checagem de coleta de power-ups
            catched_pups = []
            for player in self.__players:
                head = player.get_head()
                for pup in self.__powerups:
                    if pup.collision(head):
                        pup.catch(player, self)
                        catched_pups.append(pup)

            for pup in catched_pups:
                pup.destroy()
                self.__powerups.remove(pup)
            # Coleta de power-ups
