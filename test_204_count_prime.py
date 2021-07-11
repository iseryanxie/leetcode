import unittest

"""
write down thoughts
sieve: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        prime = {i: 1 for i in range(2, n)}
        for i in range(2, math.ceil(math.sqrt(n))):
            if not prime[i]:
                continue
            else:
                for j in range(i * i, n, i):
                    prime[j] = 0
        return sum(prime.values())


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().countPrimes(10))

    def test2(self):
        self.assertEqual(0, Solution().countPrimes(0))

    def test3(self):
        self.assertEqual(0, Solution().countPrimes(1))


if __name__ == '__main__':
    unittest.main()
