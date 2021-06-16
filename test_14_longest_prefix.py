import unittest

"""
write down thoughts
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len_prefix = min([len(str) for str in strs])
        for curr in range(0, max_len_prefix):
            c = strs[0][curr]
            for str in strs:
                if c != str[curr]:
                    if curr > 0:
                        return str[:curr]
                    else:
                        return ""
        return strs[0][:max_len_prefix]
# improvement idea, no need to find the shortest string
# def longestCommonPrefix(self, strs):
#     s = ""
#     for x in range(len(strs[0])):
#         for i in range(1, len(strs)):
#             if x >= len(strs[i]) or strs[i][x] != strs[0][x]:
#                 return s
#         s += strs[0][x]
#
#     return s

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("fl", Solution().longestCommonPrefix(["flower", "flow", "flight"]))

    def test2(self):
        self.assertEqual("", Solution().longestCommonPrefix(["", "flow", "flight"]))

    def test3(self):
        self.assertEqual("", Solution().longestCommonPrefix(["a", "flow", "flight"]))

    def test4(self):
        self.assertEqual("flow", Solution().longestCommonPrefix(["flower", "flow", "flowers"]))


if __name__ == '__main__':
    unittest.main()
