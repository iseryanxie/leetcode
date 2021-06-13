import unittest

"""
write down thoughts
Use backtrack to enumerate all combinations
1. initialize empty list
2. define backtrack recursive method
    1. if length is enough, append to output list
    2. if # of open is not used up, add left ( to tmp and branch recursion on left
    3. if # of open is more than close, add right ) to tmp and branch recursion on right

1. Choice
choose ( or )
2. Constraint
cannot ) before (
3. Goal
have total 2*n parenthesis
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(tmp, open, close, max):
            if len(tmp) == 2 * max:
                res.append(tmp)
            if open < max:
                backtrack(tmp + "(", open + 1, close, max) # add recursion, note this does not skip the next if
            if open > close:
                backtrack(tmp + ")", open, close + 1, max)

        backtrack("", 0, 0, n)
        return res
        # res = []
        #
        # def dfs(tmp, left, right):
        #     if len(tmp) == 2 * n:
        #         res.append(tmp)
        #
        #     if left:
        #         dfs(tmp + "(", left - 1, right)
        #     if right > left:
        #         dfs(tmp + ")", left, right - 1)
        #
        # dfs("", n, n)
        # return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"], Solution().generateParenthesis(3))


if __name__ == '__main__':
    unittest.main()
