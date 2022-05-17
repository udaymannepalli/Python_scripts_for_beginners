import pygame
from pygame.locals import *
size = width, height = (800,800)
road_w = int(width/1.6)
pygame.init()
running = True
screen = pygame.display.set_mode((size))

pygame.display.set_caption("Bunny's car game")
screen.fill((60,220,0))
pygame.draw.rect( 
    screen,
    (50,50,50),
    (width/2 - road_w/2, 0,road_w, height)
)
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
pygame.quit()