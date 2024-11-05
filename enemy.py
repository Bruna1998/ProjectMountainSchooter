from const import ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_SHOOT, WIN_HEIGHT, WIN_WIDHT
from enemyshot import EnemyShoot
from entity import Entity
import level



class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = 1  # 1 para baixo, -1 para cima
    
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
    
        if self.name == 'Enemy3':
            # Verifica as bordas da tela
            if self.rect.top <= 0:  # Borda superior
                    self.direction = 1  # Começa a descer
            elif self.rect.bottom >= WIN_HEIGHT:  # Borda inferior
                self.direction = -1  # Começa a subir
            
            # Move o inimigo para cima ou para baixo
            self.rect.centery += self.direction * ENTITY_SPEED[self.name] * (2 if self.direction == 1 else 1)

        
    
    def shoot(self):
        self.shot_delay-=1
        if self.shot_delay<=0:
            self.shot_delay=ENTITY_SHOT_DELAY[self.name]
            return EnemyShoot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        