import pygame
from pygame.locals import *
from config import *
from player import Player, Bullet
from import_images import animation_lists
from enemy import Enemy

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Juego CLASS")
        pygame.display.set_icon(pygame.image.load("assets\\img\\iconopng.png"))
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #agrego un grupo de sprites 
        self.all_sprites = pygame.sprite.Group()
        #inicializo el player y le paso los grupos de sprite donde pertenece
        self.player = Player([self.all_sprites], animation_lists, 5, 0, HEIGHT) #hay q pasarle una lista de los grupos q tiene mi player
        self.enemy = Enemy([self.all_sprites], 100, HEIGHT - 60)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
            self.draw()
            self.update()
            
            self.clock.tick(FPS)
        self.close()

    def update(self):
        if self.player.shooting:
            if self.player.shoot_cooldown == 0 and self.player.ammo > 0:
                self.player.shoot_cooldown = 20
                Bullet([self.all_sprites], self.player.rect.centerx + (0.6 * self.player.rect.size[0] * self.player.direction), self.player.rect.centery, self.player.direction)
                self.player.ammo -= 1
        
        self.all_sprites.update() #invoca el metodo update de cada uno de los sprites, en el caso de Player termina llamano al metodo que le creamos 
        pygame.display.flip()

    def draw(self):
        self.screen.fill((150,150,150))
        self.all_sprites.draw(self.screen) #por cada uno de los slpite hace el blit, asi aunque player no tenga un metodo draw echo por nosotros funciona igual 

    def close(self):
        pygame.quit()


game = Game()
game.run()






