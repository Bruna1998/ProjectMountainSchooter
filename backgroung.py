
from const import ENTITY_SPEED, WIN_WIDHT
from entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    #Movimento Parallax
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = WIN_WIDHT

