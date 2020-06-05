from game import pg, Screen, GameObject, Player, GameEngine, gspeed, gunity, imgsetb, imgsety,MainMenu

sprites_list = [imgsety,imgsetb,imgsety,imgsetb]

screen = Screen();
menu = MainMenu(screen);
config = menu.menu_loop();

game = GameEngine(screen)
# menu.wait_to_init();
## se pá é melhor dar mais informações pra config e fazer um loop mais bonitinho kk
n = len(config["players"])
if n>0:
    menu.wait_to_init(3);
    i = 0;
    while i < n :
        game.add_player(sprites_list[i], 1, -210 , -200+100*i, config["players"][i])
        i = i + 1;

    screen.remove_slave(menu);
    game.game_loop()
