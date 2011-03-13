import heapq
import math

class PercentileTracker(object):
    def __init__(self, *percentilesToTrack):
        pass

    def add(self, num):
        pass


    def add_list(self, lst):
        for i in lst:
            self.add(num)

    def get_percentile(self, percentile):
        pass


class SinglePercentileTracker(object):
    def __init__(self, percentile):
        self.percentile_tracked = percentile
        self.lheap = MaxHeap()
        self.rheap = MinHeap()
        self.size = 0
        self.percentile = None

    def add(self, num):
        self.size += 1
        n = (self.percentile_tracked/100.0)*(self.size+1)
        lsize = int(math.floor(n))
        if num > self.percentile:
            self.rheap.push(num)
        else:
            self.lheap.push(num)

        if self.lheap.size() < lsize:
            self.lheap.push(self.rheap.pop())
        ir = int(n)
        fr = n - ir
        low_data = self.lheap.get(0)
        high_data = self.rheap.get(0)
        self.percentile = fr*(high_data - low_data) + low_data

    def add_list(self, lst):
        for l in lst:
            self.add(l)





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
