import pygame
from pygame.locals import *
from config import *
from import_images import *

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, item_type, player) -> None:
        super().__init__(groups)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y-18)
        self.player = player
    
    def update(self) -> None:
        if pygame.sprite.collide_rect(self, self.player):
            if self.item_type == 'ammo':
                self.player.ammo += 15
            if self.item_type == 'health':
                self.player.health += 25
                if self.player.health > self.player.max_health:
                    self.player.health = self.player.max_health
            if self.item_type == 'granade':
                self.player.num_grandes += 2

            self.kill()