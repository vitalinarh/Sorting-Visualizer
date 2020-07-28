import pygame
import copy
import random
import sys

WINDOW_HEIGHT = 600
WINDOW_WIDTH  = 900

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 200)

def setup(n):

    values = [0 for i in range(n)]

    for i in range(len(values)):
        values[i] = random.randint(0, WINDOW_HEIGHT)

    return values

def swap(values, i, j):

    temp = values[i]
    values[i] = values[j]
    values[j] = temp

    return values

if __name__=="__main__":

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bubble Sort Visualizer')
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    n = 500

    values = setup(n)

    for i in range(n):

        for j in range(n - 1):
            CLOCK.tick(1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            temp = values[j]
            temp2 = values[j + 1]

            if temp > temp2:
                values = swap(values, j, j + 1)

                SCREEN.fill(BLACK)

                for i in range(len(values)):
                    start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
                    end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
                    pygame.draw.line(SCREEN, WHITE, start, end, 1)


            pygame.display.update()
