import unittest

"""
write down thoughts
1. two pointers
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1
        res = list(s)  # [s[i] for i in range(len(s))]
        while left < right:
            if s[left] not in vowels:
                res[left] = s[left]
                left += 1
            elif s[right] not in vowels:
                res[right] = s[right]
                right -= 1
            else:
                res[left] = s[right]
                res[right] = s[left]
                left += 1
                right -= 1
        return "".join(res)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("holle", Solution().reverseVowels("hello"))

    def test2(self):
        self.assertEqual("Aa", Solution().reverseVowels("aA"))


if __name__ == '__main__':
    unittest.main()
