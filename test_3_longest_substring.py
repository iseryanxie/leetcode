import unittest
import bisect

"""
write down thoughts
1. for all letters
2. maintain a hashmap with letter as key, location as value, 
3. maintain the start position of the substring
4. when repeat letter is found, substring start position will move to the right of the first  repeat letter
5. and the hashmap will update the location of the repeat letter.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        repeat_dict = {}
        max_len = 0
        substr_start = 0
        for i, c in enumerate(s):
            if c in repeat_dict and repeat_dict[c] >= substr_start:
                substr_start = repeat_dict[c] + 1  # move substr start position to the repeat letter+1
            max_len = max(i - substr_start + 1, max_len)
            repeat_dict[c] = i
        return max_len


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))

    def test2(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("bbbbbbb"))

    def test3(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))

    def test4(self):
        self.assertEqual(0, Solution().lengthOfLongestSubstring(""))

    def test5(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring(" "))

    def test6(self):
        self.assertEqual(2, Solution().lengthOfLongestSubstring("ccd"))


if __name__ == '__main__':
    unittest.main()
