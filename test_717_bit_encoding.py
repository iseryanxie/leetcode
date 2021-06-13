import unittest
import bisect

"""
write down thoughts
from left to right enumerate, if current digit is 1, move 2 position to the right, if 0, move 1 position to the right
check if final position equals the length of array

The given string will always end with a zero, no need to check the last position
"""
from typing import List


# class Solution:
#     def isOneBitCharacter(self, bits: List[int]) -> bool:
#         p = 0
#         while p < len(bits)-1: # The given string will always end with a zero, no need to check the last position
#             if bits[p] == 1:
#                 p += 2
#             else:
#                 p += 1
#         return p == len(bits)-1
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            # 当前位置为0，且已经是最后一个元素，直接返回True
            if bits[i] == 0 and i == len(bits) - 1 :
                return True
            if bits[i] == 1: # 当前位置为1，则说明肯定是2比特的开头
                i += 2
                continue
            i += 1 # 当前位置为0（一比特），则从下一个位置开始计算
        return False # 所有的元素都遍历完还没返回, last number was skipped，说明最后一个字符肯定是2比特**


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(False, Solution().isOneBitCharacter([ 1, 0]))

    def test2(self):
        self.assertEqual(True, Solution().isOneBitCharacter([1, 1, 0]))


if __name__ == '__main__':
    unittest.main()
