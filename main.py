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
        self.game_time = 180
    def update(self):
        self.health_bar.draw(self.screen ,self.player.health)
        draw_text(self.screen, 'Ammo: ', font, 'Red',10, 30)
        for x in range(self.player.ammo):
            self.screen.blit(bullet_img, (90 + (x * 10), 35))
        draw_text(self.screen, 'Granades: ', font, 'Red',10, 50)
        for x in range(self.player.num_grandes):
            self.screen.blit(grande_img, (125 + (x * 15), 52))
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

        print(self.player.can_jump)
        
        self.bullet_group.update()
        self.granade_group.update()
        self.explosion_group.update()
        self.item_box_group.update()
        self.player_group.update()
        self.enemy_group.update(self.screen) 
        self.plataform_group.update()
        pygame.display.flip()
    def draw(self):
        self.screen.fill((150,150,150))
        self.player_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.granade_group.draw(self.screen)
        self.item_box_group.draw(self.screen)
        self.explosion_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.plataform_group.draw(self.screen)

class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 100, HEIGHT - 50, 200, 20, dirt_img)
        plataforma2 = Plataform(self.plataform_group, 400, HEIGHT - 100, 150, 20, dirt_img)
        plataforma3 = Plataform(self.plataform_group, 600, HEIGHT - 200, 180, 20, dirt_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        self.enemy = Enemy(self.enemy_group, enemy_animation_lists, 450, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.enemy2 = Enemy(self.enemy_group, enemy_animation_lists, 600, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.item_box = ItemBox(self.item_box_group, 300, HEIGHT, 'health', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)

class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 100, HEIGHT - 50, 200, 20, dirt_img)
        plataforma2 = Plataform(self.plataform_group, 400, HEIGHT - 100, 150, 20, dirt_img)
        plataforma3 = Plataform(self.plataform_group, 600, HEIGHT - 200, 180, 20, dirt_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        self.enemy = Enemy(self.enemy_group, enemy_animation_lists, 450, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.enemy2 = Enemy(self.enemy_group, enemy_animation_lists, 600, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.item_box = ItemBox(self.item_box_group, 300, HEIGHT, 'granade', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)

class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        plataforma1 = Plataform(self.plataform_group, 100, HEIGHT - 50, 200, 20, dirt_img)
        plataforma2 = Plataform(self.plataform_group, 400, HEIGHT - 100, 150, 20, dirt_img)
        plataforma3 = Plataform(self.plataform_group, 600, HEIGHT - 200, 180, 20, dirt_img)
        self.plataform_list = [plataforma1, plataforma2, plataforma3]
        self.player = Player(self.player_group, player_animation_lists, 15, 6, 0, HEIGHT, 100, self.plataform_list) 
        self.enemy = Enemy(self.enemy_group, enemy_animation_lists, 450, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.enemy2 = Enemy(self.enemy_group, enemy_animation_lists, 600, HEIGHT - 60, 100, self.player, self.bullet_group)
        self.item_box = ItemBox(self.item_box_group, 300, HEIGHT, 'ammo', self.player)
        self.health_bar = HealthBar(10, 10, self.player.health, self.player.max_health)

class Game(BaseLevel):
    def __init__(self) -> None:
        super().__init__()
        self.levels = [Level1(), Level2(), Level3()]
        self.current_level = 0
        self.in_game = True
        self.game_over = False
        self.paused = False 
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

            if self.in_game:
                self.levels[self.current_level].draw()
                self.levels[self.current_level].update()
            
            if self.paused:
                self.screen.fill((150, 150, 150))
                draw_text_mid(self.screen, 'Pause', title_font, 'Black', 70)
                
            
        
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
