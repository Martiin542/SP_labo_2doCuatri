import pygame
from pygame.locals import *
from config import *
from import_images import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, animation_lists, ammo, granades, x, y, max_health, plataform_list) -> None:
        super().__init__(groups) 
        self.active = True
        self.animation_lists = animation_lists
        self.time_animation = 150
        self.current_animation = self.animation_lists['idle']
        self.current_sprite = 0
        self.image = self.current_animation[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 5
        self.direction = 1
        self.vel_y = 0  # Velocidad vertical
        self.gravity = 1
        self.last_update = pygame.time.get_ticks()
        self.max_health = max_health
        self.health = max_health
        self.plataform_list = plataform_list
        #shoot
        self.shoot = False
        self.shoot_cooldown = 0
        self.ammo = ammo
        #self.start_ammo = self.ammo #ver si sirve ???
        #grande
        self.grande = False
        self.grande_thrown = False
        self.num_grandes = granades

        self.in_plataform = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.in_plataform = False
        for platform in self.plataform_list:
            if pygame.sprite.collide_rect(self, platform):
                self.rect.bottom = platform.rect.top
                self.vel_y = 0  # Reset vertical velocity when landing on a platform
                self.in_plataform = True
                break

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
            
        
        if keys[K_w] and self.rect.bottom == HEIGHT or self.in_plataform:
            self.vel_y = -15
            self.current_animation = self.animation_lists['jump']
            jump_sound.play()
        
        if keys[K_SPACE]:
            self.shoot = True
        else:
            self.shoot = False
        
        if keys[K_q]:
            self.grande = True
        else:
            self.grande = False
            self.grande_thrown = False
            
            
        self.animate()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]

class HealthBar():
    def __init__(self, x, y, health, max_health) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
    
    def draw(self, screen, helath):
        self.health = helath
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, 'Black', (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, 'Red', (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, 'Green', (self.x, self.y, 150 * ratio, 20))

