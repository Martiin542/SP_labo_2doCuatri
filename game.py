import pygame
from pygame.locals import *
from config import *
from baselevel import BaseLevel
from level1 import Level1
from level2 import Level2
from level3 import Level3
from functions import draw_text_mid

class Game(BaseLevel):
    def __init__(self) -> None:
        super().__init__()
        self.levels = [Level1(), Level2(), Level3()]
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
                # if event.type == KEYDOWN and event.key == K_r:
                #     self.reset_level()

            if self.in_game:
                self.levels[self.current_level].draw()
                self.levels[self.current_level].update()
            
            if self.paused:
                self.screen.fill((150, 150, 150))
                draw_text_mid(self.screen, 'Pause', title_font, 'Black', 70)
                draw_text_mid(self.screen, 'Press ESC to back', title_font, 'Black', 400)
            
            if self.game_over:
                self.screen.fill((150, 150, 150))
                draw_text_mid(self.screen, 'Game Over', title_font, 'Black', 70)
                draw_text_mid(self.screen, 'Press R to restart', title_font, 'Black', 900)
        
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