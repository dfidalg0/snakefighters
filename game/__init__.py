import pygame as pg

gspeed = 30
gunity = 30

imgpowerup = {
    'FOOD': pg.transform.scale(pg.image.load('assets/img/ponto.png'), (gunity, gunity)),
    'LIFE': pg.transform.scale(pg.image.load('assets/img/vida.png'), (gunity, gunity)),
    'INVI': pg.transform.scale(pg.image.load('assets/img/invencibilidade.png'), (gunity, gunity))
}

imgsety = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_direita_cima.png'), (gunity, gunity))
}

imgsetb = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/azul_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/azul_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/azul_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/azul_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/azul_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/azul_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/azul_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/azul_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/azul_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/azul_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/azul_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/azul_curva_direita_cima.png'), (gunity, gunity))
}

imgsetp = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/roxo_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/roxo_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/roxo_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/roxo_curva_direita_cima.png'), (gunity, gunity))
}

from game.screen import Screen
from game.interface_object import InterfaceObject
from game.game_object import GameObject
from game.player import Player
from game.powerup import PowerUp
from game.food import Food
from game.secondchance import SecondChance
from game.invencibility import Invencibility
from game.game_engine import GameEngine
