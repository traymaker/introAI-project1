import pygame as pg
import time, timeit
from aStarNew import *

from util import *


def initMap():
    n = input('Enter a map number from 0 to 49: \n')

    while ((int(n) > 49) or (int(n) < 0)):
        n = input('Invalid Choice! Enter a map number 0 to 49: \n')

    fp = 'Maps/' + 'map' + str(n) + '.txt'
    fs = open(fp, 'r')

    lines = fs.readlines()
    tempArray = []
    tempCell = None

    for line in lines:
        line = line.strip().split(',')
        line = list(map(int, line))
        tempArray.append(line)

    return tempArray


def drawMap():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            color = BLUE

            if grid[i][j] == 0:
                color = WHITE
            elif grid[i][j] == 1:
                color = BLACK
            elif grid[i][j] == 2:
                color = RED
            elif grid[i][j] == 3:
                color = GREEN

            pg.draw.rect(screen, color,
                         [(PAD + SIZE) * j + PAD, (PAD + SIZE) * i + PAD, SIZE, SIZE])

    pg.display.flip()


def clearMap():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (grid[i][j] == 0):
                color = WHITE
            elif (grid[i][j] == 2):
                color = RED
            elif (grid[i][j] == 3):
                color = GREEN

            pg.draw.rect(screen, color,
                         [(PAD + SIZE) * j + PAD, (PAD + SIZE) * i + PAD, SIZE, SIZE])
            pg.display.flip()

    print('Path Cleared')


pg.init()
screen = pg.display.set_mode((((HEIGHT * 8) + 1), ((WIDTH * 8) + 1)))
pg.display.set_caption("DisplayStar")
clock = pg.time.Clock()
done = False
pg.display.flip()

distance = 0
start = 0.0
stop = 0.0
runTime = 0.0

start_state = (0, 0)
goal_state = (100, 100)
grid = []

tieBreak = 0

while not done:
    for event in pg.event.get():
        if (event.type == pg.QUIT):  # Exit button quits program
            done = True
        elif event.type == pg.KEYDOWN:
            if (event.key == pg.K_l):  # l key press Loads/initializes a new map
                grid = initMap()
                drawMap()
            elif (event.key == pg.K_c):  # c key press Clears screen of previous A* Star Path
                clearMap()
            elif (event.key == pg.K_1):  # Forward A* with Low G-Value Tie-Break
                tieBreak = 0
                start = timeit.default_timer()
                aStar = AStarNew(screen, grid, start_state, goal_state)
                g = aStar.plotPath(tieBreak)
                stop = timeit.default_timer()

                pg.display.flip()

                runTime = stop - start
                print(runTime)
            elif event.key == pg.K_2:  # Forward A* with High G-Value Tie-Break
                tieBreak = 1
                start = timeit.default_timer()
                aStar = AStarNew(screen, grid, start_state, goal_state)
                g = aStar.plotPath(tieBreak)
                stop = timeit.default_timer()

                pg.display.flip()

                runTime = stop - start
                print(runTime)
            elif event.key == pg.K_3:  # Backward A* with Low G-Value Tie-Break
                tieBreak = 0
                start = timeit.default_timer()
                aStar = AStarNew(screen, grid, goal_state, start_state)
                g = aStar.plotPath(tieBreak)
                stop = timeit.default_timer()

                pg.display.flip()

                runTime = stop - start
                print(runTime)
            elif event.key == pg.K_4:  # Backward A* with High G-Value Tie-Break
                tieBreak = 1
                start = timeit.default_timer()
                aStar = AStarNew(screen, grid, goal_state, start_state)
                g = aStar.plotPath(tieBreak)
                stop = timeit.default_timer()

                pg.display.flip()

                runTime = stop - start
                print(runTime)

            elif event.key == pg.K_5:  # Adaptive A* with Low G-Value Tie-Break
                tieBreak = 2
                start = timeit.default_timer()
                aStar = AStarNew(screen, grid, start_state, goal_state)
                g = aStar.plotPath(tieBreak)
                stop = timeit.default_timer()

                pg.display.flip()

                runTime = stop - start
                print(runTime)

    pg.display.flip()

pg.quit()
