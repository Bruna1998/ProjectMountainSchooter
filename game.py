import pygame
from level import Level
from menu import Menu
from const import MENU_OPTION, WIN_WIDHT,WIN_HEIGHT
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(size=(WIN_WIDHT,WIN_HEIGHT))

    def run(self):
        while True:
            score=Score(self.window)
            menu=Menu(self.window)
            menu_return=menu.run()
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1], MENU_OPTION[2]]:
                player_score=[0,0] # Score Player 1 e Player 2
                level=Level(self.window,'Level1',menu_return, player_score)
                level_return=level.run(player_score)
                if level_return:
                    level=Level(self.window,'Level2',menu_return,player_score)
                    level_return=level.run(player_score)
                    if level_return:
                        level=Level(self.window,'Level3',menu_return,player_score)
                        level_return=level.run(player_score)
                        if level_return:
                         score.save(menu_return,player_score)

            elif menu_return==MENU_OPTION[3]:
                 score.show()
                 
            elif menu_return==MENU_OPTION[4]:
                    pygame.quit()
                    quit()
            else:
                 pass        