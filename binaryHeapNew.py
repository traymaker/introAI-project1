class binaryHeapNew:
    def __init__(self):
        self.heap = []

    def siftUp(self, index1):
        if ((self.heap[index1]) < (self.heap[int((index1 - 1) / 2)])):
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

    def get(self, index):
        try:
            return self.heap[index]
        except:
            return 0

    def get_heap(self):
        return self.heap

    def printAll(self):
        for i in range(len(self.heap)):
            print(self.heap[i])