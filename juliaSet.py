import pygame, numpy, sys;
import time
from juliaFunction import juliaSet
pygame.init()
size = width, height = 400, 400
black = 0,0,0

screen = pygame.display.set_mode(size)
canvas = pygame.display.get_surface()
screen.fill(black)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
                cringebrain = pygame.mouse.get_pos()
                """ start = time.process_time()
                test = juliaSet(cringebrain[0], cringebrain[1], width, height)
                print(time.process_time() - start)
                start = time.process_time()
                test = juliaset(cringebrain[0], cringebrain[1], width, height)
                print(time.process_time() - start) """
                test = juliaSet(cringebrain[0], cringebrain[1], width, height)

                for x in range(width):
                    for y in range(height):
                        if(test[y + x * width] == 10):
                            canvas.set_at((x,y), black)
                        else:
                            canvas.set_at((x,y), (test[y + x * width] * 20, 0, 255))
        pygame.display.flip()
