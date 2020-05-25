from game import pg, Screen, GameObject, Player, GameEngine, gspeed, imgsety, imgsetb


screen = Screen()
game = GameEngine(screen)

game.add_player(imgsety, 1, -200, 0, [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT])
game.add_player(imgsetb, -1, 200, 0, [pg.K_w, pg.K_a, pg.K_s, pg.K_d])

game.game_loop()
