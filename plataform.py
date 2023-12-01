import pygame
from pygame.locals import *
from config import *
from import_images import *

class Plataform(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height, image) -> None:
        super().__init__(groups)
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.plataform_group = groups