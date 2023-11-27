import pygame
from pygame.locals import *
from config import *
from import_images import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x,y) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((60, 60))
        self.rect = self.image.get_rect(topleft = (x,y))
        