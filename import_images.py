import pygame
from pygame.locals import *

pygame.init()

idle = [pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\0.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\1.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\2.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\3.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\4.png'), (60, 60))]

idle_left = [pygame.transform.flip(image, True, False) for image in idle]

run_right = [pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\0.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\1.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\2.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\3.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\4.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\run\\5.png'), (60, 60))]

run_left = [pygame.transform.flip(image_run, True, False) for image_run in run_right]

jump = [pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\jump\\0.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\jump\\1.png'), (60, 60))]

death = [pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\0.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\1.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\2.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\3.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\4.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\5.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\6.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\death\\7.png'), (60, 60))]

death_left = [pygame.transform.flip(image_death, True, False) for image_death in death]

explosion = [pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\EXTRAS\\explosion\\exp1.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\explosion\\exp2.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\explosion\\exp3.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\explosion\\exp4.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\explosion\\exp5.png'), (60, 60))]

animation_lists = {
    'idle': idle,
    'idle_left': idle_left,
    'run_right': run_right,
    'run_left': run_left,
    'jump': jump,
    'death_right': death,
    'death_left': death_left,
    'explosion': explosion
}

bullet_img = pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\bullet.png')
grande_img = pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\grenade.png')

healt_box_img = pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\health_box.png')
ammo_box_img = pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\ammo_box.png')
granade_box_img = pygame.image.load('assets\\img\\CHARACTER_SPRITES\EXTRAS\\grenade_box.png')
item_boxes = {
    'health': healt_box_img,
    'ammo': ammo_box_img,
    'granade': granade_box_img
}
