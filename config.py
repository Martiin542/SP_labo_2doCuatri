import pygame

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
WIDTH = screen_width
HEIGHT = screen_height

FPS = 60
WIDTH_PLAYER = 50
HEIGHT_PLAYER = 50
GRAVITY = 0.75

font = pygame.font.SysFont('Futura', 30)
title_font = pygame.font.Font('assets\\fonts\\04B_30__.TTF', 60)
lvl_font = pygame.font.Font('assets\\fonts\\04B_30__.TTF', 30)