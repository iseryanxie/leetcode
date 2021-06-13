# Too slow to pass
# class NumMatrix(object):
#
#     def __init__(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         """
#         self.matrix = matrix
#
#     def sumRegion(self, row1, col1, row2, col2):
#         """
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
#         if row1>row2 or col1>col2 or col1>len(self.matrix[0]) or col2>len(self.matrix[0])\
#                 or row1>len(self.matrix) or row2>len(self.matrix):
#             return None
#         total = 0
#         for r in range(row1,row2+1):
#             for c in range(col1,col2+1):
#                 total += self.matrix[r][c]
#         return total

# precalculate sum
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not (matrix[0]):
            R, C = 0, 0
        else:
            R, C = len(matrix), len(matrix[0])
        # initialize matrix
        self.sumElem = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.sumElem[r + 1][c + 1] = -self.sumElem[r][c] + self.sumElem[r + 1][c] + self.sumElem[r][c + 1] + \
                                             matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumElem[row2 + 1][col2 + 1] - self.sumElem[row1][col2 + 1] - self.sumElem[row2 + 1][col1] + \
               self.sumElem[row1][col1]


if __name__ == '__main__':
    sumElem = [[0] * (5) for _ in range(5)]
    print(sumElem)
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    test_cases = [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    for l in test_cases:
        ans = obj.sumRegion(l[0], l[1], l[2], l[3])
        print(ans)
