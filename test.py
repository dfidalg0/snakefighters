from game import pg, Screen, GameObject
from time import sleep


def get_close():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return True
    else:
        return False


screen = Screen()

SNAKE = pg.image.load('assets/img/snake_test.png')
SNAKE = pg.transform.scale(SNAKE,(90,90))

KUNAI = pg.image.load('assets/img/weapon.png')
KUNAI = pg.transform.scale(KUNAI,(90,90))

master = GameObject(screen, SNAKE, y=180, vy=-5)
slv1 = GameObject(master, SNAKE, -200,100)
slv2 = GameObject(slv1, SNAKE, -200,100)

sword = GameObject(slv1, KUNAI, y=-SNAKE.get_rect().size[1])

w = 2.5
angle = w

for i in range(100):
    if get_close():
        exit()
    screen.update()
    sleep(0.001)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_position().rotate(-w))
    angle += w
    angle %= 360

master.set_spd((2,0))
slv1.set_spd((-2,0))
slv2.set_spd((2,2))

for i in range(200):
    if get_close():
        exit()
    screen.update()
    sleep(0.001)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_position().rotate(-w))
    angle += w
    angle %= 360

master.set_spd((0,0))
slv1.set_spd((0,0))
slv2.set_spd((0,0))

while True:
    if get_close():
        exit()
    screen.update()
    sleep(0.001)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_position().rotate(-w))
    angle += w
    angle %= 360
