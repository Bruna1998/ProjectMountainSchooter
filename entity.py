
from abc import ABC, abstractmethod
import pygame

from const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


class Entity(ABC):

    def __init__(self,name: str, position: tuple):
       
       self.name= name
       self.surf= pygame.image.load('./assets/' + name + '.png')
       self.rect =self.surf.get_rect(left=position[0], top=position[1])
       self.speed=0
       self.health=ENTITY_HEALTH[self.name]
       self.damage= ENTITY_DAMAGE[self.name]
       self.score= ENTITY_SCORE[self.name]
       self.last_dmg='None'


    @abstractmethod
    def move(self):
        pass