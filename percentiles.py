import math
from heap import MinHeap, MaxHeap


class PercentileTracker(object):
    ''' A class to track multiple percentages'''
    def __init__(self, *percentilesToTrack):
        self.percentiles = {}
        for p in percentilesToTrack:
            self.percentiles[p] = SinglePercentileTracker(p)

    def add(self, num):
        for p in self.percentiles.itervalues():
            p.add(num)

    def add_list(self, lst):
        for i in lst:
            self.add(i)

    def get_percentile(self, percentile):
        p = self.percentiles.get(percentile, None)
        if p:
            return p.percentile
        else:
            raise PercentileNotTrackedError(percentile)


class SinglePercentileTracker(object):
    ''' A class that tracks a single percentile'''
    def __init__(self, percentile):
        self.percentile_tracked = percentile
        self.lheap = MaxHeap()
        self.rheap = MinHeap()
        self.size = 0
        self.percentile = None

    def add(self, num):
        self.size += 1
        n = (self.percentile_tracked / 100.0) * (self.size + 1)
        lsize = int(math.floor(n))
        if num > self.percentile:
            self.rheap.push(num)
        else:
            self.lheap.push(num)
        if self.lheap.size() < lsize:
            self.lheap.push(self.rheap.pop())
        elif self.lheap.size() > lsize:
            self.rheap.push(self.lheap.pop())
        ir = int(n)
        fr = n - ir
        low_data = self.lheap.get(0)
        high_data = self.rheap.get(0)
        self.percentile = fr * (high_data - low_data) + low_data

    def add_list(self, lst):
        for l in lst:
            self.add(l)


class PercentileNotTrackedError(Exception):
    def __init__(self, percentile):
        self.percentile = percentile

    def __str__(self):
        return str(self.percentile)
