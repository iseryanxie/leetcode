import unittest

"""
write down thoughts
1. use deque to append from left, so the concatenation can work without the need to reverse.
2. use divmod function to take mode with 16. can be 
"""


class Solution:
    def toHex(self, num: int) -> str:
        from collections import deque
        num_dict = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
        res = deque()  # use deque to allow append from left
        if not num:
            return '0'
        if num < 0:
            num = 2 ** 32 + num

        while num:
            # num, rem = divmod(num, 16) # equivalent to the following two statement
            rem = num % 16
            num = num // 16
            rem = str(rem)
            if rem in num_dict:
                rem = num_dict[rem]
            res.appendleft(rem)
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual('1a', Solution().toHex(26))


if __name__ == '__main__':
    unittest.main()
