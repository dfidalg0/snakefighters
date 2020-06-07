from game import pg, Screen, GameObject, Player, GameEngine, gspeed, gunity, imgsetb, imgsety

screen = Screen()
game = GameEngine(screen)

WALL = pg.transform.scale(pg.image.load('assets/img/parede.png'),(90,90))

for x in range(-270,270+1,90):
    game.add_obstacle(img=WALL,x=x,y=-180)
    game.add_obstacle(img=WALL,x=x,y=+180)

game.add_player(imgsety, 1, -210, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
game.add_player(imgsetb, -1, 210, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])

game.game_loop()
