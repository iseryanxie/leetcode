import unittest
import bisect

"""
write down thoughts
1. naive method
search_pointer, left, right pointers
left++, right++ if matched char
search_pointer++, if no matched char, left=search_pointer, right=0
match found if right=len(needle)

2. KMP algorithm
when moving the search pointer, instead of always +1, we can find the matched substring and compare its head and tail,
for example, a matched substring looks like this
"abcd wjoeign abcd", in this case, we can move search pointer to the second "abcd" and let left=4, right=4, continue
the match after "abcd".
"""


# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if not needle:
#             return 0
#         for i, char in enumerate(haystack):
#             if char == needle[0]:
#                 if haystack[i:i + len(needle)] == needle:
#                     return i
#
#         return -1
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if not needle:
#             return 0
#         if needle in haystack:
#             return haystack.index(needle)
#         return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        search_p, left, right = 0, 0, 0
        while search_p + left < len(haystack) and right < len(needle):
            if haystack[search_p + left] == needle[right]:
                left += 1
                right += 1
            else:
                search_p += 1
                left = 0
                right = 0
        if right == len(needle):
            return search_p
        else:
            return -1


# class Solution:
#     def strStr(self, haystack, needle):
#         if len(needle) == 0: return 0
#
#         n, m = len(haystack), len(needle)
#         next = [0] * m
#         self.GetNext(needle, next)  # next array initialization
#
#         i, j = 0, 0
#         while i < n and j < m:
#             if j == -1 or haystack[i] == needle[j]:
#                 i, j = i + 1, j + 1
#             else:
#                 j = next[j]
#
#         return i - m if j >= m else -1
#
#     def GetNext(self, t, next):  # improved version next calculation array
#         j, k, next[0], n = 0, -1, -1, len(next)
#         while j < n - 1:
#             if k == -1 or t[j] == t[k]:
#                 j, k = j + 1, k + 1
#                 if t[j] != t[k]:
#                     next[j] = k
#                 else:
#                     next[j] = next[k]
#             else:
#                 k = next[k]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().strStr("hello", "ll"))
    def test2(self):
        self.assertEqual(-1, Solution().strStr("aaaaa", "bba"))
    def test3(self):
        self.assertEqual(-1, Solution().strStr("aaa", "aaaa"))



if __name__ == '__main__':
    unittest.main()
