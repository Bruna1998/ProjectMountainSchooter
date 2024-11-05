import pygame
from pygame import font,Rect,Surface
from const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, WIN_HEIGHT, WIN_WIDHT


class Menu:
    def __init__(self,window):
        self.window=window    
        self.surf=pygame.image.load('./assets/MenuBg.png')
        self.rect=self.surf.get_rect(left=0,top=0)
    
    def run(self):
        menu_option=0
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            #Draw the Surface and the text
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50,text='Mountain',text_color=COLOR_ORANGE,text_center_pos=((WIN_WIDHT/2),70))
            self.menu_text(text_size=50,text='Schooter',text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDHT/2),120))
            self.menu_text(text_size=20, text='Bruna Sampaio May - RU:3620214', text_color=COLOR_WHITE,text_center_pos=(120,10))

            for i in range(len(MENU_OPTION)):
                if i==menu_option:
                    self.menu_text(text_size=20,text=MENU_OPTION[i],text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDHT/2),200 + 25*i))
                else:
                    self.menu_text(text_size=20,text=MENU_OPTION[i],text_color= COLOR_WHITE, text_center_pos=((WIN_WIDHT/2),200 + 25*i))
        
            pygame.display.flip()

            #Checa todos os eventos
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN: #DOWN KEY
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option+=1
                        else:
                            menu_option=0  
                
                    if event.key==pygame.K_UP: #UP KEY
                        if menu_option > 0:
                            menu_option-= 1
                        else:
                            menu_option=len(MENU_OPTION)-1
                    if event.key==pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]        
                     

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font:font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf:Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect:Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        