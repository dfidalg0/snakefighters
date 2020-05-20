from game import pg, Screen, GameObject
from time import sleep

def get_close():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return True
    else:
        return False


screen = Screen()

SNAKE_FIG = pg.image.load('assets/img/snake_test.png')
SWORD = pg.image.load('assets/img/weapon.png')

master = GameObject(screen, SNAKE_FIG, y=180, vy=-5)
slv1 = GameObject(master, SNAKE_FIG, -200,100)
slv2 = GameObject(slv1, SNAKE_FIG, -200,100)

sword = GameObject(slv2, SWORD, y=-128)

for i in range(100):
    if get_close():
        exit()
    screen.update()
    sleep(0.001)
    master.update()
    slv1.update()
    slv2.update()
    sword.update()

master.set_spd((4,0))
slv1.set_spd((-4,0))
slv2.set_spd((5,5))

for i in range(100):
    if get_close():
        break
    screen.update()
    sleep(0.001)
    master.update()
    slv1.update()
    slv2.update()
    sword.update()

while True:
    if get_close():
        break
