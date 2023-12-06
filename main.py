import pygame
from pygame.locals import *
from config import *
from player import Player, HealthBar
from projectiles import Bullet, Granade
from items import ItemBox
from import_images import *
from enemy import Enemy
from functions import *
from plataform import Plataform

class BaseLevel:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.granade_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.item_box_group = pygame.sprite.Group()
        self.plataform_group = pygame.sprite.Group()
        self.elapsed_time = 0
        self.current_level = 0
        self.in_game = True
        self.game_over = False
        self.paused = False 
        self.level_pased = False
    def update(self):
        self.health_bar.draw(self.screen ,self.player.health)
        draw_text(self.screen, 'Ammo: ', font, 'Red',10, 30)
        for x in range(self.player.ammo):
            self.screen.blit(bullet_img, (90 + (x * 10), 35))
        draw_text(self.screen, 'Granades: ', font, 'Red',10, 50)
        for x in range(self.player.num_grandes):
            self.screen.blit(grande_img, (125 + (x * 15), 52))
        draw_text(self.screen, f'Score: {self.player.score}', font, 'Red', 10, 70)

        if self.in_game and not self.paused:
            self.elapsed_time += 1
            self.time = max(0, 300 - self.elapsed_time // FPS)

        draw_text(self.screen, f'Time: {self.time}', font, 'Red', 10, 90)

        #arreglar
        if self.player.shoot and self.player.active:
            if self.player.shoot_cooldown == 0 and self.player.ammo > 0:
                self.player.shoot_cooldown = 20
                Bullet(self.bullet_group, self.player.rect.centerx + (0.6 * self.player.rect.size[0] * self.player.direction), self.player.rect.centery, self.player.direction, self.enemy_group, self.player)
                self.player.ammo -= 1
                shoot_sound.play()
        if self.player.grande and self.player.grande_thrown == False and self.player.num_grandes > 0:
            Granade(self.granade_group, self.player.rect.centerx + (0.6 * self.player.rect.size[0] * self.player.direction), self.player.rect.top, self.player.direction, self.enemy_group, self.player)
            self.player.grande_thrown = True
            self.player.num_grandes -= 1
        
        if self.time < 0:
            self.game_over = True
        
        self.bullet_group.update()
        self.granade_group.update()
        self.explosion_group.update()
        self.item_box_group.update()
        self.player_group.update()
        self.enemy_group.update(self.screen) 
        self.plataform_group.update()
        pygame.display.flip()
    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.player_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.granade_group.draw(self.screen)
        self.item_box_group.draw(self.screen)
        self.explosion_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.plataform_group.draw(self.screen)
    
    def reset_level(self):
        self.game_over = False
        self.in_game = True
        self.player_group.empty()

class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, WIDTH - 600, HEIGHT - 100, 600, 20, dirt_img)
        plataforma2 = Plataform(self.plataform_group, WIDTH - 1100, HEIGHT - 200, 400, 20, dirt_img)
        plataforma3 = Plataform(self.plataform_group, 0, HEIGHT - 300, 700, 20, dirt_img)
        plataforma4 = Plataform(self.plataform_group, 800, HEIGHT - 400, 330, 20, dirt_img)
        plataforma5 = Plataform(self.plataform_group, WIDTH - 640, HEIGHT - 500, 640, 20, dirt_img)
        plataforma6 = Plataform(self.plataform_group, 830, HEIGHT - 600, 330, 20, dirt_img)
        plataforma7 = Plataform(self.plataform_group, 0, HEIGHT - 700, 700, 20, dirt_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5, plataforma6, plataforma7]
        self.player = Player(self.player_group, player_animation_lists, 10, 2, 0, HEIGHT, 100, self.plataform_list) 
        self.enemy = Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 60, HEIGHT - 160, 100, self.player, self.bullet_group, WIDTH - 600, WIDTH)
        self.enemy2 = Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 1040, HEIGHT - 260, 100, self.player, self.bullet_group, 819, 1219)
        self.enemy3 = Enemy(self.enemy_group, enemy_animation_lists, 0, HEIGHT - 360, 100, self.player, self.bullet_group, 0, 700)
        self.enemy4 = Enemy(self.enemy_group, enemy_animation_lists, WIDTH - 60, HEIGHT - 560, 100, self.player, self.bullet_group, 1280, WIDTH)
        self.enemy5 = Enemy(self.enemy_group, enemy_animation_lists, 1280, HEIGHT - 560, 100, self.player, self.bullet_group, 1280, WIDTH)
        self.enemy6 = Enemy(self.enemy_group, enemy_animation_lists, 0, HEIGHT - 760, 100, self.player, self.bullet_group, 0, 700)
        self.item_box = ItemBox(self.item_box_group, WIDTH - 20, HEIGHT - 100, 'health', self.player)
        self.item_box = ItemBox(self.item_box_group, WIDTH - 1050, HEIGHT - 200, 'ammo', self.player)
        self.item_box = ItemBox(self.item_box_group, 950, HEIGHT - 400, 'granade', self.player)
        self.item_box = ItemBox(self.item_box_group, WIDTH - 20, HEIGHT - 500, 'ammo', self.player)
        self.item_box = ItemBox(self.item_box_group, WIDTH - 300, HEIGHT - 500, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 980, 665, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, WIDTH - 300, HEIGHT - 100, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 400, HEIGHT - 300, 'coin', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)
        self.bg = bg_lvl1

class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 300, HEIGHT - 100, 200, 20, wood_img)
        plataforma2 = Plataform(self.plataform_group, 500, HEIGHT - 200, 200, 20, wood_img)
        plataforma3 = Plataform(self.plataform_group, 700, HEIGHT - 300, 400, 20, wood_img)
        plataforma4 = Plataform(self.plataform_group, WIDTH - 200, HEIGHT - 300, 200, 20, wood_img)
        plataforma5 = Plataform(self.plataform_group, 1200, HEIGHT - 400, HEIGHT, 20, wood_img)
        plataforma6 = Plataform(self.plataform_group, 1600, HEIGHT - 500, HEIGHT, 20, wood_img)
        plataforma7 = Plataform(self.plataform_group, 1200, HEIGHT - 600, 300, 20, wood_img)
        plataforma8 = Plataform(self.plataform_group, 1600, HEIGHT - 700, HEIGHT, 20, wood_img)
        plataforma9 = Plataform(self.plataform_group, 700, HEIGHT - 700, 400, 20, wood_img)
        plataforma10 = Plataform(self.plataform_group, 0, HEIGHT - 800, 670, 20, wood_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5, plataforma6, plataforma7, plataforma8, plataforma9, plataforma10]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        self.enemy = Enemy(self.enemy_group, enemy_two_animation_lists, 890, 720, 100, self.player, self.bullet_group, 700,1100)
        self.enemy2 = Enemy(self.enemy_group, enemy_two_animation_lists, 1800, 720, 100, self.player, self.bullet_group, 1720,WIDTH)
        self.enemy3 = Enemy(self.enemy_group, enemy_two_animation_lists, 1800, 620, 100, self.player, self.bullet_group, 1200,WIDTH)
        self.enemy4 = Enemy(self.enemy_group, enemy_two_animation_lists, 1750, 520, 100, self.player, self.bullet_group, 1600,WIDTH)
        self.enemy5 = Enemy(self.enemy_group, enemy_two_animation_lists, 1780, 320, 100, self.player, self.bullet_group, 1600,WIDTH)
        self.enemy6 = Enemy(self.enemy_group, enemy_two_animation_lists, 895, 320, 100, self.player, self.bullet_group, 700,1100)
        self.enemy7 = Enemy(self.enemy_group, enemy_two_animation_lists, 350, 220, 100, self.player, self.bullet_group, 0,670)
        self.item_box = ItemBox(self.item_box_group, 1880, 680, 'health', self.player)
        self.item_box = ItemBox(self.item_box_group, 1880, 580, 'ammo', self.player)
        self.item_box = ItemBox(self.item_box_group, 955, 380, 'granade', self.player)
        self.item_box = ItemBox(self.item_box_group, 480, 280, 'ammo', self.player)
        self.item_box = ItemBox(self.item_box_group, 880, 780, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 1600, 680, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 1340, 480, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 1770, 380, 'coin', self.player)
        self.item_box = ItemBox(self.item_box_group, 170, 280, 'coin', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)
        self.bg = bg_lvl2


# class Level3(BaseLevel):
#     def __init__(self):
#         super().__init__()
#         plataforma1 = Plataform(self.plataform_group, 100, HEIGHT - 50, 200, 20, dirt_img)
#         plataforma2 = Plataform(self.plataform_group, 400, HEIGHT - 100, 150, 20, dirt_img)
#         plataforma3 = Plataform(self.plataform_group, 600, HEIGHT - 200, 180, 20, dirt_img)
#         self.plataform_list = [plataforma1, plataforma2, plataforma3]
#         self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
#         #self.enemy = Enemy(self.enemy_group, enemy_animation_lists, 450, HEIGHT - 60, 100, self.player, self.bullet_group)
#         #self.enemy2 = Enemy(self.enemy_group, enemy_animation_lists, 600, HEIGHT - 60, 100, self.player, self.bullet_group)
#         self.item_box = ItemBox(self.item_box_group, 300, HEIGHT, 'ammo', self.player)
#         self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)

class Game(BaseLevel):
    def __init__(self) -> None:
        super().__init__()
        self.levels = [Level1(), Level2()]
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Call Of Duty')
        pygame.display.set_icon(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\0.png'))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F1):
                    running = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.toggle_pause()
                if event.type == KEYDOWN and event.key == K_r:
                    self.reset_level()

            print(pygame.mouse.get_pos())
            if self.in_game:
                self.levels[self.current_level].draw()
                self.levels[self.current_level].update()
            
            if self.paused:
                self.screen.fill((150, 150, 150))
                draw_text_mid(self.screen, 'Pause', title_font, 'Black', 70)
                draw_text_mid(self.screen, 'Press ESC to back', title_font, 'Black', 900)
            
            if self.game_over:
                self.screen.fill((150, 150, 150))
                draw_text_mid(self.screen, 'Game Over', title_font, 'Black', 70)
                draw_text_mid(self.screen, 'Press R to restart', title_font, 'Black', 900)
        
            self.clock.tick(FPS)
            pygame.display.flip()
        self.close()
    
    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.in_game = False
        else:
            self.in_game = True

    def close(self):
        pygame.quit()

