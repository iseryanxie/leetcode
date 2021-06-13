import unittest

"""
write down thoughts
"""


class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        s = set(source)
        for ch in set(target):
            if ch not in s:
                return -1 # rule out the possibility that some letter in target cannot be formed

        i, j = 0, 0
        res = 0
        while j < len(target):
            i = 0  # 每次从source的头部开始找
            while i < len(source) and j < len(target):
                if source[i] == target[j]:  # 如果当前位匹配上，则继续往后找
                    i += 1
                    j += 1
                else:  # 没匹配上则只让 i 往前走一步
                    # in this case, the letter is skipped (i.e., we can delete letters in the string to form substring and match)
                    i += 1
            res += 1  # 找到了目前最长的子序列
        return res


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     source = "abc"
    #     target = "abcbc"
    #     self.assertEqual(2, Solution().shortestWay(source,target))
    #
    # def test2(self):
    #     source = "abc"
    #     target = "acdbc"
    #     self.assertEqual(-1, Solution().shortestWay(source, target))

    def test3(self):
        source = "xyz"
        target = "xzyxz"
        self.assertEqual(3, Solution().shortestWay(source, target))


if __name__ == '__main__':
    unittest.main()
