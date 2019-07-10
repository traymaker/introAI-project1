class Node:
    def __init__(self, x, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.x = x

class MinHeap:

    def __init__(self):
        self.heap = []

    def add(self, x):
        if len(self.heap) == 0:
            self.heap.append(x)
        else:
            self.heap.append(x)
            if self.heap[len(self.heap)-1].x < self.heap[int((len(self.heap)-1)/2)].x:
                self.siftUp(len(self.heap)-1)

    def siftUp(self, index1):
        if self.heap[index1].x < self.heap[int((index1-1)/2)].x:
            temp = self.heap[index1]
            self.heap[index1] = self.heap[int((index1-1)/2)]
            self.heap[int((index1-1)/2)] = temp
            self.siftUp(int((index1 - 1) / 2))

    def remove(self):
        if len(self.heap) == 0:
            return
        target = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap)-1)
        if len(self.heap) > 1:
            if self.heap[1].x < self.heap[0].x:
                self.siftDown(0)
        return target

    def siftDown(self, index2):
        if len(self.heap) > index2*2+2:
            if self.heap[index2].x > self.heap[index2*2+1].x:
                temp = self.heap[index2]
                if len(self.heap) == index2*2+2:
                    self.heap[index2] = self.heap[index2 * 2 + 1]
                    self.heap[index2 * 2 + 1] = temp
                    self.siftDown(index2 * 2 + 1)
                    return
                if self.heap[index2*2+1].x <= self.heap[index2*2+2].x:
                    self.heap[index2] = self.heap[index2*2+1]
                    self.heap[index2*2+1] = temp
                    self.siftDown(index2*2+1)
                else:
                    self.heap[index2] = self.heap[index2 * 2 + 2]
                    self.heap[index2 * 2 + 2] = temp
                    self.siftDown(index2 * 2 + 2)

    def len(self):
        return len(self.heap)

    def get(self, index):
        return self.heap[index]

    def printAll(self):
        for i in range(len(self.heap)):
            print(self.heap[i])
