from game import pg, Screen, GameObject
from game.constants import gspeed, gunity, left, right, max_health
from pygame.math import Vector2
from collections import deque
from pygame import mixer


class Player:
    def __init__(self, screen, imgset, x, y, orient):
        self.__screen = screen
        self.__imgset = imgset
        self.__id = imgset['id']
        if orient == right:
            imghead = imgset['HEAD_R']
            imgbody = imgset['BODY_R']
            imgtail = imgset['TAIL_R']
        elif orient == left:
            imghead = imgset['HEAD_L']
            imgbody = imgset['BODY_L']
            imgtail = imgset['TAIL_L']
        head = GameObject(screen, imghead, x, y, gspeed * orient, 0)
        body = GameObject(screen, imgbody, x - gunity * orient, y, gspeed * orient, 0)
        tail = GameObject(screen, imgtail, x - gunity * orient * 2, y, gspeed * orient, 0)
        self.__nodes = [head, body, tail]
        self.__grow = False
        self.__health = [1, 0]
        self.__pontos = 0
        self.__sound = mixer.Sound('assets/sounds/silence.wav')
        self.__effect = None
        self.__command_queue = deque()

    def get_id(self):
        return self.__id

    def get_nodes(self):
        return self.__nodes

    def get_head(self):
        return self.__nodes[0]

    def get_controls(self):
        return [self.up, self.left, self.down, self.right]

    def grow_size(self):
        self.__grow = True
        self.__pontos += 1

    def get_pontos(self):
        return self.__pontos

    def get_imgset(self):
        return self.__imgset

    def set_imgset(self, imgset):
        self.__imgset = imgset

    def get_health(self):
        return self.__health[0]

    def get_virtual_health(self):
        return self.__health[1]

    def set_health(self, health):
        self.__health[0] = health

    def set_virtual_health(self, health):
        self.__health[1] = health

    def inc_health(self):
        if self.__health[0] < max_health:
            self.__health[0] += 1

    def dec_health(self):
        self.__health[0] -= 1

    def inc_virtual_health(self):
        if self.__health[1] < max_health:
            self.__health[1] += 1

    def dec_virtual_health(self):
        self.__health[1] -= 1

    def update(self):
        while self.__command_queue:
            command = self.__command_queue.popleft()
            if command():
                break

        if self.__effect:
            self.__effect()

        if self.__grow:
            self.__grow = False

            old_spd = self.__nodes[1].get_spd()
            new_spd = self.__nodes[0].get_spd()

            new_pos = self.__nodes[0].get_pos()

            new_img = self.__get_img_body(old_spd, new_spd)

            new_node = GameObject(self.__screen, new_img, *new_pos, *new_spd)

            self.__nodes.insert(1, new_node)
        else:
            new_spd = self.__nodes[-2].get_spd()

            new_img = self.__get_img_tail(new_spd)

            self.__nodes[-1].set_img(new_img)
            self.__nodes[-1].update()
            self.__nodes[-1].set_spd(new_spd)

            for i in range(len(self.__nodes) - 2, 0, -1):
                new_spd = self.__nodes[i - 1].get_spd()
                old_spd = self.__nodes[i].get_spd()

                new_img = self.__get_img_body(old_spd, new_spd)

                self.__nodes[i].update()
                self.__nodes[i].set_img(new_img)
                self.__nodes[i].set_spd(new_spd)

        new_spd = self.__nodes[0].get_spd()
        new_img = self.__get_img_head(new_spd)
        self.__nodes[0].update()
        self.__nodes[0].set_img(new_img)

    def up(self):
        def command():
            if self.__nodes[0].get_spd().y == 0:
                self.__nodes[0].set_spd((0, -gspeed))
                return True
            return False

        self.__command_queue.append(command)

    def down(self):
        def command():
            if self.__nodes[0].get_spd().y == 0:
                self.__nodes[0].set_spd((0, gspeed))
                return True
            return False

        self.__command_queue.append(command)

    def left(self):
        def command():
            if self.__nodes[0].get_spd().x == 0:
                self.__nodes[0].set_spd((-gspeed, 0))
                return True
            return False

        self.__command_queue.append(command)

    def right(self):
        def command():
            if self.__nodes[0].get_spd().x == 0:
                self.__nodes[0].set_spd((gspeed, 0))
                return True
            return False

        self.__command_queue.append(command)

    def clear_command_queue(self):
        self.__command_queue.clear()

    def collision(self, obj):
        i0 = 4 if self.__nodes[0] == obj else 0
        for i in range(i0, len(self.__nodes)):
            if self.__nodes[i].collision(obj):
                return True

        return False

    def destroy(self):
        self.clear_effect()
        for i in range(len(self.__nodes)):
            self.__nodes[i].destroy()

    def add_effect(self, effect, sound=mixer.Sound('assets/sounds/silence.wav')):
        self.__effect = effect
        self.__sound = sound
        self.__sound.play()

    def clear_effect(self):
        if self.__effect:
            self.__effect(end=True)

        self.__effect = None
        self.__sound.stop()
        self.__sound = mixer.Sound('assets/sounds/silence.wav')

    # Funções auxiliares da classe
    def __get_img_body(self, old_spd, new_spd):
        if old_spd == new_spd:
            if new_spd.y < 0:
                img = self.__imgset['BODY_U']
            elif new_spd.y > 0:
                img = self.__imgset['BODY_D']
            elif new_spd.x < 0:
                img = self.__imgset['BODY_L']
            elif new_spd.x > 0:
                img = self.__imgset['BODY_R']
        else:
            if (old_spd.y > 0 and new_spd.x > 0) or (old_spd.x < 0 and new_spd.y < 0):
                img = self.__imgset['TURN_RU']
            elif (old_spd.y < 0 and new_spd.x > 0) or (old_spd.x < 0 and new_spd.y > 0):
                img = self.__imgset['TURN_RD']
            elif (old_spd.y > 0 and new_spd.x < 0) or (old_spd.x > 0 and new_spd.y < 0):
                img = self.__imgset['TURN_LU']
            elif (old_spd.y < 0 and new_spd.x < 0) or (old_spd.x > 0 and new_spd.y > 0):
                img = self.__imgset['TURN_LD']

        return img

    def __get_img_head(self, new_spd):
        if new_spd.y < 0:
            img = self.__imgset['HEAD_U']
        elif new_spd.y > 0:
            img = self.__imgset['HEAD_D']
        elif new_spd.x < 0:
            img = self.__imgset['HEAD_L']
        elif new_spd.x > 0:
            img = self.__imgset['HEAD_R']

        return img

    def __get_img_tail(self, new_spd):
        if new_spd.y < 0:
            img = self.__imgset['TAIL_U']
        elif new_spd.y > 0:
            img = self.__imgset['TAIL_D']
        elif new_spd.x < 0:
            img = self.__imgset['TAIL_L']
        elif new_spd.x > 0:
            img = self.__imgset['TAIL_R']

        return img
