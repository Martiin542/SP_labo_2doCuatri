import pygame
from pygame.locals import *
from config import *

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
########
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
###########
idle_enemy_two = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\idle\\0.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\idle\\1.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\idle\\2.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\idle\\3.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\idle\\4.png'), (60, 60))]

idle_left_enemy_two = [pygame.transform.flip(image, True, False) for image in idle_enemy_two]

run_right_enemy_two = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\0.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\1.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\2.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\3.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\4.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\run\\5.png'), (60, 60))]

run_left_enemy_two = [pygame.transform.flip(image, True, False) for image in run_right_enemy_two]

death_enemy_two = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\0.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\1.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\2.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\3.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\4.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\5.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\6.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES2\\death\\7.png'), (60, 60))]

death_left_enemy_two = [pygame.transform.flip(image_death, True, False) for image_death in death_enemy_two]

enemy_two_animation_lists = {
    'idle': idle_enemy_two,
    'idle_left': idle_left_enemy_two,
    'run_right': run_right_enemy_two,
    'run_left': run_left_enemy_two,
    'death_right': death_enemy_two,
    'death_left': death_left_enemy_two
}
#####
idle_enemy_three = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\0.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\1.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\2.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\3.png'), (60, 60)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\4.png'), (60, 60))]

idle_left_enemy_three = [pygame.transform.flip(image, True, False) for image in idle_enemy_three]

run_right_enemy_three = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\0.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\1.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\2.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\3.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\4.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\5.png'), (60, 60))]

run_left_enemy_three = [pygame.transform.flip(image, True, False) for image in run_right_enemy_three]

death_enemy_three = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\0.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\1.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\2.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\3.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\4.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\5.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\6.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\7.png'), (60, 60))]

death_left_enemy_three = [pygame.transform.flip(image_death, True, False) for image_death in death_enemy_three]

enemy_three_animation_lists = {
    'idle': idle_enemy_three,
    'idle_left': idle_left_enemy_three,
    'run_right': run_right_enemy_three,
    'run_left': run_left_enemy_three,
    'death_right': death_enemy_three,
    'death_left': death_left_enemy_three
}
#####
idle_enemy_boss = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\0.png'), (100, 100)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\1.png'), (100, 100)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\2.png'), (100, 100)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\3.png'), (100, 100)),
              pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\idle\\4.png'), (100, 100))]

idle_left_enemy_boss = [pygame.transform.flip(image, True, False) for image in idle_enemy_boss]

run_right_enemy_boss = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\0.png'), (100, 100)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\1.png'), (100, 100)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\2.png'), (100, 100)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\3.png'), (100, 100)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\4.png'), (100, 100)),
                   pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\run\\5.png'), (100, 100))]

run_left_enemy_boss = [pygame.transform.flip(image, True, False) for image in run_right_enemy_boss]

death_enemy_boss = [pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\0.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\1.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\2.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\3.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\4.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\5.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\6.png'), (100, 100)),
         pygame.transform.scale(pygame.image.load('assets\\img\\ENEMY_SPRITES3\\death\\7.png'), (100, 100))]

death_left_enemy_boss = [pygame.transform.flip(image_death, True, False) for image_death in death_enemy_boss]

enemy_boss_animation_lists = {
    'idle': idle_enemy_boss,
    'idle_left': idle_left_enemy_boss,
    'run_right': run_right_enemy_boss,
    'run_left': run_left_enemy_boss,
    'death_right': death_enemy_boss,
    'death_left': death_left_enemy_boss
}


bullet_img = pygame.image.load('assets\\img\\EXTRAS\\bullet.png')
grande_img = pygame.image.load('assets\\img\\EXTRAS\\grenade.png')

healt_box_img = pygame.image.load('assets\\img\\EXTRAS\\health_box.png')
ammo_box_img = pygame.image.load('assets\\img\\EXTRAS\\ammo_box.png')
granade_box_img = pygame.image.load('assets\\img\EXTRAS\\grenade_box.png')
coin_img = pygame.image.load('assets\\img\\EXTRAS\\coin.png')
coin_img = pygame.transform.scale(coin_img, (30,30))
item_boxes = {
    'health': healt_box_img,
    'ammo': ammo_box_img,
    'granade': granade_box_img,
    'coin': coin_img
}


dirt_img = pygame.image.load('assets\\img\\PLATAFORM\\dirt.png')
wood_img = pygame.image.load('assets\\img\\PLATAFORM\\wood.png')

jump_sound = pygame.mixer.Sound("assets\\sounds\\jump.wav")
jump_sound.set_volume(0.5)
shoot_sound = pygame.mixer.Sound("assets\\sounds\\shot.wav")
shoot_sound.set_volume(0.2)
granade_sound = pygame.mixer.Sound("assets\\sounds\\grenade.wav")
granade_sound.set_volume(0.2)
music = pygame.mixer.Sound("assets\\sounds\\music2.mp3")
music.set_volume(0.05)

#menu
bg_lvl1 = pygame.image.load('assets\\img\\BGS\\bg1.jpg')
bg_lvl1 = pygame.transform.scale(bg_lvl1, (WIDTH, HEIGHT))

bg_lvl2 = pygame.image.load('assets\\img\\BGS\\bg2.jpg')
bg_lvl2 = pygame.transform.scale(bg_lvl2, (WIDTH, HEIGHT))

bg_lvl3 = pygame.image.load('assets\\img\\BGS\\bg3.jpg')
bg_lvl3 = pygame.transform.scale(bg_lvl3, (WIDTH, HEIGHT))