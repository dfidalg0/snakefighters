from game import pg
from game.constants import gunity, resolution


dummy_surface = pg.Surface((2, 2))
dummy_surface.set_colorkey((0, 0, 0))

from json import load
from os import listdir

maps = {}
for filename in listdir('assets/maps'):
    if filename[-5:] == '.json':
        path = 'assets/maps/' + filename
        with open(path) as file:
            maps[filename[:-5]] = load(file)

for i in maps.keys():
    maps[i]['positions'] = [(pos[0]*gunity, pos[1]*gunity) for pos in maps[i]['positions']]
    maps[i]['walls'] = [(wall[0],wall[1]*gunity,wall[2]*gunity) for wall in maps[i]['walls']]

del load, listdir, filename

pg.font.init()
font_barbarian = pg.font.Font('assets/fonts/barbarian.ttf', 90)
font_snake = pg.font.Font('assets/fonts/Snake Chan.ttf', 50)

img_icon = pg.image.load('assets/img/icon.png')

img_wait_background = pg.Surface(resolution)
img_wait_background.fill((0, 0, 0))

img_menu_background = pg.transform.scale(pg.image.load('assets/img/menu_background.png'), resolution)
img_ending_screen = pg.transform.scale(pg.image.load('assets/img/ending_screen.png'),resolution)

# Screen Background
half_res = (resolution[0] / 2, resolution[1] / 2)
aux = pg.Surface(half_res)
img_scr_background = pg.Surface(resolution)

colors = [(136, 131, 8), (12, 24, 106), (113, 60, 11), (81, 14, 87)]
coords = [(0, 0), (half_res[0], 0), (0, half_res[1]), half_res]

for i in range(4):
    aux.fill(colors[i])
    img_scr_background.blit(aux, coords[i])

background2 = pg.transform.scale(pg.image.load('assets/img/background2.png'), (60 * gunity, 30 * gunity))

img_scr_background.blit(background2, (40, 60))

del aux, colors, coords, half_res, i
# Screen Background

imgkeyboard = {}
keys = 'abcdefghijklmnopqrstuvwxyz0123456789'

for key in keys:
    imgkeyboard[ord(key)] = pg.transform.scale(pg.image.load('assets/img/keyboard_keys/keyboard_key_' + key + '.png'),
                                               (2 * gunity, 2 * gunity))

for i in range(10):
    imgkeyboard[pg.K_KP0 + i] = imgkeyboard[pg.K_0 + i]

for (i, key) in enumerate(['up', 'down', 'right', 'left']):
    imgkeyboard[pg.K_UP + i] = pg.transform.scale(
        pg.image.load('assets/img/keyboard_keys/keyboard_key_' + key + '.png'), (2 * gunity, 2 * gunity))

del key, keys, i

imgpowerup = {
    'FOOD': pg.transform.scale(pg.image.load('assets/img/powerups/ponto.png'), (gunity, gunity)),
    'LIFE': pg.transform.scale(pg.image.load('assets/img/powerups/vida.png'), (gunity, gunity)),
    'INVI': pg.transform.scale(pg.image.load('assets/img/powerups/invencibilidade.png'), (gunity, gunity)),
    'WEAP': pg.transform.scale(pg.image.load('assets/img/powerups/dagger.png'), (gunity, gunity)),
    'BOMB': pg.transform.scale(pg.image.load('assets/img/powerups/bomb.png'), (gunity, gunity)),
    'FIRE': pg.transform.scale(pg.image.load('assets/img/powerups/fire.png'), (gunity, gunity))
}

imgwall = {}

imgwall = {
    'H1': pg.transform.scale((pg.image.load('assets/img/parede.png')), (gunity, gunity)),
    'H9': pg.transform.scale((pg.image.load('assets/img/parede_9.png')), (9 * gunity, gunity)),
    'H11': pg.transform.scale((pg.image.load('assets/img/parede_11.png')), (11 * gunity, gunity)),
    'H15': pg.transform.scale((pg.image.load('assets/img/parede_15.png')), (15 * gunity, gunity)),
    'V7': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_7.png'), (7 * gunity, gunity)), 90),
    'V5': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_5.png'), (5 * gunity, gunity)), 90),
    'V9': pg.transform.rotate(pg.transform.scale(pg.image.load('assets/img/parede_9.png'), (9 * gunity, gunity)), 90)
}

imgsety = {
    'id': 0,
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_curva_esquerda_baixo.png'),
                                  (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/snakes/amarelo_curva_direita_cima.png'), (gunity, gunity))
}

imgsetb = {
    'id': 1,
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/snakes/azul_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/snakes/azul_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/snakes/azul_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/snakes/azul_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/snakes/azul_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/snakes/azul_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/snakes/azul_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/snakes/azul_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/snakes/azul_curva_direita_cima.png'), (gunity, gunity))
}

imgseto = {
    'id': 2,
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_curva_esquerda_baixo.png'),
                                  (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/snakes/laranja_curva_direita_cima.png'), (gunity, gunity))
}

imgsetp = {
    'id': 3,
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/snakes/roxo_curva_direita_cima.png'), (gunity, gunity))
}

# Game effects
imgsetw = {
    'HEAD_U': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cabeca_cima.png'), (gunity, gunity)),
    'HEAD_D': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cabeca_baixo.png'), (gunity, gunity)),
    'HEAD_L': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cabeca_esquerda.png'), (gunity, gunity)),
    'HEAD_R': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cabeca_direita.png'), (gunity, gunity)),
    'BODY_U': pg.transform.scale(pg.image.load('assets/img/snakes/branco_corpo_cima.png'), (gunity, gunity)),
    'BODY_D': pg.transform.scale(pg.image.load('assets/img/snakes/branco_corpo_baixo.png'), (gunity, gunity)),
    'BODY_L': pg.transform.scale(pg.image.load('assets/img/snakes/branco_corpo_esquerda.png'), (gunity, gunity)),
    'BODY_R': pg.transform.scale(pg.image.load('assets/img/snakes/branco_corpo_direita.png'), (gunity, gunity)),
    'TAIL_U': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cauda_cima.png'), (gunity, gunity)),
    'TAIL_D': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cauda_baixo.png'), (gunity, gunity)),
    'TAIL_L': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cauda_esquerda.png'), (gunity, gunity)),
    'TAIL_R': pg.transform.scale(pg.image.load('assets/img/snakes/branco_cauda_direita.png'), (gunity, gunity)),
    'TURN_LD': pg.transform.scale(pg.image.load('assets/img/snakes/branco_curva_esquerda_baixo.png'), (gunity, gunity)),
    'TURN_LU': pg.transform.scale(pg.image.load('assets/img/snakes/branco_curva_esquerda_cima.png'), (gunity, gunity)),
    'TURN_RD': pg.transform.scale(pg.image.load('assets/img/snakes/branco_curva_direita_baixo.png'), (gunity, gunity)),
    'TURN_RU': pg.transform.scale(pg.image.load('assets/img/snakes/branco_curva_direita_cima.png'), (gunity, gunity))
}

imgbutton = {
    'jogar': [
        pg.image.load('assets/img/buttons/jogar.png'),
        pg.image.load('assets/img/buttons/jogar2.png'),
        pg.image.load('assets/img/buttons/jogar3.png')
    ],
    'modo_pratica': [
        pg.image.load('assets/img/buttons/modo_pratica.png'),
        pg.image.load('assets/img/buttons/modo_pratica2.png'),
        pg.image.load('assets/img/buttons/modo_pratica3.png')
    ],
    'opcoes': [
        pg.image.load('assets/img/buttons/opcoes.png'),
        pg.image.load('assets/img/buttons/opcoes2.png'),
        pg.image.load('assets/img/buttons/opcoes3.png')
    ],
    'extra': [
        pg.image.load('assets/img/buttons/extra.png'),
        pg.image.load('assets/img/buttons/extra2.png'),
        pg.image.load('assets/img/buttons/extra3.png')
    ],
    'encerrar': [
        pg.image.load('assets/img/buttons/encerrar.png'),
        pg.image.load('assets/img/buttons/encerrar2.png'),
        pg.image.load('assets/img/buttons/encerrar3.png')
    ],
    'dois_jogadores': [
        pg.image.load('assets/img/buttons/dois_jogadores.png'),
        pg.image.load('assets/img/buttons/dois_jogadores2.png'),
        pg.image.load('assets/img/buttons/dois_jogadores3.png')
    ],
    'tres_jogadores': [
        pg.image.load('assets/img/buttons/tres_jogadores.png'),
        pg.image.load('assets/img/buttons/tres_jogadores2.png'),
        pg.image.load('assets/img/buttons/tres_jogadores3.png')
    ],
    'quatro_jogadores': [
        pg.image.load('assets/img/buttons/quatro_jogadores.png'),
        pg.image.load('assets/img/buttons/quatro_jogadores2.png'),
        pg.image.load('assets/img/buttons/quatro_jogadores3.png')
    ],
    'voltar': [
        pg.image.load('assets/img/buttons/voltar.png'),
        pg.image.load('assets/img/buttons/voltar2.png'),
        pg.image.load('assets/img/buttons/voltar3.png')
    ],
    'eights':           [
        pg.image.load('assets/img/buttons/eights.png'),
        pg.image.load('assets/img/buttons/eights2.png'),
        pg.image.load('assets/img/buttons/eights3.png')
    ],
    'mapa_aleatorio':           [
        pg.image.load('assets/img/buttons/mapa_aleatorio.png'),
        pg.image.load('assets/img/buttons/mapa_aleatorio2.png'),
        pg.image.load('assets/img/buttons/mapa_aleatorio3.png')
    ],
    'cross_and_borders':           [
        pg.image.load('assets/img/buttons/cross_and_borders.png'),
        pg.image.load('assets/img/buttons/cross_and_borders2.png'),
        pg.image.load('assets/img/buttons/cross_and_borders3.png')
    ],
    'lines':           [
        pg.image.load('assets/img/buttons/lines.png'),
        pg.image.load('assets/img/buttons/lines2.png'),
        pg.image.load('assets/img/buttons/lines3.png')
    ],
    'menu_principal':           [
        pg.image.load('assets/img/buttons/menu_principal.png'),
        pg.image.load('assets/img/buttons/menu_principal2.png'),
        pg.image.load('assets/img/buttons/menu_principal3.png')
    ],
    'encerrar_w':           [
        pg.image.load('assets/img/buttons/encerrar_w.png'),
        pg.image.load('assets/img/buttons/encerrar_w2.png'),
        pg.image.load('assets/img/buttons/encerrar_w3.png')
    ],
    'menu_sec':           [
        pg.image.load('assets/img/buttons/menu_sec.png'),
        pg.image.load('assets/img/buttons/menu_sec.png'),
        pg.image.load('assets/img/buttons/menu_sec.png')
    ]
}

imgsnake = [ pg.image.load('assets/img/cobra_amarela.png'),
             pg.image.load('assets/img/cobra_azul.png'),
             pg.image.load('assets/img/cobra_roxa.png'),
             pg.image.load('assets/img/cobra_laranja.png')
]

imgexplosion = pg.transform.scale(pg.image.load('assets/img/explosion.png'), (5 * gunity, 5 * gunity))
imgkunai = pg.transform.scale(pg.image.load('assets/img/kunai.png'), (24, 64))

skull = pg.image.load('assets/img/skull.png')
heart = pg.image.load('assets/img/coracao_interface.png')
crown = pg.image.load('assets/img/coroa.png')