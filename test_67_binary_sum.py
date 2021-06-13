import unittest

"""
Method 1
1. Use Python bin function
Method 2
Use two pointers
"""


# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a, base=2) + int(b, base=2))[2:]

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry_digit = 0
        res = ""
        while a or b:
            na, nb = 0, 0
            if a:
                na = int(a[-1])
                a = a[:-1]
            if b:
                nb = int(b[-1])
                b = b[:-1]

            if na + nb + carry_digit == 3:
                carry_digit = 1
                res = '1' + res
            elif na + nb + carry_digit == 2:
                carry_digit = 1
                res = '0' + res
            elif na + nb + carry_digit == 1:
                carry_digit = 0
                res = '1' + res
            else:
                carry_digit = 0
                res = '0' + res
        if carry_digit == 1:
            res = '1' + res
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        a = "101"
        b = "1"
        self.assertEqual("110", Solution().addBinary(a, b))

    def test2(self):
        a = "101"
        b = "11"
        self.assertEqual("1000", Solution().addBinary(a, b))


if __name__ == '__main__':
    unittest.main()
