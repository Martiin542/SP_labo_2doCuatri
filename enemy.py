import pygame
from pygame.locals import *
from config import *
from import_images import *
from projectiles import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, animation_lists, x,y, max_health, player, bullet_group) -> None:
        super().__init__(groups)
        self.enemy_group = groups
        self.active = True
        self.animation_lists = animation_lists
        self.current_animation = self.animation_lists['run_right']
        self.current_sprite = 0
        self.image = self.current_animation[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 0
        self.direction = 1
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 150
        self.health = max_health
        self.player = player
        self.bullet_group = bullet_group
        self.shoot_cooldown = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
    
    def update(self, screen):
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.health <= 0:
            self.restet_stats()
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        self.ia(screen)
        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]

    def ia(self, screen):
        if self.active and self.player.active:
            if self.vision.colliderect(self.player.rect):
                if self.direction == 1:
                    self.current_animation = self.animation_lists['idle']
                elif self.direction == -1:
                    self.current_animation = self.animation_lists['idle_left']
                if self.shoot_cooldown == 0:
                    self.shoot_cooldown = 20
                    Bullet(self.bullet_group, self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, self.enemy_group, self.player)
            else:
                self.rect.x += self.direction * self.speed
                self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                pygame.draw.rect(screen, 'Red', self.vision)
                if self.rect.right > WIDTH or self.rect.left < 400:
                    self.direction *= -1
                
                if self.direction == 1:
                    self.current_animation = self.animation_lists['run_right']
                elif self.direction == -1:
                    self.current_animation = self.animation_lists['run_left']
    
    def restet_stats(self):
        self.active = False
        self.health = 0
        self.speed = 0
        if self.direction == 1:
            self.current_animation = self.animation_lists['death_right']
        elif self.direction == -1:
            self.current_animation = self.animation_lists['death_left']
        if self.current_sprite == len(self.current_animation) - 1:
            self.kill()
        else:
            self.animate()
    
