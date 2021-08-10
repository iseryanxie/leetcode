import unittest

"""
write down thoughts
use multiply digits by digits
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = [ord(n) - ord('0') for n in num1]
        l2 = [ord(n) - ord('0') for n in num2]
        l1.reverse()
        l2.reverse()
        n1 = len(l1)
        n2 = len(l2)
        # multiply 2 digits number with another 2 digits number will get at most 4 digits number
        l = [0] * (n1 + n2)  # placeholder 0s, remove leading 0s in the end
        carry = 0
        for i in range(n1):
            for j in range(n2):
                sum = l1[i] * l2[j] + l[i + j] + carry  # current, previous and carry
                l[i + j] = sum % 10  # how many digits: for example, 6* x 6*, i=1,j=1, then 36**, l[1+1]
                carry = sum // 10
            l[n2 + i] += carry
            carry = 0

        # remove leading 0s
        while len(l) > 1 and l[-1] == 0:
            l.pop()
        # convert to string
        l.reverse()
        l = [str(i) for i in l]
        return "".join(l)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("600", Solution().multiply("20", "30"))

    def test2(self):
        self.assertEqual("56088", Solution().multiply("123", "456"))

    def test3(self):
        self.assertEqual("0", Solution().multiply("0", "0"))


if __name__ == '__main__':
    unittest.main()
