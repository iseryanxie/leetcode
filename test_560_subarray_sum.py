import unittest

"""
write down thoughts
1. calculate cumulative sum
2. keep track of cumulative sum as key and frequency as value in a hashmap []
3. handle when the numbers in between cum sum to 0, hashmap[cum_sum]+=1
4. for all num in nums, sum frequency when cum_sum-k is found in hashmap, means sum of series between that number and current number is k
"""


class Solution:
    def subarraySum(self, nums, k):
        hashmap = {}  # index:frequency

        # start the hashmap with 0 size or we already have a hashmap of size 0, 1time or we already have subarraySum of size 0 , 1time
        hashmap[0] = 1
        sum_ = 0
        result = 0
        for i in range(len(nums)):
            num = nums[i]
            sum_ += num  # calculate the cummulative sum

            # if the subarray is found
            if (sum_ - k) in hashmap:
                result += hashmap[sum_ - k]

            # if no subarray is found so keep on updating the hashmap with the frequency
            if sum_ in hashmap: # only to handle when num[i]==0, so increment freq
                hashmap[sum_] = hashmap[sum_] + 1  # we already have val in hashmap so update the frequency
            else:
                hashmap[sum_] = 1  # first time we are seeing the value.
        return result


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [6,-6, 1, 2, 3]
        k = 3
        self.assertEqual(3, Solution().subarraySum(nums, k))

    def test2(self):
        nums = [2, 1, -2, 3]
        k = 3
        self.assertEqual(2, Solution().subarraySum(nums, k))


if __name__ == '__main__':
    unittest.main()
