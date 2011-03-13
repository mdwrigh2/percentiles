import percentiles
import unittest

class PercentilesTest(unittest.TestCase):

    def testSinglePercentileTracker(self):
        p = SinglePercentileTracker(25)
        p.add_list([3, 5, 7, 8, 9, 11, 13, 15])
        self.assertEquals(5.5, p.percentile)
