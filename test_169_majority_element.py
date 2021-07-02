import unittest

"""
write down thoughts
approach 1: sort then return the element in the middle
time: o(nlogn), space: o(1)
approach 2: hashmap
time: o(n), space: o(n)
approach 3: randomization, keep choosing random number in nums and verify if it is majority number. large prob that it is.
time: o(inf), space: o(1), practically very fast
approach 4: boyer-moore voting
choose 1st element as candidate, count ++ if new number matches candidate, count -- if not, when count is reset to 0, 
use the current number as candidate. It works because any non-majority number will cancel out with other non-majority 
number or the majority number. Majority number will not be canceled out because it has >n/2 occurances.
time: o(n), space: o(1)
approach 5: partial sort, pivot on the mid location of the nums to make left half elements are smaller than the pivot,
right half larger than the mid number. Find the k_th_element of the number array, k is n//2
https://medium.com/analytics-vidhya/how-to-find-k-th-smallest-largest-element-in-an-unsorted-array-4ab7015d802a
time: o(n) on average, space: o(1)

approach 6: divide and conquer
divide in half, find majority of left and majority of right,
if left==right, then majority found, otherwise, count occurance of left majority and right majority, to determine the 
true majority of the two groups.
Recursively call this function to determine for the whole list.
time: o(nlogn), space: o(nlogn)
"""

from typing import List
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n=len(nums)
        for num in nums:
            num_cnt = count.get(num,0) # after get call, it will avoid the key error
            count[num] = num_cnt + 1
            if count[num] > n / 2:
                return num
            # if num not in count:
            #     count[num] = 1
            #     if count[num] > n/2: # if there is only 1 element
            #         return num
            # else:
            #     count[num] += 1
            #     if count[num] > n/2: # no need to find the max, just return the case count>n/2
            #         return num

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = nums[0]
#         counter = 0
#         for num in nums:
#             if num == candidate:
#                 counter += 1
#             else:
#                 counter -= 1
#             if counter == 0:
#                 counter = 1
#                 candidate = num
#         return candidate

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().majorityElement([2,2,1,1,1,2,2]))
    def test2(self):
        self.assertEqual(3, Solution().majorityElement([3,2,3]))


if __name__ == '__main__':
    unittest.main()
