from game import pg, Screen, GameObject
from pygame.time import Clock


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
KUNAI = KUNAI.subsurface((5*90//16,0,90-5*90//16,90))

master = GameObject(screen, SNAKE, y=180, vy=-15)
slv1 = GameObject(master, SNAKE, -200,100)
slv2 = GameObject(slv1, SNAKE, -200,100)

sword = GameObject(slv1, KUNAI, y=-SNAKE.get_rect().size[1])

w = 25
angle = w

clock = Clock()
clock_tick = 30
for i in range(33):
    if get_close():
        exit()
    screen.update()
    clock.tick(clock_tick)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_pos().rotate(-w))
    angle += w
    angle %= 360

master.set_spd((10,0))
slv1.set_spd((-10,0))
slv2.set_spd((10,10))

for i in range(40):
    if get_close():
        exit()
    screen.update()
    clock.tick(clock_tick)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_pos().rotate(-w))
    angle += w
    angle %= 360

master.set_spd((0,0))
slv1.set_spd((0,0))
slv2.set_spd((0,0))

while True:
    if get_close():
        exit()
    screen.update()
    clock.tick(clock_tick)
    master.update()
    slv1.update()
    slv2.update()
    sword.set_img(pg.transform.rotate(KUNAI,angle))
    sword.set_pos(sword.get_pos().rotate(-w))
    angle += w
    angle %= 360
