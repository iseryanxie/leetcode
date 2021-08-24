import unittest

"""
write down thoughts
1. use built in
2. count segments
"""
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


#
# class Solution:
#     def countSegments(self, s: str) -> int:
#         cnt = 0
#         for i in range(len(s)):
#             if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
#                 cnt += 1
#         return cnt


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().countSegments("love live! mu'sic forever"))

    def test2(self):
        self.assertEqual(0, Solution().countSegments(" "))


if __name__ == '__main__':
    unittest.main()
