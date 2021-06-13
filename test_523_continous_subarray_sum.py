import unittest

"""
write down thoughts
1. build a dictionary with key = cum_sum_0_to_index % k
2. if we find key is duplicated, it means the subarray in between will add up to a number %k =0
for example,
23 -> (23%6) = 5 -> {5:0}
2 -> (23+2)%6 = 1 -> {1:1}
4 -> (23+2+4)%6 = 5 -> {5:2}, now we found a subarray [2,4] that has a sum 6%6==0

What if there is a 6?
we should check if the index is the one immediate to the left, if so, it's just one n%k==0, it does not count
"""


class Solution(object):
    def checkSubarraySum(self, nums, k: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_map = {}
        mod_map[0] = -1 # need this to count the subarray start from beginning.
        cum_sum = 0
        for i, n in enumerate(nums):
            cum_sum += n
            key = cum_sum % k
            find_idx = mod_map.get(key, -2)
            if find_idx < -1:
                mod_map[key] = i
            else:
                if find_idx < i - 1: # not next to each other
                    return True
                else:
                    continue
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [23, 2, 4, 6, 7]
        k = 6
        self.assertEqual(True, Solution().checkSubarraySum(nums, k))

    def test2(self): #not a subarray with size=1
        nums = [23, 6, 5]
        k = 6
        self.assertEqual(False, Solution().checkSubarraySum(nums, k))

    def test3(self):
        nums = [23, 6, 12]
        k = 6
        self.assertEqual(True, Solution().checkSubarraySum(nums, k))

    def test4(self):
        nums = [2, 4, 7]
        k = 6
        self.assertEqual(True, Solution().checkSubarraySum(nums, k))

    def test5(self):
        nums = [23, 2, 4, 6, 6]
        k = 7
        self.assertEqual(True, Solution().checkSubarraySum(nums, k))


if __name__ == '__main__':
    unittest.main()
