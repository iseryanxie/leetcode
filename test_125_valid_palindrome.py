import unittest

"""
write down thoughts
1. lower and remove spaces to the original string and store in tmp
2. check if tmp==tmp[::-1] to validate palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for char in s.lower():
            if char.isalpha() or char.isdigit():
                tmp += char
        return tmp == tmp[::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        test_str = "A man, a plan, a canal: Panama"
        self.assertEqual(True, Solution().isPalindrome(test_str))

    def test2(self):
        test_str = "race a car"
        self.assertEqual(False, Solution().isPalindrome(test_str))


if __name__ == '__main__':
    unittest.main()
