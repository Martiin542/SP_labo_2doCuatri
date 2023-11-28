import pygame
from pygame.locals import *
from config import *
from import_images import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, direction) -> None:
        super().__init__(groups)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
    
    def update(self):
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Granade(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, direction, explosion_group) -> None:
        super().__init__(groups)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grande_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.explosion_group = explosion_group
    
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
            Explosion(self.explosion_group, self.rect.x, self.rect.y, animation_lists)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, animation_lists) -> None:
        super().__init__(groups)
        self.animation_lists = animation_lists
        self.time_animation = 150
        self.current_animation = self.animation_lists['explosion']
        self.current_sprite = 0
        self.image = self.current_animation[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y - 30))
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]
        
        if self.current_sprite == len(self.current_animation) - 1:
            self.kill()

