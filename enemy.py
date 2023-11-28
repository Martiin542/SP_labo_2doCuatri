import pygame
from pygame.locals import *
from config import *
from import_images import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, animation_lists, x,y, max_health) -> None:
        super().__init__(groups)
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
        #self.max_health = max_health
        self.death_animation_played = False
    
    def update(self):
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Simple movement for the enemy
        self.rect.x += self.direction * self.speed

        # Change direction when hitting the screen edge
        if self.rect.right > WIDTH or self.rect.left < 400:
            self.direction *= -1
        
        if self.direction == 1:
            self.current_animation = self.animation_lists['run_right']
        elif self.direction == -1:
            self.current_animation = self.animation_lists['run_left']

        if self.health <= 0:
            self.restet_stats()

        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]
    
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