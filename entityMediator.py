
from const import ENTITY_SCORE
from enemy import Enemy
from enemyshot import EnemyShoot
from entity import Entity
from player import Player
from playershot import PlayerShoot



class EntityMediator:

    @staticmethod
    def __verify_colision_window(ent:Entity):
        if isinstance(ent,Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

        if isinstance(ent,PlayerShoot):
            if ent.rect.right <= 0:
                ent.health = 0
        
        if isinstance(ent,EnemyShoot):
            if ent.rect.left <= 0:
                ent.health = 0

    @staticmethod
    def __verify_colision_entity(ent1,ent2):
        interaction=False
        if isinstance (ent1,PlayerShoot) and isinstance(ent2,Enemy):
            interaction=True
        elif isinstance (ent1,EnemyShoot) and isinstance(ent2,Player):
            interaction=True
        elif isinstance(ent1,Player) and isinstance(ent2,EnemyShoot):
            interaction=True
        elif isinstance(ent1,Enemy) and isinstance(ent2,PlayerShoot):
            interaction=True

        if interaction: # interaction==True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health-=ent2.damage
                ent2.health-=ent1.damage
                ent1.last_dmg=ent2.name
                ent2.last_dmg=ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score+= enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score
        

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
       for i in range(len(entity_list)):
           entity1=entity_list[i]
           EntityMediator.__verify_colision_window(entity1)
           for j in range(i+1, len(entity_list)):
                entity2= entity_list[j]
                EntityMediator.__verify_colision_entity(entity1,entity2)
    
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <=0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                    entity_list.remove(ent)