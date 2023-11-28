import pygame
from pygame.locals import *
from config import *
from import_images import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, direction, enemy_group, player) -> None:
        super().__init__(groups)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.bullet_group = groups
        self.enemies = enemy_group
        self.player = player

    
    def update(self):
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
        
        for enemy in self.enemies:
            if enemy.active:
                hits_to_enemys = pygame.sprite.spritecollide(enemy, self.bullet_group, True)
                for _ in hits_to_enemys:
                        enemy.health -= 25
        if self.player.active:
            hits_to_player = pygame.sprite.spritecollide(self.player, self.bullet_group, True)
            for _ in hits_to_player:
                    self.player.health -= 25

class Granade(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, direction, enemy, player) -> None:
        super().__init__(groups)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grande_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.explosion_group = groups
        self.enemy = enemy
        self.player = player
    
    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        if self.rect.bottom + dy > HEIGHT:
            dy = HEIGHT - self.rect.bottom
            self.speed = 0
        
        if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH:
            self.direction *= -1
        
        self.rect.x += dx
        self.rect.y += dy

        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(self.explosion_group, self.rect.x, self.rect.y, animation_lists, self.enemy, self.player)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, animation_lists, enemy_group, player) -> None:
        super().__init__(groups)
        self.animation_lists = animation_lists
        self.time_animation = 150
        self.current_animation = self.animation_lists['explosion']
        self.current_sprite = 0
        self.image = self.current_animation[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y - 30))
        self.last_update = pygame.time.get_ticks()
        self.explosion_group = groups
        self.enemies = enemy_group
        self.player = player
        self.collided_with_enemy = False
        self.collided_with_player = False
        self.reset_flags()
    
    def reset_flags(self):
        self.collided_with_enemy = False
        self.collided_with_player = False
    
    def update(self):
        self.animate()
        for enemy in self.enemies:
            if enemy.active and not self.collided_with_enemy:
                granades_to_enemys = pygame.sprite.spritecollide(enemy, self.explosion_group, False)
                for _ in granades_to_enemys:
                    enemy.health -= 50
                self.collided_with_enemy = True
        
        if self.player.active and not self.collided_with_player:
            granades_to_player = pygame.sprite.spritecollide(self.player, self.explosion_group, False)
            for _ in granades_to_player:
                self.player.health -= 50
            self.collided_with_player = True
        

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]
        
        if self.current_sprite == len(self.current_animation) - 1:
            self.kill()

