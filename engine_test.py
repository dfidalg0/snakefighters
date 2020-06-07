from game import pg, Screen, GameObject, InterfaceObject, Player, GameEngine, gspeed, gunity, imgsetb, imgsety, wall

screen = Screen()
background = pg.transform.scale(pg.image.load('assets/img/background.jpg'), (60 * gunity, 30 * gunity))
arena = InterfaceObject(screen, background)
game = GameEngine(screen, arena)

game.add_obstacle(img=wall['V5'], x=0, y=3*gunity)
game.add_obstacle(img=wall['V5'], x=0, y=-3*gunity)
game.add_obstacle(img=wall['H11'], x=0, y=0)
game.add_obstacle(img=wall['H9'], x=20*gunity, y=10*gunity)
game.add_obstacle(img=wall['H9'], x=-20*gunity, y=-10*gunity)
game.add_obstacle(img=wall['H9'], x=20*gunity, y=-10*gunity)
game.add_obstacle(img=wall['H9'], x=-20*gunity, y=10*gunity)
game.add_obstacle(img=wall['V7'], x=(20+4)*gunity, y=(10-4)*gunity)
game.add_obstacle(img=wall['V7'], x=-(20+4)*gunity, y=(10-4)*gunity)
game.add_obstacle(img=wall['V7'], x=-(20+4)*gunity, y=-(10-4)*gunity)
game.add_obstacle(img=wall['V7'], x=(20+4)*gunity, y=-(10-4)*gunity)
WALL = pg.transform.scale(pg.image.load('assets/img/parede.png'), (gunity, gunity))


for x in range(-30 * gunity, +30 * gunity+1, gunity):
    InterfaceObject(arena, WALL,x,+15*gunity)
    InterfaceObject(arena, WALL,x,-15*gunity)

for y in range(-14 * gunity, +14 * gunity+1, gunity):
    InterfaceObject(arena, WALL,+30*gunity,y)
    InterfaceObject(arena, WALL,-30*gunity,y)

game.add_player(imgsety, 1, -10*gunity, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
game.add_player(imgsetb, -1, 10*gunity, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])
game.game_loop()
