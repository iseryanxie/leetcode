import unittest

"""
write down thoughts
1. Recursion
Space: O(n), Time: O(n)
2. DP
Space: O(n)->O(2), Time: O(n)
dp[i] = 0 if s[i] is NOT valid (s[i]=='0') or s[i-1:i+1] is NOT valid
dp[i] = dp[i-2]+dp[i-1], if s[i]!='0' and s[i-1:i+1] is valid between "10" and "26"
dp[i] = dp[i-1] if s[i-1]!='0'
dp[i] = dp[i-2] if s[i-2] between "10" and "26"

bottom up, for i from 0 to len(s), find dp(i), since dp(i) only depends on dp(i-1) and dp(i-2), can use temp variable
to save space complexity to O(3)
"""


#
# class Solution:
#     """Recursion 1"""
#     def count_ways(self, s: str, left: int, right: int):
#         if left in self.count_map:
#             return self.count_map[left]
#
#         if s[left] == '0':
#             return 0
#
#         if left >= right:
#             return 1
#         # count ways when a single char is used to decode
#         cnt = self.count_ways(s, left + 1, right)
#         # count ways when two chars are used to decode, remove invalid cases
#
#         decode = int(s[left:left + 2])
#         if decode <= 26:
#             if left + 2 >= len(s):
#                 # if left+2 reached the end, add 1 more way for "" left. otherwise, index out of range in count_ways
#                 cnt += 1
#             else:
#                 cnt += self.count_ways(s, left + 2, right)
#             # update count map
#         self.count_map[left] = cnt  # use left as index key to represent the string to the right of the key
#         return cnt
#
#     def numDecodings(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         self.count_map = {}
#         return self.count_ways(s, 0, len(s) - 1)
#

class Solution:
    def numDecodings(self, s: str) -> int:
        """DP 2: bottom up"""
        dp = {}
        dp[-1] = 1
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0' and not(10 <= int(s[i - 1:i + 1]) <= 26):
                return 0 # not valid for all
            elif s[i] != '0' and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i] != '0':
                dp[i] = dp[i - 1]
            elif 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i - 2]
        return dp[len(s) - 1]



class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().numDecodings("226"))

    def test2(self):
        self.assertEqual(2, Solution().numDecodings("12"))

    def test3(self):
        self.assertEqual(0, Solution().numDecodings("0"))
    def test4(self):
        self.assertEqual(1, Solution().numDecodings("10"))



if __name__ == '__main__':
    unittest.main()
