import pygame, sys
from BST import *

w, h = 1000, 625
header = 100
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
framerate = 30

bst = BST([])
input_font = pygame.font.SysFont('Monaco', 30)
error_mode = False
A = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            error_mode = False

            if event.key == pygame.K_RETURN:
                array = A
                array.strip()
                try:
                    array = [int(i) for i in array.split(sep=',')]
                    bst = BST(array)
                except ValueError:
                    error_mode = True
            elif event.key == pygame.K_BACKSPACE:
                A = A[:-1]
            else:
                A += event.unicode

    screen.fill(pygame.Color('black'))
    input_surface = input_font.render("A = [" + A + "]" if not error_mode else "Invalid Input", True, pygame.Color('red'))
    screen.blit(input_surface, input_surface.get_rect(center=(w / 2, header / 2)))
    bst.visualize(screen, header)
    pygame.display.update()

    clock.tick(framerate)
