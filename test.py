from percentiles import SinglePercentileTracker, PercentileTracker
import unittest

class PercentilesTest(unittest.TestCase):

    def testSinglePercentileTracker(self):
        p = SinglePercentileTracker(25)
        p.add_list([3, 5, 7, 8, 9, 11, 13, 15])
        self.assertEquals(5.5, p.percentile)

    def testSinglePercentileMedian(self):
        p = SinglePercentileTracker(50)
        p.add_list([5,3, 6])
        self.assertEquals(5, p.percentile)
        p.add_list([1, 5])
        self.assertEquals(5, p.percentile)
        p.add(2)
        self.assertEquals(4, p.percentile)

    def testPercentileTracker(self):
        p = PercentileTracker(25, 85)
        lst = [4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10]
        p.add_list(lst)
        self.assertEquals(5, p.get_percentile(25))
        self.failUnlessAlmostEqual(9.85, p.get_percentile(85))

if __name__ == "__main__":
    unittest.main()
