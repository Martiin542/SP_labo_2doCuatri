import pygame
from pygame.locals import *
from config import *
from functions import draw_text
from projectiles import Bullet, Granade
from import_images import *
from data import initialize_database

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
        self.time = 0
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
            self.time = max(0, 5 - self.elapsed_time // FPS)

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
        
        if self.time <= 0 or self.player.health:
            self.game_over = True
        
        print(self.game_over)

        initialize_database()
        
        self.bullet_group.update()
        self.granade_group.update()
        self.explosion_group.update()
        self.item_box_group.update()
        self.player_group.update()
        self.enemy_group.update() 
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
