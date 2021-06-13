import unittest
import bisect

"""
problem: given a list of born year and death year, find the year with max population
write down thoughts
1. sort birth list, sort death list
2. set two pointers, each in each list
3. move left or right pointer depending on which has a smaller key, +1 or -1 the population, find max
"""
from typing import List


class Solution(object):
    def find_max_population(self, birth_yrs: List[int], death_yrs: List[int]) -> int:
        """
        :type birth_yrs: List[int]
        :type death_yrs: List[int]
        :rtype: int
        """
        max, pop = 0, 0
        left, right = 0, 0
        birth_yrs.sort()
        death_yrs.sort()
        while left < len(birth_yrs) and right < len(death_yrs):
            if birth_yrs[left] < death_yrs[right]:
                pop += 1
                if pop > max:
                    max = pop
                left += 1
                continue
            elif birth_yrs[left] > death_yrs[right]:
                pop -= 1
                right += 1
                continue
            else:
                left += 1
                right += 1

        if left < len(birth_yrs) - 1:
            pop += len(birth_yrs) - 1 - left
        if pop > max:
            max = pop
        return max


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().find_max_population([1942, 1980, 1935, 1997, 1836, 1903],
                                                           [1998, 2000, 2012, 2049, 1923, 1942]))


if __name__ == '__main__':
    unittest.main()
