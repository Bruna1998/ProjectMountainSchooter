
import random
import sys
import pygame
from pygame import font,Rect,Surface
from const import C_CYAN, C_GREEN, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
from enemy import Enemy
from entity import Entity
from entityFactory import EntityFactory
from entityMediator import EntityMediator
from player import Player



class Level:
    def __init__(self,window: Surface,name: str,game_mode:str, player_score:list[int]):
        self.window= window 
        self.name= name
        self.timeout=TIMEOUT_LEVEL
        self.game_mode= game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player= EntityFactory.get_entity('Player1')
        player.score= player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            player= EntityFactory.get_entity('Player2')
            player.score= player_score[1]
            self.entity_list.append(player)

        #Defini o tempo que que cada inimigo vai aparecer na tela    
        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)

        pygame.time.set_timer(EVENT_TIMEOUT,TIMEOUT_STEP) 
        

    def run(self,player_score:list[int]): 
        pygame.mixer_music.load('./assets/'+ self.name + '.mp3')
        pygame.mixer_music.play(-1)
        clock= pygame.time.Clock()
        if self.name=='Level3':
            self.timeout=TIMEOUT_LEVEL*2
        while True:
            clock.tick(60)
            for ent in self.entity_list: 
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent,(Player, Enemy)):
                    shot= ent.shoot()
                    if shot is not None:
                        self.entity_list.append((shot))
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))
                

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==EVENT_ENEMY:
                    if self.name == 'Level1':
                        choice=random.choice(('Enemy1','Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))
                    if self.name == 'Level2':
                        choice=random.choice(('Enemy1','Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))
                    if self.name=="Level3":
                        self.entity_list.append(EntityFactory.get_entity("Enemy3"))

                if event.type==EVENT_TIMEOUT:
                    self.timeout-=TIMEOUT_STEP
                    if self.timeout==0:  
                        for ent in self.entity_list:
                            if isinstance (ent,Player) and ent.name=='Player1':
                                player_score[0]=ent.score
                            if isinstance (ent,Player) and ent.name=='Player2':
                                player_score[1]=ent.score
                        return True
                    
                found_player=False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player=True
                if not found_player:
                    return False
                    
                        
            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            #Verify Colisions e Health
            EntityMediator.verify_colision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
            