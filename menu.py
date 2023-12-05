import pygame
from pygame.locals import *
from config import *
from functions import *
from import_images import *
from main import *

class MainMenu():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Call Of Duty")
        pygame.display.set_icon(pygame.image.load('assets\\img\\CHARACTER_SPRITES\\idle\\0.png'))
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.selected_level = None

    def show(self):
        self.clock.tick(FPS)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
            
            self.screen.fill((150, 150, 150))
            label_mid(self.screen, idle[0], 150, 3)
            draw_text_mid(self.screen, 'Call Of Duty', title_font, 'Black', 70)
            play_button_clicked = button(self.screen, 300, 420, 200, 50, (150,150,150), (100, 100, 100), 'play', title_font, 'Black', 6, 1)
            exit_button_clicked = button(self.screen, 300, 480, 200, 50, (150,150,150), (100, 100, 100), 'exit', title_font, 'Black', 6, 1)
            ranking_button_clicked = button(self.screen, 300, 550, 200, 50, (150,150,150), (100, 100, 100), 'ranking', title_font, 'Black', 6, 1)

            if play_button_clicked:
                LevelSelector.show(self)
            if ranking_button_clicked:
                Ranking.show(self)
            if exit_button_clicked:
                self.running = False
            

            pygame.display.flip()

class LevelSelector(MainMenu):
    def __init__(self) -> None:
        super().__init__()

    def show(self):
        self.clock.tick(FPS)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
            
            self.screen.fill((150, 150, 150))
            label_mid(self.screen, idle[0], 150, 3)
            draw_text_mid(self.screen, 'Level Selector', title_font, 'Black', 70)
            level1 = button(self.screen, 50, 420, 200, 50, (150,150,150), (100, 100, 100), 'Level 1', lvl_font, 'Black', 6, 1)
            level2 = button(self.screen, 50, 480, 200, 50, (150,150,150), (100, 100, 100), 'Level 2', lvl_font, 'Black', 6, 1)
            exit = button(self.screen, 50, 550, 200, 50, (150,150,150), (100, 100, 100), 'Exit', lvl_font, 'Black', 6, 1)

            if exit:
                self.running = False
            if level1:
                game.current_level = 0
                game.run()
                self.running = False
            if level2:
                game.current_level = 1
                game.run()
                self.running = False
            
            pygame.display.flip()


class Ranking(MainMenu):
    def __init__(self) -> None:
        super().__init__()
    
    def show(self):
        self.clock.tick(FPS)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
            
            self.screen.fill((150, 150, 150))
            label_mid(self.screen, idle[0], 150, 3)
            draw_text_mid(self.screen, 'Ranking', title_font, 'Black', 70)
            back_button = button(self.screen, 0, 550, 200, 50, (150,150,150), (100, 100, 100), 'back', title_font, 'Black', 6, 1)

            if back_button:
                MainMenu.show(self)

            pygame.display.flip()

game = Game()
menu = MainMenu()
menu.show()
