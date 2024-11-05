
import random
from backgroung import Background
from const import WIN_HEIGHT, WIN_WIDHT
from player import Player
from enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}',(WIN_WIDHT,0)))
                return list_bg
            
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level2Bg{i}',(WIN_WIDHT,0)))
                return list_bg
            
            case 'Level3Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level3Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level3Bg{i}',(WIN_WIDHT,0)))
                return list_bg
            
            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT/2 -30))
            case 'Player2':
                return Player(name='Player2', position=(10, WIN_HEIGHT/2 + 30))
            case 'Enemy1':
                return Enemy(name='Enemy1',position=(WIN_WIDHT + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy(name='Enemy2',position=(WIN_WIDHT + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Enemy3':
                return Enemy(name='Enemy3',position=(WIN_WIDHT + 10, random.randint(40, WIN_HEIGHT - 40)))
            


