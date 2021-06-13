import unittest

"""
write down thoughts
approach 1:
binary search
approach 2:
newton's method : https://amsi.org.au/ESA_Senior_Years/SeniorTopic3/3j/3j_2content_2.html#:~:text=Newton's%20method%20for%20solving%20equations,requires%20calculus%2C%20in%20particular%20differentiation.
find x for f(x) = x**2-a = 0
iteratively update x_n
x_{n+1} = x_n - f(x_n)/f'(x_n) = (x_n+a/x_n)/2
Newton's method use linear approximation, so the intercept is x-f(x)/f'(x). the best next guess is the intercept with linear assumption
"""

#
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x <= 0:
#             return 0
#         if x <= 1:
#             return 1
#         left = 1
#         right = x // 2 + 1
#         while left < right:
#             mid = (left + right) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid > x:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left - 1
class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x / 2
        while abs(guess * guess - x) > 0.05:
            guess = (guess + x / guess) / 2
        return int(guess)  # int is floor


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().mySqrt(4))

    def test2(self):
        self.assertEqual(2, Solution().mySqrt(8))

    def test3(self):
        self.assertEqual(20, Solution().mySqrt(400))

    def test4(self):
        self.assertEqual(1, Solution().mySqrt(3))


if __name__ == '__main__':
    unittest.main()
