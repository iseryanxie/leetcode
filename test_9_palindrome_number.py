import unittest

"""
write down thoughts
method 1. convert to string, check palindrome
method 2. get digit one by one to form a list, 
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x<0:
#             return False
#         ln = []
#         while x>0:
#             ln.append(x%10)
#             x = x//10
#
#         if ln == ln[::-1]:
#             return True
#         else:
#             return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isPalindrome(121))

    def test2(self):
        self.assertEqual(False, Solution().isPalindrome(10))

    def test3(self):
        self.assertEqual(False, Solution().isPalindrome(-101))


if __name__ == '__main__':
    unittest.main()
