class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quicksort(nums, start, pivot - 1)
            self.quicksort(nums, pivot + 1, end)
        else:
            return

    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i] # swap current spot to the left, if current spot value is less than pivot
                i += 1
        nums[i], nums[end] = nums[end], nums[i] # swap the last to the middle
        return i


# class Solution:
#     def sortArray(self, nums):
#         self.quicksort(nums, 0, len(nums) - 1)
#         return nums
#
#     def quicksort(self, nums, lower, upper):
#         if lower < upper:
#             pivot = self.partition(nums, lower, upper)
#             self.quicksort(nums, lower, pivot - 1)
#             self.quicksort(nums, pivot + 1, upper)
#         else:
#             return
#
#     def partition(self, nums, lower, upper):
#
#         pivot = nums[upper]
#
#         i = lower
#
#         for j in range(lower, upper):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#
#         nums[i], nums[upper] = nums[upper], nums[i]
#
#         return i

if __name__ == '__main__':
    nums = [5, 3, 3, 2, 5, 6, 1, 8, 7, 10]
    ans = Solution().sortArray(nums)
    print(ans)
