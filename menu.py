import pygame
from pygame.locals import *
from config import *
from functions import *
from import_images import *
from game import Game
from data import load_max_score


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
        self.max_score = load_max_score()
        self.state_music = False
        self.music = music

    def show(self):
        self.clock.tick(FPS)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
            
            self.music.play(-1)
            
            self.screen.fill((150, 150, 150))
            label_mid(self.screen, idle[0], 150, 3)
            draw_text_mid(self.screen, 'Call Of Duty', title_font, 'Black', 70)
            play_button_clicked = button(self.screen, (WIDTH - 200) // 2, (HEIGHT - 50) // 2, 200, 50, (150,150,150), (100, 100, 100), 'play', title_font, 'Black', 6, 1)
            exit_button_clicked = button(self.screen, (WIDTH - 200) // 2, ((HEIGHT - 50) // 2) + 120, 200, 50, (150,150,150), (100, 100, 100), 'exit', title_font, 'Black', 6, 1)
            ranking_button_clicked = button(self.screen, (WIDTH - 200) // 2, ((HEIGHT - 50) // 2) + 60, 315, 50, (150,150,150), (100, 100, 100), 'ranking', title_font, 'Black', 6, 1)
            unmute_button_clicked = button(self.screen, (WIDTH - 200) // 2 + 400, HEIGHT - 100, 315, 50, (150,150,150), (100, 100, 100), 'Unmute', title_font, 'Black', 6, 1)
            mute_button_clicked = button(self.screen, (WIDTH - 200) // 2 + 400, HEIGHT - 150, 315, 50, (150,150,150), (100, 100, 100), 'Mute', title_font, 'Black', 6, 1)
            if play_button_clicked:
                LevelSelector.show(self)
            if ranking_button_clicked:
                Ranking.show(self)
            if exit_button_clicked:
                self.running = False
            if mute_button_clicked:
                self.state_music = True
            if unmute_button_clicked:
                self.state_music = False
            
            if self.state_music:
                self.music.stop()
            
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
            draw_text_mid(self.screen, 'Level Selector', title_font, 'Black', 70)
            level1 = button(self.screen, 50, (HEIGHT - 50) // 2, 200, 50, (150,150,150), (100, 100, 100), 'Level 1', lvl_font, 'Black', 6, 1)
            level2 = button(self.screen, 50, ((HEIGHT - 50) // 2) + 60, 200, 50, (150,150,150), (100, 100, 100), 'Level 2', lvl_font, 'Black', 6, 1)
            level3 = button(self.screen, 50, ((HEIGHT - 50) // 2) + 120, 200, 50, (150,150,150), (100, 100, 100), 'Level 3', lvl_font, 'Black', 6, 1)
            back = button(self.screen, 50, ((HEIGHT - 50) // 2) + 180, 200, 50, (150,150,150), (100, 100, 100), 'Back', lvl_font, 'Black', 6, 1)

            if back:
                MainMenu.show(self)
            if level1:
                game.current_level = 0
                game.run()
                self.running = False
            if level2:
                game.current_level = 1
                game.run()
                self.running = False
            if level3:
                game.current_level = 2
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
            draw_text_mid(self.screen, f'Max Score: {self.max_score}', title_font, 'Black', 500)
            back_button = button(self.screen, 0, 550, 200, 50, (150,150,150), (100, 100, 100), 'back', title_font, 'Black', 6, 1)
            if back_button:
                MainMenu.show(self)

            pygame.display.flip()
    
    

game = Game()
# menu = MainMenu()
# menu.show()
