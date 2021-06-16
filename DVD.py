from os import system
import random
import time

currentX = 0
currentY = 0
up = 0
right = 0
width = 20
height = 10

currentX = random.randint(1, 4)
currentY = random.randint(1, 4)
up = random.randint(0, 1)
right = random.randint(0, 1)

while(1):
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ")

    for y in range(0, height):
        print('■', end = "   ")

        for x in range(0, width):
            if y == currentY and x == currentX:
                print('■', end = "   ")
            else:
                print('•', end = "   ")

        print('■', end = "   ")
        print('\n')
        
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ")

    if up == 1:
        if right == 1:
            currentX += 1
            currentY -= 1
        else:
            currentX -= 1
            currentY -= 1
    else:
        if right == 1:
            currentX += 1
            currentY += 1
        else:
            currentX -= 1
            currentY += 1

    if currentX == width - 1:
        right = 0
    if currentX == 0:
        right = 1
    if currentY == height - 1:
        up = 1
    if currentY == 0:
        up = 0

    time.sleep(0.5)
    system('cls')
    
