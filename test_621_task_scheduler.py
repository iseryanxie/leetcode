import unittest
from collections import defaultdict

"""
write down thoughts
Greedy
1. find the max frequency
2. For example, n=2, [A,A,A,B,B,B,C,C], task can be ordered like A__A__=(max_freq-1)*(n+1) first
3. Then Add A,B that both appeared 3 times, A__A__,AB to the end, += 2(AB to the end)
4. The rest can always be rearranged to inserted in blank space because it will not break rules. 
For example, n=2,[A,A,A,B,B,B,C,C,C,D,D], first ABC,ABC,ABC, then insert D to the cycle ABCD,ABCD,ABC
"""


class Solution(object):
    def leastInterval(self, tasks, n: int) -> int:
        """
        :type tasks: List[int]
        :type n: int
        :rtype: int
        """
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        lst = sorted(counts.values())
        max_freq = lst[-1] # Find max frequency
        counter = 0 # count how many times the max frequency of tasks are tied
        while lst and lst[-1] == max_freq:
            lst.pop()
            counter += 1
        ret = (max_freq - 1) * (n + 1) + counter
        return max(len(tasks), ret)
        # take the max of previous calculation and task length
        # when more tasks with less frequency need to be inserted to previous cycle


class TestSolution(unittest.TestCase):
    def test1(self):
        tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"]
        cool_down_n = 2
        self.assertEqual(11, Solution().leastInterval(tasks, cool_down_n))


if __name__ == '__main__':
    unittest.main()
