from pygame.locals import *
from config import *
from baselevel import BaseLevel
from import_images import *
from plataform import Plataform
from player import Player, HealthBar
from enemy import Enemy
from items import ItemBox


class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 100, HEIGHT - 50, 150, 20, wood_img)
        plataforma2 = Plataform(self.plataform_group, 250, HEIGHT - 120, 150, 20, wood_img)
        plataforma3 = Plataform(self.plataform_group, 450, HEIGHT - 200, 300, 20, wood_img)
        plataforma4 = Plataform(self.plataform_group, 950, HEIGHT - 200, 200, 20, wood_img)
        plataforma5 = Plataform(self.plataform_group, 820, HEIGHT - 300, HEIGHT, 20, wood_img)
        plataforma6 = Plataform(self.plataform_group, 1050, HEIGHT - 400, HEIGHT, 20, wood_img)
        plataforma7 = Plataform(self.plataform_group, 680, HEIGHT - 500, 250, 20, wood_img)
        plataforma8 = Plataform(self.plataform_group, 1050, HEIGHT - 600, HEIGHT, 20, wood_img)
        plataforma9 = Plataform(self.plataform_group, 380, HEIGHT - 550, 250, 20, wood_img)
        plataforma10 = Plataform(self.plataform_group, 0, HEIGHT - 600, 320, 20, wood_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5, plataforma6, plataforma7, plataforma8, plataforma9, plataforma10]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        Enemy(self.enemy_group, enemy_two_animation_lists, 600, 460, 100, self.player, self.bullet_group, 450,750, 2, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 1050, 460, 100, self.player, self.bullet_group, 950,1150, 0, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 1060, 360, 100, self.player, self.bullet_group, 820,WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 1180, 260, 100, self.player, self.bullet_group, 1050,WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 1780, 320, 100, self.player, self.bullet_group, 1600,WIDTH, 2, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 500, 110, 100, self.player, self.bullet_group, 380,630, 2, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 1165, 60, 100, self.player, self.bullet_group, 1050,WIDTH, 0, -1)
        Enemy(self.enemy_group, enemy_two_animation_lists, 160, 60, 100, self.player, self.bullet_group, 0,320, 0, 1)
        ItemBox(self.item_box_group, 1220, 420, 'health', self.player)
        ItemBox(self.item_box_group, 1210, 320, 'ammo', self.player)
        ItemBox(self.item_box_group, 500, 170, 'granade', self.player)
        ItemBox(self.item_box_group, 150, 120, 'ammo', self.player)
        ItemBox(self.item_box_group, 600, 520, 'coin', self.player)
        ItemBox(self.item_box_group, 1050, 420, 'coin', self.player)
        ItemBox(self.item_box_group, 1145, 320, 'coin', self.player)
        ItemBox(self.item_box_group, 575, 170, 'coin', self.player)
        ItemBox(self.item_box_group, 1175, 120, 'coin', self.player)
        ItemBox(self.item_box_group, 220, 120, 'coin', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)
        self.bg = bg_lvl2