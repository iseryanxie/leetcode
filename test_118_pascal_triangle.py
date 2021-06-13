class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if numRows == 0:
            return ans
        ans.append([1])
        for row_num in range(1, numRows):
            prev_row = ans[row_num - 1]
            row = [1]
            for j in range(1,row_num):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
            ans.append(row)
        return ans


if __name__ == '__main__':
    ans = Solution().generate(5)
    print(ans)
