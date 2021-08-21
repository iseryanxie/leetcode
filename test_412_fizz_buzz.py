import unittest

"""
write down thoughts
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res



class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["1", "2", "Fizz"], Solution().fizzBuzz(3))
    def test2(self):
        self.assertEqual(["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"], Solution().fizzBuzz(15))


if __name__ == '__main__':
    unittest.main()
