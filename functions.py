import pygame
from pygame.locals import *
from config import *
from import_images import *

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))