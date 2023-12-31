import pygame
from pygame.locals import *
from config import *
from import_images import *
from functions import *
from data import save_max_score


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
        self.score = 0
        self.max_score = 0
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
        #grande
        self.grande = False
        self.grande_thrown = False
        self.num_grandes = granades
        #plataformas bug
        self.can_jump = False

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
            
        if self.rect.bottom == HEIGHT:
            self.can_jump = True
        
        for platform in self.plataform_list:
            if pygame.sprite.collide_rect(self, platform):
                self.rect.bottom = platform.rect.top
                self.vel_y = 0  # Reset vertical velocity when landing on a platform
                self.can_jump = True

        if keys[K_w] and self.can_jump:
            self.vel_y = -15
            self.current_animation = self.animation_lists['jump']
            self.can_jump = False
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
            
        if self.health <= 0:
            self.die()

        self.animate()
        if self.score > self.max_score:
            self.max_score = self.score
            save_max_score(self.max_score)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_animation:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_sprite]

    def die(self):
        self.active = False
        self.health = 0
        self.speed = 0
        self.vel_y = 0
        if self.direction == 1:
            self.current_animation = self.animation_lists['death_right']
        elif self.direction == -1:
            self.current_animation = self.animation_lists['death_left']
        
        self.image = self.current_animation[self.current_sprite]

        if self.current_sprite == len(self.current_animation) - 1:
            self.kill()
        else:
            self.animate()

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

