import pygame
from pygame.locals import *
from config import *
from import_images import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, animation_lists, ammo, x, y) -> None:
        super().__init__(groups) 
        self.animation_lists = animation_lists
        self.current_animation = self.animation_lists['idle']
        self.current_sprite = 0
        self.image = self.current_animation[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 5
        self.direction = 1
        self.vel_y = 0  # Velocidad vertical
        self.gravity = 1
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 150
        self.shooting = False
        self.shoot_cooldown = 0
        self.ammo = ammo
        self.start_ammo = self.ammo #ver si sirve ???

    def update(self):
        keys = pygame.key.get_pressed()

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0

        if keys[K_d]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
            self.current_animation = self.animation_lists['run_right']
            self.direction = 1
        elif keys[K_a]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
            self.current_animation = self.animation_lists['run_left']
            self.direction = -1
        else:
            if self.direction == 1:
                self.current_animation = self.animation_lists['idle']
            elif self.direction == -1:
                self.current_animation = self.animation_lists['idle_left']
            
        
        if keys[K_w] and self.rect.bottom == HEIGHT:
            self.vel_y = -15
            self.current_animation = self.animation_lists['jump']
        
        if keys[K_SPACE]:
            self.shooting = True
        else:
            self.shooting = False
            
        self.animate()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, direction) -> None:
        super().__init__(groups)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        #self.player = player
    
    def update(self):
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

