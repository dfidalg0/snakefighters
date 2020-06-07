from game import pg
from game.constants import gunity
import json


def load_map(path):
    with open(path) as file:
        return json.load(file)


maps = {
    'cross_and_borders': load_map('assets/maps/cross_and_borders.json'),
    'lines': load_map('assets/maps/lines.json'),
    'eights': load_map('assets/maps/eights.json')
}

del load_map, json

imgpowerup = {
    'FOOD': pg.transform.scale(pg.image.load('assets/img/ponto.png'), (gunity, gunity)),
    'LIFE': pg.transform.scale(pg.image.load('assets/img/vida.png'), (gunity, gunity)),
    'INVI': pg.transform.scale(pg.image.load('assets/img/invencibilidade.png'), (gunity, gunity)),
    'WEAP': pg.transform.scale(pg.image.load('assets/img/pup_generico.png'), (gunity, gunity))
}

imgwall = {
    'H9': pg.transform.scale((pg.image.load('assets/img/parede_9.png')), (9 * gunity, gunity)),
    'H11': pg.transform.scale((pg.image.load('assets/img/parede_11.png')), (11 * gunity, gunity)),
    'H15': pg.transform.scale((pg.image.load('assets/img/parede_15.png')), (15 * gunity, gunity)),
    'V7': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_7.png'), (7 * gunity, gunity)), 90),
    'V5': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_5.png'), (5 * gunity, gunity)), 90),
    'V9': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_9.png'), (9 * gunity, gunity)), 90)
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

imgsetw = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/branco_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/branco_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/branco_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/branco_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/branco_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/branco_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/branco_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/branco_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/branco_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/branco_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/branco_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/branco_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/branco_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/branco_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/branco_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/branco_curva_direita_cima.png'), (gunity, gunity))
}
