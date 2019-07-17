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
        self.og_start_state = start_state
        self.goal_state = goal_state

        self.neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.reverse_path = []
        self.total_path = []
        self.last_path = []

        self.parent = {self.start_state: None}
        self.hScore = {self.start_state: self.getH(self.start_state, self.goal_state)}

    def getH(self, a, b):
        # returns the scalar distance from point A, to point B
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plotPath(self, tiebreak):
        pg.event.get()
        self.close_set = set()

        self.gScore = {self.start_state: 0}
        self.hScore[self.start_state] = self.getH(self.start_state, self.goal_state)
        self.fScore = {self.start_state: self.gScore[self.start_state]+self.hScore[self.start_state]*10000}

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
                g = self.gScore[current] + self.getH(current, neighbor)
                if neighbor in self.close_set:
                    continue
                if neighbor == self.goal_state:
                    temp_path.append(current)
                    temp_path.append(neighbor)
                    self.parent[neighbor] = current
                    self.followPath(temp_path, tiebreak)
                    return
                if 0 <= neighbor[0] < 101 and 0 <= neighbor[1] < 101:
                    if self.gScore.get(neighbor, 0) == 0:
                        self.gScore[neighbor] = self.getH(neighbor, self.start_state)

                    self.gScore[neighbor] = g
                    if g <= self.gScore.get(neighbor, 0):
                        if not self.total_path.__contains__(neighbor):
                            self.parent[neighbor] = current
                    if neighbor in self.hScore:
                        if self.hScore[neighbor] != 1000:
                            if tiebreak == 2:
                                if self.last_path.__contains__(neighbor):
                                    self.hScore[neighbor] = self.last_path.index(self.goal_state) - self.last_path.index(neighbor) - self.gScore.get(neighbor)
                                else:
                                    self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                            else:
                                self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                    else:
                        if tiebreak == 2:
                            if self.last_path.__contains__(neighbor):
                                self.hScore[neighbor] = self.last_path.index(self.goal_state) - self.last_path.index(neighbor) - self.gScore.get(neighbor)
                            else:
                                self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                        else:
                            self.hScore[neighbor] = self.getH(neighbor, self.goal_state)
                    if tiebreak == 0:
                        self.fScore[neighbor] = 10000 * self.hScore[neighbor] + g
                        heapEntry = (self.fScore[neighbor], neighbor)
                    else:
                        self.fScore[neighbor] = 10000 * self.hScore[neighbor] - g
                        heapEntry = (self.fScore[neighbor], neighbor)
                    self.open_heap.add(heapEntry)
            temp_path.append(current)

    def followPath(self, temp_path, tiebreak):
        for x in temp_path:
            current = x
            if self.grid[current[0]][current[1]] == 1:
                self.start_state = last
                self.hScore[current] = 1000
                if current[0] < 25 and current[1] < 25:  # CHANGE THIS TO REDUCE PLOTTED PATHS FOR FASTER RUNTIME
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
                self.last_path = temp_path
                self.plotPath(tiebreak)
                return
            elif current == self.goal_state:
                tiles = 0
                self.total_path.append(current)
                while current != self.og_start_state:
                    pg.draw.rect(self.screen, RED,
                                 [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                                  SIZE, SIZE])
                    current = self.parent[current]
                    tiles = tiles + 1
                    pg.display.update()
                print(tiles, " tiles traversed.")
                return
            if current not in self.total_path:
                self.total_path.append(current)
                pg.draw.rect(self.screen, YELLOW,
                             [(PAD + SIZE) * current[1] + PAD, (PAD + SIZE) * current[0] + PAD,
                              SIZE, SIZE])
                pg.display.update()
            last = current
