import unittest

"""
write down thoughts
1. take a product of all elements in the array, other than 0
2. record how many 0s in the array, if more than 2, always return 0
3. return product_all/self, except 0
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        n_zeros = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                n_zeros += 1
        if n_zeros > 1:
            return [0 for n in nums]
        ans = []
        for n in nums:
            if n != 0:
                if n_zeros > 0:
                    ans.append(0)
                else:
                    ans.append(int(product / n))
            else:
                ans.append(product)
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(Solution().productExceptSelf(nums), [24, 12, 8, 6])

    def test2(self):
        nums = [-1, 1, 0, -3, 3]
        self.assertEqual(Solution().productExceptSelf(nums), [0, 0, 9, 0, 0])

    def test3(self):
        nums = [-1, 1, 0, -3, 0]
        self.assertEqual(Solution().productExceptSelf(nums), [0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
