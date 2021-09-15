import unittest

"""
write down thoughts
1. Use generator and memoization
2. Use functools provided cache
"""
from typing import List


class Solution:
    def fib(self, n: int) -> int:
        return [_ for _ in self.fibonacci_gen(n, {})][-1]

    def fibonacci_gen(self, n, cache):
        if n in cache:
            yield cache[n]
        if n == 0:
            yield 0
        else:
            a = 1
            b = 1
            yield a
            yield b
            while n > 2:
                a, b = b, a + b
                cache[n] = b
                yield b
                n -= 1


# import functools
# class Solution:
#     @functools.lru_cache(maxsize=30, typed=False)
#     def fib(self, n: int) -> int:
#         if n ==0:
#             return 0
#         if n == 1:
#             return 1
#         return self.fib(n-1)+self.fib(n-2)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().fib(3))

    def test2(self):
        self.assertEqual(0, Solution().fib(0))

    def test3(self):
        self.assertEqual(1, Solution().fib(1))


if __name__ == '__main__':
    unittest.main()
