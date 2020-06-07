import pygame as pg

import game.constants as constants
import game.assets as assets

from game.screen import Screen
from game.interface_object import InterfaceObject
from game.game_object import GameObject
from game.player import Player

from game.powerup.secondchance import SecondChance
from game.powerup.invencibility import Invencibility
from game.powerup.food import Food

powerup_list = [SecondChance,Invencibility]

from game.game_engine import GameEngine
