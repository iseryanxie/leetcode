import unittest

"""
write down thoughts
calculate digit by digit. Similar to LC 43, template to convert to numbers back and forth.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = [ord(n) - ord('0') for n in num1]
        l2 = [ord(n) - ord('0') for n in num2]
        l1.reverse()
        l2.reverse()
        carry = 0
        n1 = len(l1)
        n2 = len(l2)
        if n1 <= n2:
            max_l = n2
        else:
            max_l = n1
        res = []
        for i in range(max_l):
            tmpsum = 0
            if i < n1:
                tmpsum += l1[i]
            if i < n2:
                tmpsum += l2[i]
            tmpsum += carry
            carry = tmpsum // 10
            res.append(str(tmpsum % 10))
        if carry > 0:
            res.append(str(carry))
        res.reverse()
        return "".join(res)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("134", Solution().addStrings("11", "123"))

    def test2(self):
        self.assertEqual("1033", Solution().addStrings("956", "77"))


if __name__ == '__main__':
    unittest.main()
