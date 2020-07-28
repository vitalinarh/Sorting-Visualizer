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

bubble_sort = True          # 0
selection_sort = False      # 1
insertion_sort = False      # 2
merge_sort = False          # 3
quick_sort = False          # 4
heap_sort = False           # 5

buttons = []

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

# BUBBLE SORT
def bubbleSort(values):

    for i in range(n):

        for j in range(n - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            temp = values[j]
            temp2 = values[j + 1]

            if temp > temp2:
                values = swap(values, j, j + 1)

                SCREEN.fill(BLACK)

                for i in range(n):
                    start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
                    end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
                    pygame.draw.line(SCREEN, WHITE, start, end, 2)



                CLOCK.tick(10000)
                pygame.display.update()

    return

#SELECTION SORT

def drawText(message, x, y, color):

    font = pygame.font.Font('freesansbold.ttf', 14)
    text = font.render(message, True, color, BLACK)

    textRect = text.get_rect()
    textRect.center = (x, y)

    SCREEN.blit(text, textRect)

def display_buttons():
    # button 0
    rect = pygame.Rect(1000, 40, 100, 40)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if bubble_sort:
        drawText('Bubble Sort', 1050, 60, RED)
    else:
        drawText('Bubble Sort', 1050, 60, WHITE)

def check_click_btn(pos):

    global bubble_sort
    x = pos[0]
    y = pos[1]

    # x = 1000 y = 40
    if x >= 1000 and x <= 1100 and y >= 40 and y <= 80:
        print("clicked")
        bubble_sort = not bubble_sort

if __name__=="__main__":

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH + 300, WINDOW_HEIGHT))
    pygame.display.set_caption('Bubble Sort Visualizer')
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    n = 100

    values = setup(n)

    for i in range(n):
        start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
        end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
        pygame.draw.line(SCREEN, WHITE, start, end, 2)

    # bubbleSort(values)

    '''
    for i in range(n):
        start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
        end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
        pygame.draw.line(SCREEN, GREEN, start, end, 2)
        CLOCK.tick(50)
        pygame.display.update()'''

    while True:

        display_buttons()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                check_click_btn(pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
