from random import *

class binaryHeapNew:
    def __init__(self):
        self.heap = []

    def siftUp(self, index1):
        if self.get_item(index1)[0] < self.get_item(int((index1 - 1) / 2))[0]:
            temp = self.heap[index1]
            self.heap[index1] = self.heap[int((index1 - 1) / 2)]
            self.heap[int((index1 - 1) / 2)] = temp
            self.siftUp(int((index1 - 1) / 2))
        if self.get_item(index1)[0] == self.get_item(int((index1 - 1) / 2))[0]:
            if random() >= .5:
                temp = self.heap[index1]
                self.heap[index1] = self.heap[int((index1 - 1) / 2)]
                self.heap[int((index1 - 1) / 2)] = temp
                self.siftUp(int((index1 - 1) / 2))

    def siftDown(self, index2):
        if ((len(self.heap) - 1) >= ((index2 * 2) + 1)):
            if (len(self.heap) - 1 == (index2 * 2) + 1):
                minVal = (index2 * 2) + 1
            elif (self.heap[(index2 * 2) + 1] < self.heap[(index2 * 2) + 2]):
                minVal = (index2 * 2) + 1
            else:
                minVal = (index2 * 2) + 2
            if (self.heap[minVal] < self.heap[index2]):
                temp = self.heap[index2]
                self.heap[index2] = self.heap[minVal]
                self.heap[minVal] = temp
                self.siftDown(minVal)

    def add(self, x):
        if (len(self.heap) == 0):
            self.heap.append(x)
        else:
            self.heap.append(x)
            self.siftUp(len(self.heap) - 1)

    def remove(self):
        if (len(self.heap) == 0):
            return

        target = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self.siftDown(0)

        return target

    def len(self):
        return len(self.heap)

    def get(self, item):
        i = 0
        for x in self.heap:
            if x[1] == item:
                return i
            i = i + 1
        return 0

    def get_item(self, index):
        return self.heap[index]

    def get_heap(self):
        return self.heap

    def set_item(self, index, item):
        self.heap[index] = item
        self.siftUp(index)
        return

    def printAll(self):
        for i in range(len(self.heap)):
            print(self.heap[i])