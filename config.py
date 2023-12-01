import pygame

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
WIDTH = 800
HEIGHT = 600

FPS = 60
WIDTH_PLAYER = 50
HEIGHT_PLAYER = 50
GRAVITY = 0.75

font = pygame.font.SysFont('Futura', 30)