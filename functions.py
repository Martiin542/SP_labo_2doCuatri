import pygame
from pygame.locals import *
from config import *
from import_images import *

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_text_mid(screen, text, font, text_col, y):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect()
    x = (screen.get_width() - img_rect.width) // 2
    screen.blit(img, (x, y))


def button(screen, x, y, width, height, default_color, hover_color, text, font, font_color, border_radius, scale=1.0):
    default_rect = pygame.Rect(x, y, width, height)
    hover_rect = pygame.Rect(x, y, width, height)
    default_rect.width = int(default_rect.width * scale)
    default_rect.height = int(default_rect.height * scale)
    hover_rect.width = int(hover_rect.width * scale)
    hover_rect.height = int(hover_rect.height * scale)

    mouse_pos = pygame.mouse.get_pos()
    clicked = False

    if hover_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, hover_rect, border_radius=border_radius)
        if pygame.mouse.get_pressed()[0] == 1 and not clicked:
            clicked = True
    else:
        pygame.draw.rect(screen, default_color, default_rect, border_radius=border_radius)
        clicked = False

    # Renderizar el texto en el centro del botón
    text_surface = font.render(text, True, font_color)
    text_rect = text_surface.get_rect(center=default_rect.center)
    screen.blit(text_surface, text_rect)

    return clicked


def label_mid(screen, image, y, scale):
    image = image
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    rect = image.get_rect()
    x = (WIDTH - rect.width) // 2
    rect.topleft = (x, y)

    screen.blit(image, (rect.x, rect.y))

    
