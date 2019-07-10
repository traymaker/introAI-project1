import binaryHeap


class Node:
    def __init__(self, x, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.x = x


class aStar:
    def __init__(self, maze, n):
        self.n=n
        self.start = Node(0, None, None)
        self.start.position = (0, 0)
        self.end = Node(0, None, None)
        self.end.position = (n - 1, n - 1)
        self.heap = binaryHeap.MinHeap()
        self.heap.add(self.start)
        self.board = maze
        self.closedList = [[0]*n]*n
        self.currentPosition = (0, 0)

    def search(self):
        while self.heap.len() != 0:  # while heap is not empty
            currentNode = self.heap.remove()
            self.currentPosition = currentNode.position
            for i in range(-1, 2):  # testing points left/right
                if 0 < i+self.currentPosition[0] < self.n - 1:
                    if self.board[self.currentPosition[0] + i][self.currentPosition[1]] == 3:  # check goal
                        return
                    elif self.board[self.currentPosition[0] + i][self.currentPosition[1]] == 0:
                        if self.closedList[self.currentPosition[0] + i][self.currentPosition[1]] == 0:  # not on closed list
                            for x in range(self.heap.len()-1):
                                if self.heap.get(x).position == (self.currentPosition[0] + i, self.currentPosition[1]):  # not already in heap
                                    continue
                            g = abs(self.currentPosition[0] - 1 - self.start.position[0]) + abs(self.currentPosition[1] - self.start.position[1])
                            h = abs(self.currentPosition[0] - 1 - self.end.position[0]) + abs(self.currentPosition[1] - self.end.position[1])
                            newNode = Node(g + h, currentNode, (self.currentPosition[0] + i, self.currentPosition[1]))
                            self.heap.add(newNode)
                            self.board[self.currentPosition[0] + i][self.currentPosition[1]] = 4
            for j in range(-1, 2):  # testing points above/below
                if 0 < j + self.currentPosition[1] < self.n - 1:
                    if self.board[self.currentPosition[0]][self.currentPosition[1] + j] == 3:
                        return
                    elif self.board[self.currentPosition[0]][self.currentPosition[1] + j] == 0:
                        if self.closedList[self.currentPosition[0]][self.currentPosition[1] + j] == 0:
                            for x in range(self.heap.len()-1):
                                if self.heap.get(x).position == (self.currentPosition[0], self.currentPosition[1] + j):
                                    continue
                            g = abs(self.currentPosition[0] - 1 - self.start.position[0]) + abs(self.currentPosition[1] - self.start.position[1])
                            h = abs(self.currentPosition[0] - 1 - self.end.position[0]) + abs(self.currentPosition[1] - self.end.position[1])
                            newNode = Node(g + h, currentNode, (self.currentPosition[0], self.currentPosition[1] + j))
                            self.heap.add(newNode)
                            self.board[self.currentPosition[0]][self.currentPosition[1] + j] = 4
            self.closedList[self.currentPosition[0]][self.currentPosition[1]] = 1


maze = [[2, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in maze]))
search1 = aStar(maze, 10)
search1.search()
print('\n')
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in search1.board]))


