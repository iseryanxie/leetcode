import unittest

"""
write down thoughts
First try
1. find set of possible values by checking intersection of each roll
2. if no intersection found, return -1 
3. for each element in intersection set, for A and B, count the occurrences of the element, 
len(A)-# of occurrence is how many switches needed. find the minimum of them.

Second try: no need to know possible values, just enumerate all
1. for all possible value between 1:6
for A and B, count the occurrences of the element, 
len(A)-# of occurrence is how many switches needed. find the minimum of them.
"""


# class Solution:
#     def minDominoRotations(self, A, B) -> int:
#         dice_set = set()
#         dice_set.add(A[0])
#
#         dice_set.add(B[0])
#         for i in range(1, len(A)):
#             dice_set = dice_set.intersection({A[i], B[i]})
#         if len(dice_set) == 0:
#             return -1
#         min_rotation = len(A)
#         for d in dice_set:
#             count_a, count_b = 0, 0
#             for i in range(len(A)):
#                 if A[i] == d:
#                     count_a += 1
#                 if B[i] == d:
#                     count_b += 1
#             min_rotation = min(len(A) - count_a, len(A) - count_b, min_rotation)
#
#         return min_rotation

class Solution:
    def minDominoRotations(self, A, B) -> int:

        min_rotation = len(A) + 1
        for d in range(1, 7):
            count_a, count_b = 0, 0
            for i in range(len(A)):
                if A[i] != d and B[i] != d:
                    break  # not possible for this d
                elif A[i] == d and B[i] == d:
                    continue  # no need to swap for this d
                elif A[i] != d and B[i] == d:
                    count_a += 1
                else:
                    count_b += 1
            else:  # only execute if not break
                min_rotation = min(count_a, count_b, min_rotation)
        if min_rotation > len(A):
            min_rotation = -1
        return min_rotation


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [2, 1, 2, 4, 2, 2]
        B = [5, 2, 6, 2, 3, 2]
        self.assertEqual(2, Solution().minDominoRotations(A, B))

    def test2(self):
        A = [3, 5, 1, 2, 3]
        B = [3, 6, 3, 3, 4]
        self.assertEqual(-1, Solution().minDominoRotations(A, B))


if __name__ == '__main__':
    unittest.main()
