import unittest
import bisect

"""
write down thoughts
"""
from typing import List


# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         res = []
#
#         def dfs(op, k):
#             if k == n:
#                 res.append(op)
#                 return
#             for i in range(k, n):
#                 temp = s[k:i + 1]
#                 if temp == temp[::-1]:
#                     dfs(op + [temp], i + 1)
#
#         dfs([], 0)
#         return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)

        def dfs(k):
            """substring start from k position"""
            if k == n:
                res.append(part.copy())
                return
            for i in range(k, n):
                tmp = s[k:i + 1] # substring is from k to i (inclusive)
                if tmp == tmp[::-1]:
                    part.append(tmp)
                    dfs(i + 1)
                    part.pop() # remove previously added substring

        dfs(0)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([["a", "a", "b"], ["aa", "b"]], Solution().partition("aab"))


if __name__ == '__main__':
    unittest.main()
