import unittest

"""
write down thoughts
1. for each start time (except the last one), add the minimum of (timeSeries[i+1]-timeSeries[i], duration)
This way, it adds either the duration (if it is smaller than the interval between attacks), or add it to 
the next point of attack. 
2. In the last point of attack, add the duration, because it has accounted for all duration BEFORE the last 
point of attack.
"""
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries)-1):
            total += min(timeSeries[i+1]-timeSeries[i],duration)
        return total + duration


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().findPoisonedDuration([1,4], 2))


if __name__ == '__main__':
    unittest.main()
