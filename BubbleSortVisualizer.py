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

# bubble_sort 0
# selection_sort 1
# insertion_sort 2
# count_sort 3
# quick_sort 4
# heap_sort 5

sort_type = [True, False, False, False, False, False]

def setup(n):

    values = [0 for i in range(n)]

    for i in range(len(values)):
        values[i] = random.randint(0, WINDOW_HEIGHT)

    return values

def finish(values):
    for i in range(n):
        start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
        end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
        pygame.draw.line(SCREEN, GREEN, start, end, 2)
        CLOCK.tick(50)
        pygame.display.update()

def reDrawLines(values):

    SCREEN.fill(BLACK)

    for i in range(len(values)):
        start = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT)
        end = (i * (WINDOW_WIDTH / n) + (WINDOW_WIDTH / n), WINDOW_HEIGHT - values[i])
        pygame.draw.line(SCREEN, WHITE, start, end, 2)

    CLOCK.tick(10000)
    pygame.display.update()
    return

def swap(values, i, j):

    temp = values[i]
    values[i] = values[j]
    values[j] = temp

    return values

# BUBBLE SORT ==================================================================================================
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
                reDrawLines(values)
    finish(values)

    return

#SELECTION SORT ====================================================================================================
def selectionSort(values):

    for i in range(len(values)):
        min_index = i

        for j in range(i + 1, len(values)):

            if values[min_index] > values[j]:
                min_index = j

        values = swap(values, i, min_index)
        reDrawLines(values)

    return

# INSERTION SORT ==================================================================================================
def insertionSort(values):
    for i in range(1, len(values)):
        key = values[i]

        j = i - 1
        while j >= 0 and key < values[j]:
            reDrawLines(values)
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

# COCKTAIL SORT ================================================================================================
def cocktailSort(values):

    n = len(values)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True):

        swapped = False

        for i in range (start, end):
            if (values[i] > values[i + 1]) :
                values[i], values[i + 1]= values[i + 1], values[i]
                reDrawLines(values)
                swapped = True

        if (swapped == False):
            break

        swapped = False

        end = end - 1

        for i in range(end-1, start-1, -1):
            if (values[i] > values[i + 1]):
                values[i], values[i + 1] = values[i + 1], values[i]
                reDrawLines(values)
                swapped = True

        start = start + 1

# MERGE SORT ==================================================================================================

def flip(values, i):
    start = 0
    while start < i:
        temp = values[start]
        values[start] = values[i]
        values[i] = temp
        reDrawLines(values)
        start += 1
        i -= 1

def findMax(values, n):
    mi = 0
    for i in range(n):
        if values[i] > values[mi]:
            mi = i
    return mi

def pancakeSort(values):

    curr_size = len(values)

    while curr_size > 1:

        mi = findMax(values, curr_size)

        if mi != curr_size - 1:

            flip(values, mi)
            flip(values, curr_size - 1)

        curr_size -= 1

# MERGE SORT ==================================================================================================
def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            reDrawLines(result)
            i+= 1
        else:
            result.append(right[j])
            reDrawLines(result)
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            reDrawLines(result)
            break

    return result

def mergeSort(values):

    if len(values) < 2:
        return values

    middle = len(values) // 2
    left = mergeSort(values[:middle])
    right = mergeSort(values[middle:])

    return merge(left, right)

def drawText(message, x, y, color):

    font = pygame.font.Font('freesansbold.ttf', 14)
    text = font.render(message, True, color, BLACK)

    textRect = text.get_rect()
    textRect.center = (x, y)

    SCREEN.blit(text, textRect)

button_height = 35
button_width = 150

def display_buttons():
    # button 0 - bubbleSort
    rect = pygame.Rect(970, 40, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if sort_type[0]:
        drawText('Bubble Sort', 1045, 57, RED)
    else:
        drawText('Bubble Sort', 1045, 57, WHITE)

    #button 1 - selectionSort
    rect = pygame.Rect(970, 100, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if sort_type[1]:
        drawText('Selection Sort', 1045, 117, RED)
    else:
        drawText('Selection Sort', 1045, 117, WHITE)

    #button 2 - insertionSort
    rect = pygame.Rect(970, 160, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if sort_type[2]:
        drawText('Insertion Sort', 1045, 177, RED)
    else:
        drawText('Insertion Sort', 1045, 177, WHITE)

    #button 3 - mergeSort
    rect = pygame.Rect(970, 220, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if sort_type[3]:
        drawText('Cocktail Sort', 1045, 237, RED)
    else:
        drawText('Cocktail Sort', 1045, 237, WHITE)

    #button 4 - quickSort
    rect = pygame.Rect(970, 280, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    if sort_type[4]:
        drawText('Pancake Sort', 1045, 297, RED)
    else:
        drawText('Pancake Sort', 1045, 297, WHITE)


    # reset button
    rect = pygame.Rect(970, 480, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    drawText('Reset', 1045, 497, WHITE)

    # start button
    rect = pygame.Rect(970, 530, 150, 35)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    drawText('Start', 1045, 547, WHITE)

def select_type(i):

    for j in range(len(sort_type)):
        sort_type[j] = False

    sort_type[i] = True

def getType(i, values):
    if i == 0:
        bubbleSort(values)
    elif i == 1:
        selectionSort(values)
    elif i == 2:
        insertionSort(values)
    elif i == 3:
        cocktailSort(values)
    elif i == 4:
        pancakeSort(values)

def startAlgorithm(values):
    for i in range(len(sort_type)):
        if sort_type[i] == True:
            getType(i, values)

def check_click_btn(pos, values):

    global bubble_sort
    x = pos[0]
    y = pos[1]

    button_x = 970
    button_x2 = 970 + button_width

    # x = 1000 y = 40
    if button_x >= 970 and button_x2 <= 1120:
        if y >= 40 and y <= 75:
            select_type(0)
        elif y >= 100 and y <= 135:
            select_type(1)
        elif y >= 160 and y <= 195:
            select_type(2)
        elif y >= 220 and y <= 255:
            select_type(3)
        elif y >= 280 and y <= 315:
            select_type(4)

        elif y >= 480 and y <= 515:
            values = setup(len(values))
        elif y >= 530 and y <= 565:
            # start button
            startAlgorithm(values)

    return values

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

    while True:

        display_buttons()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                values = check_click_btn(pos, values)
                reDrawLines(values)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
