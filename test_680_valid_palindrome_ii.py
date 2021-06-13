import unittest

"""
write down thoughts
1. check from start and end pointer one by one
2. if equal, keep going till two pointers meet
3. if not equal, check if remove left or right makes the string in between a palindrome
"""


class Solution(object):
    def palindrome_check(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if self.palindrome_check(s):
            return True
        else:
            left, right = 0, len(s) - 1
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    # remove left to select between left+1 to right+1(not inclusive)
                    # remove right to select between left(inclusive) to right(not inclusive)
                    # check anything in between, because outside is already verified
                    if self.palindrome_check(s[left+1:right+1]) or self.palindrome_check(s[left:right]):
                        return True
                    else:
                        return False

        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().validPalindrome("aba"))

    def test2(self):
        self.assertEqual(True, Solution().validPalindrome("abca"))

    def test3(self):
        self.assertEqual(False, Solution().validPalindrome("abc"))


if __name__ == '__main__':
    unittest.main()
