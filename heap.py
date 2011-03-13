import heapq
class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap,-num)

    def pop(self):
        return -heapq.heappop(self.heap)

    def get(self, num):
        if num >= len(self.heap):
            return 0
        return -self.heap[num]

    def size(self):
        return len(self.heap)
        
# Just for consistency
class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap,num)

    def pop(self):
        return heapq.heappop(self.heap)

    def get(self, num):
        if num >= len(self.heap):
            return 0
        return self.heap[num]

    def size(self):
        return len(self.heap)
