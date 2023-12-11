from pygame.locals import *
from config import *
from baselevel import BaseLevel
from import_images import *
from plataform import Plataform
from player import Player, HealthBar
from enemy import Enemy
from items import ItemBox


class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 950, HEIGHT - 100, 600, 20, dirt_img)
        plataforma2 = Plataform(self.plataform_group, 550, HEIGHT - 185, 300, 20, dirt_img)
        plataforma3 = Plataform(self.plataform_group, 0, HEIGHT - 250, 450, 20, dirt_img)
        plataforma4 = Plataform(self.plataform_group, 525, HEIGHT - 350, 330, 20, dirt_img)
        plataforma5 = Plataform(self.plataform_group, 980, HEIGHT - 450, 640, 20, dirt_img)
        plataforma6 = Plataform(self.plataform_group, 500, HEIGHT - 550, 330, 20, dirt_img)
        plataforma7 = Plataform(self.plataform_group, 0, HEIGHT - 600, 430, 20, dirt_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5, plataforma6, plataforma7]
        self.player = Player(self.player_group, player_animation_lists, 10, 2, 0, HEIGHT, 100, self.plataform_list) 
        Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 60, HEIGHT - 160, 100, self.player, self.bullet_group, 950, WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 1040, 410, 100, self.player, self.bullet_group, 0, 450, 2, -1)
        Enemy(self.enemy_group, enemy_animation_lists, 685, 475, 100, self.player, self.bullet_group, 550, 850, 2, -1)
        Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 60, 210, 100, self.player, self.bullet_group, 980, WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_animation_lists, 15, 60, 100, self.player, self.bullet_group, 0, 430, 2, -1)
        Enemy(self.enemy_group, enemy_animation_lists, 300, 60, 100, self.player, self.bullet_group, 0, 430, 2, -1)
        ItemBox(self.item_box_group, 575, 370, 'health', self.player)
        ItemBox(self.item_box_group, 30, 470, 'ammo', self.player)
        ItemBox(self.item_box_group, 795, 370, 'granade', self.player)
        ItemBox(self.item_box_group, 770, 170, 'ammo', self.player)
        ItemBox(self.item_box_group, 675, 535, 'coin', self.player)
        ItemBox(self.item_box_group, 235, 470, 'coin', self.player)
        ItemBox(self.item_box_group, 1135, 270, 'coin', self.player)
        ItemBox(self.item_box_group, 205, 120, 'coin', self.player)
        ItemBox(self.item_box_group, 205, 120, 'coin', self.player)
        ItemBox(self.item_box_group, 1115, 620, 'coin', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)
        self.bg = bg_lvl1