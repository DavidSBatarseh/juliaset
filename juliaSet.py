import pygame, numpy, sys, numpy;
#import time
from juliaFunction import juliaSet
pygame.init()
size = width, height = 400, 400
black = 0,0,0
maxiterations = 30

screen = pygame.display.set_mode(size)
canvas = pygame.display.get_surface()
tempCanvas = pygame.Surface((width,height/2))
screen.fill(black)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
                """ start = time.process_time()
                test = juliaSet(mousePos[0], mousePos[1], width, height)
                print(time.process_time() - start)
                start = time.process_time()
                test = juliaset(mousePos[0], mousePos[1], width, height)
                print(time.process_time() - start) """
                pixelArray = juliaSet(mousePos[0],mousePos[1], width, height/2, maxiterations)

                for x in range(width):
                    for y in range(int(height/2)):
                        if(pixelArray[x + y * height] == maxiterations):
                            tempCanvas.set_at((x,y), black)
                        else:
                            tempCanvas.set_at((x,y), (pixelArray[x + y * height] * 250/maxiterations, 20, 20))
                #secondTemp = pygame.transform.flip(tempCanvas.copy(), True, False)
                canvas.blits([(tempCanvas,(0,height/2)),(pygame.transform.flip(tempCanvas,True,True), (0,0))])
                #canvas.blit(secondTemp, (0,height/2))
        pygame.display.flip()