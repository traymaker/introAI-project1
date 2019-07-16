import numpy as np
import pygame as pg
import time

from binaryHeapNew import *
from random import *
from util import *


class AStarNew:
    def __init__(self, screen, grid, start_state, goal_state):
        self.screen = screen
        self.grid = grid
        self.start_state = start_state
        self.goal_state = goal_state

        self.neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.reverse_path = []
        self.total_path = []

        self.hScore = {self.start_state: self.getH(self.start_state, self.goal_state)}

    def getH(self, a, b):
        # returns the scalar distance from point A, to point B
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plotPath(self, tiebreak):
        pg.event.get()
        self.close_set = set()

        self.gScore = {self.start_state: 0}
        self.hScore[self.start_state] = self.getH(self.start_state, self.goal_state)
        self.fScore = {self.start_state: self.gScore[self.start_state]+self.hScore[self.start_state]}

        self.open_heap = binaryHeapNew()
        self.open_heap.add((self.fScore[self.start_state], self.start_state))
        temp_path = []
        while self.open_heap:
            try:
                current = self.open_heap.remove()[1]
            except:
                print('Path Not Found')
                return self.total_path
            if current in self.close_set:
                continue
            self.close_set.add(current)
            for i, j in self.neighbors:
                neighbor = current[0] + i, current[1] + j
                if neighbor in self.close_set:
                    continue
                if neighbor == self.goal_state:
                    temp_path.append(current)
                    temp_path.append(neighbor)
                    self.followPath(temp_path, tiebreak)
                    return
                if 0 <= neighbor[0] < 101 and 0 <= neighbor[1] < 101:  # CHANGE THIS TO 100
                    g = self.gScore[current] + self.getH(current, neighbor)
                    self.gScore[neighbor] = g
                    if neighbor in self.hScore:
                        if self.hScore[neighbor] != 1000:
                            self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                    else:
                        self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                    self.fScore[neighbor] = g + self.hScore[neighbor]
                    if self.open_heap.get((self.fScore[neighbor], neighbor)) == 0:
                        if tiebreak == 0:
                            self.open_heap.add((self.fScore[neighbor] * 10000 + self.gScore[neighbor], neighbor))
                        else:
                            self.open_heap.add((self.fScore[neighbor] * 10000 - self.gScore[neighbor], neighbor))
            temp_path.append(current)

    def followPath(self, temp_path, tiebreak):
        for i in temp_path:
            current = i
            if self.grid[current[0]][current[1]] == 1:
                self.start_state = last
                self.hScore[current] = 1000
                if current[0] < 100 and current[1] < 100:  # CHANGE THIS TO REDUCE PLOTTED PATHS FOR FASTER RUNTIME
                    for current in temp_path:
                        if self.grid[current[0]][current[1]] == 0:
                            pg.draw.rect(self.screen, BLUE,
                                         [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                                          SIZE, SIZE])
                            temp_path.append(current)
                        if current == self.goal_state:
                            pg.display.update()
                            break
                    time.sleep(.2)  # TIME PLOTTED PATH SHOWS UP FOR
                    for current in temp_path:
                        if self.total_path.__contains__(current):
                            pg.draw.rect(self.screen, YELLOW,
                                         [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                                          SIZE, SIZE])
                        elif self.grid[current[0]][current[1]] == 0:
                            pg.draw.rect(self.screen, WHITE,
                                         [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                                          SIZE, SIZE])
                            temp_path.append(current)
                        if current == self.goal_state:
                            pg.display.update()
                            break
                self.plotPath(tiebreak)
                return
            elif current == self.goal_state:
                self.total_path.append(current)
                print("complete")
                return
            if current not in self.total_path:
                self.total_path.append(current)
                pg.draw.rect(self.screen, YELLOW,
                             [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                              SIZE, SIZE])
                pg.display.update()
            last = current
