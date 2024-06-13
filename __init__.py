import pygame

from config import windowWidth, windowHeight


pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Character Game")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()