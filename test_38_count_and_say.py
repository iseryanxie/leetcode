import unittest

"""
write down thoughts
recursive call countAndSay(n-1)
not combining all 1s,2s,...
"""


# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return "1"
#         last = self.countAndSay(n - 1)
#         p = ""
#         count = 0
#         res_num = []
#         res_count = [] #no need for additional list, just use str
#         for i,c in enumerate(last):
#             if i==0:
#                 p = c
#                 count = 1
#                 continue
#             if c == p:
#                 count += 1
#             else:
#                 res_num.append(p)
#                 res_count.append(count)
#                 count = 1
#                 p = c
#         res_num.append(p)
#         res_count.append(count)
#         res = [str(res_count[i]) + res_num[i] for i in range(len(res_num))]
#         return "".join(res)
class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"

        # recursive call
        seq = self.countAndSay(n - 1)
        i = 0
        re = ''
        c = 1
        for i in range(1, len(seq)):
            if seq[i] == seq[i - 1]:
                c += 1
            else:
                re += str(c) + seq[i - 1]
                c = 1
        re += str(c) + seq[-1]  # record last one
        return re

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("1211", Solution().countAndSay(4))
    def test2(self):
        self.assertEqual("111221", Solution().countAndSay(5))


if __name__ == '__main__':
    unittest.main()
