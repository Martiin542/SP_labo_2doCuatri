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

explosion = [pygame.transform.scale(pygame.image.load('assets\\img\\EXTRAS\\explosion\\exp1.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\EXTRAS\\explosion\\exp2.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\EXTRAS\\explosion\\exp3.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\EXTRAS\\explosion\\exp4.png'), (60, 60)),
             pygame.transform.scale(pygame.image.load('assets\\img\\EXTRAS\\explosion\\exp5.png'), (60, 60))]

player_animation_lists = {
    'idle': idle,
    'idle_left': idle_left,
    'run_right': run_right,
    'run_left': run_left,
    'jump': jump,
    'death_right': death,
    'death_left': death_left,
    'explosion': explosion
}

idle_enemy = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\idle\\0.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\idle\\1.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\idle\\2.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\idle\\3.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\idle\\4.png'), (60, 60))]

idle_left_enemy = [pygame.transform.flip(image, True, False) for image in idle_enemy]

run_right_enemy = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\0.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\1.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\2.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\3.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\4.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\run\\5.png'), (60, 60))]

run_left_enemy = [pygame.transform.flip(image, True, False) for image in run_right_enemy]

death_enemy = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\0.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\1.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\2.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\3.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\4.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\5.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\6.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES\\death\\7.png'), (60, 60))]

death_left_enemy = [pygame.transform.flip(image_death, True, False) for image_death in death_enemy]

enemy_animation_lists = {
    'idle': idle_enemy,
    'idle_left': idle_left_enemy,
    'run_right': run_right_enemy,
    'run_left': run_left_enemy,
    'death_right': death_enemy,
    'death_left': death_left_enemy
}

bullet_img = pygame.image.load('assets\\img\\EXTRAS\\bullet.png')
grande_img = pygame.image.load('assets\\img\\EXTRAS\\grenade.png')

healt_box_img = pygame.image.load('assets\\img\\EXTRAS\\health_box.png')
ammo_box_img = pygame.image.load('assets\\img\\EXTRAS\\ammo_box.png')
granade_box_img = pygame.image.load('assets\\img\EXTRAS\\grenade_box.png')
coin_img = pygame.image.load('assets\\img\\EXTRAS\\coin.png')
item_boxes = {
    'health': healt_box_img,
    'ammo': ammo_box_img,
    'granade': granade_box_img,
    'coin': coin_img
}


dirt_img = pygame.image.load('assets\\img\\PLATAFORM\\dirt.png')

jump_sound = pygame.mixer.Sound("assets\\sounds\\jump.wav")
jump_sound.set_volume(0.5)
shoot_sound = pygame.mixer.Sound("assets\\sounds\\shot.wav")
shoot_sound.set_volume(0.2)
granade_sound = pygame.mixer.Sound("assets\\sounds\\grenade.wav")
granade_sound.set_volume(0.2)
music = pygame.mixer.Sound("assets\\sounds\\music2.mp3")

#menu
bg_menu = pygame.image.load('assets\\img\\MENUIMG\\menu_bg.png')
