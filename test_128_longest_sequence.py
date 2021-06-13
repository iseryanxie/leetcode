import unittest


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        streak_len = dict()
        res = 0
        for n in nums:
            if n not in streak_len: # n is new
                left = streak_len.get(n - 1, 0) # search number next to n
                right = streak_len.get(n + 1, 0)
                length = 1 + left + right # length of consecutive sequence=length(left sequence)+self+length(right sequence)
                res = max(length, res) # find max
                for i in [n - left,n, n + right]:  #update length only to the start and end of the new sequence
                    # number in the middle of the sequence is not useful, because every time only search the +-1 location
                    # of the number that is new to the dict. New number is connecting sequences.
                    streak_len[i] = length
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().longestConsecutive(4, [100, 4, 200, 1, 3, 2]))

    def test2(self):
        self.assertEqual(Solution().longestConsecutive(9, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == '__main__':
    unittest.main()
