import pygame as pg

pg.init()

import game.constants as constants
import game.assets as assets


from game.screen import Screen
from game.interface_object import InterfaceObject
from game.game_object import GameObject
from game.button import Button
from game.player import Player
from game.menu import MainMenu
from game.player_ui import PlayerUI


from game.powerup.powerup_meta import PowerUpMeta
from game.powerup.food import Food

from os import listdir as ls

modules = [file[:-3] for file in ls('game/powerup') if file[-3:] == '.py']

for module in modules:
    exec('import game.powerup.' + module)
    exec('del game.powerup.' + module)

powerup_list = PowerUpMeta.__subclasses__()
powerup_list.remove(Food)

del PowerUpMeta, ls, module, modules


from game.game_engine import GameEngine
