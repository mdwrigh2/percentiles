import math
from heap import MinHeap, MaxHeap


class PercentileTracker(object):
    ''' A class to track multiple percentages'''
    def __init__(self, *percentilesToTrack):
        # I'm cheating a bit on this. I'm tracking each percentile in it's own
        # list. This causes the whole thing to be O(k * n) memory
        # This could be improved by wrapping each value in a datastructure,
        # and length functions would take into account other heaps in the heap,
        # but the implementation would be significantly more complex
        self.percentiles = {}
        for p in percentilesToTrack:
            self.percentiles[p] = SinglePercentileTracker(p)

    def add(self, num):
        # Time Complexity:
            # O(k) for iteration, where k is the number of percentiles tracked
            # Each addition takes O(log n) time, where n is the number of 
            # values in the lists
            # Therefore this takes O(k * log n) time
        for p in self.percentiles.itervalues():
            p.add(num)

    def add_list(self, lst):
        # This takes O(j * k * log n), where j is len(lst),
        # k is the number of percentiles tracked, and n is the number
        # of items in the lists being tracked
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
        # An addition to a list is O(log n) since look up is O(1)
        # insertions are O(log n), and worst case pop is O(log n)
        # and everything is done a constant number of times. In these
        # cases, n is the size of the larger of the two heaps 
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
        # Add list is O(k * log n) where k is len(lst) and n is
        # the size of the larger of the two heaps
        for l in lst:
            self.add(l)


class PercentileNotTrackedError(Exception):
    ''' An exception to be raised when checking a percentile that
        isn't being tracked '''
    def __init__(self, percentile):
        self.percentile = percentile

    def __str__(self):
        return str(self.percentile)
