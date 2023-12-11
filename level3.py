from pygame.locals import *
from config import *
from baselevel import BaseLevel
from import_images import *
from plataform import Plataform
from player import Player, HealthBar
from enemy import Enemy
from items import ItemBox


class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 1025, HEIGHT - 100, WIDTH, 20, wood_img)
        plataforma2 = Plataform(self.plataform_group, 705, HEIGHT - 200, 185, 20, wood_img)
        plataforma3 = Plataform(self.plataform_group, 1025, HEIGHT - 300, WIDTH, 20, wood_img)
        plataforma4 = Plataform(self.plataform_group, 705, HEIGHT - 400, 185, 20, wood_img)
        plataforma5 = Plataform(self.plataform_group, 1025, HEIGHT - 500, WIDTH, 20, wood_img)
        plataforma6 = Plataform(self.plataform_group, 350, HEIGHT - 300, 250, 20, wood_img)
        plataforma7 = Plataform(self.plataform_group, 0, HEIGHT - 200, 250, 20, wood_img)
        plataforma8 = Plataform(self.plataform_group, 0, HEIGHT - 400, 250, 20, wood_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5, plataforma6, plataforma7, plataforma8]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        Enemy(self.enemy_group, enemy_three_animation_lists, 470, 360, 100, self.player, self.bullet_group, 350,600, 2, 1)
        Enemy(self.enemy_group, enemy_three_animation_lists, 1150, 560, 100, self.player, self.bullet_group, 1025,WIDTH, 2, 1)
        Enemy(self.enemy_group, enemy_three_animation_lists, 1150, 360, 100, self.player, self.bullet_group, 1025,WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_three_animation_lists, 1150, 160, 100, self.player, self.bullet_group, 1025,WIDTH, 2, 1)
        Enemy(self.enemy_group, enemy_three_animation_lists, 120, 260, 100, self.player, self.bullet_group, 0,WIDTH, 0, 1)
        Enemy(self.enemy_group, enemy_three_animation_lists, 120, 460, 100, self.player, self.bullet_group, 0,WIDTH, 0, 1)
        Enemy(self.enemy_group, enemy_boss_animation_lists, 1000, HEIGHT - 60, 200, self.player, self.bullet_group, 0,WIDTH, 2, 1)
        ItemBox(self.item_box_group, 1220, 420, 'health', self.player)
        ItemBox(self.item_box_group, 470, 420, 'ammo', self.player)
        ItemBox(self.item_box_group, 800, 520, 'granade', self.player)
        ItemBox(self.item_box_group, 65, 520, 'ammo', self.player)
        ItemBox(self.item_box_group, 1150, 620, 'coin', self.player)
        ItemBox(self.item_box_group, 510, 420, 'coin', self.player)
        ItemBox(self.item_box_group, 1150, 220, 'coin', self.player)
        ItemBox(self.item_box_group, 70, 320, 'coin', self.player)
        ItemBox(self.item_box_group, 200, 520, 'coin', self.player)
        ItemBox(self.item_box_group, 200, 320, 'health', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)
        self.bg = bg_lvl3