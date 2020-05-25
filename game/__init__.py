import pygame as pg

gspeed = 45

imgsety = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_cima.png'), (45, 45)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_baixo.png'), (45, 45)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_esquerda.png'), (45, 45)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/amarelo_cabeca_direita.png'), (45, 45)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_cima.png'), (45, 45)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_baixo.png'), (45, 45)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_esquerda.png'), (45, 45)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/amarelo_corpo_direita.png'), (45, 45)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_cima.png'), (45, 45)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_baixo.png'), (45, 45)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_esquerda.png'), (45, 45)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/amarelo_cauda_direita.png'), (45, 45)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_esquerda_baixo.png'), (45, 45)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_esquerda_cima.png'), (45, 45)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_direita_baixo.png'), (45, 45)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/amarelo_curva_direita_cima.png'), (45, 45))
}

imgsetb = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_cima.png'), (45, 45)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_baixo.png'), (45, 45)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_esquerda.png'), (45, 45)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/azul_cabeca_direita.png'), (45, 45)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/azul_corpo_cima.png'), (45, 45)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/azul_corpo_baixo.png'), (45, 45)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/azul_corpo_esquerda.png'), (45, 45)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/azul_corpo_direita.png'), (45, 45)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/azul_cauda_cima.png'), (45, 45)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/azul_cauda_baixo.png'), (45, 45)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/azul_cauda_esquerda.png'), (45, 45)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/azul_cauda_direita.png'), (45, 45)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/azul_curva_esquerda_baixo.png'), (45, 45)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/azul_curva_esquerda_cima.png'), (45, 45)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/azul_curva_direita_baixo.png'), (45, 45)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/azul_curva_direita_cima.png'), (45, 45))
}

imgsetp = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_cima.png'), (45, 45)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_baixo.png'), (45, 45)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_esquerda.png'), (45, 45)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/roxo_cabeca_direita.png'), (45, 45)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_cima.png'), (45, 45)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_baixo.png'), (45, 45)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_esquerda.png'), (45, 45)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/roxo_corpo_direita.png'), (45, 45)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_cima.png'), (45, 45)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_baixo.png'), (45, 45)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_esquerda.png'), (45, 45)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/roxo_cauda_direita.png'), (45, 45)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/roxo_curva_esquerda_baixo.png'), (45, 45)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/roxo_curva_esquerda_cima.png'), (45, 45)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/roxo_curva_direita_baixo.png'), (45, 45)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/roxo_curva_direita_cima.png'), (45, 45))
}

from game.screen import Screen
from game.interface_object import InterfaceObject
from game.game_object import GameObject
from game.player import Player
from game.game_engine import GameEngine
