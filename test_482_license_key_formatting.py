import unittest

"""
write down thoughts
1. start from -1
2. convert to upper, add - every k
3. reverse order in the end, need to remove the trailing - when number of valid char %k ==0
"""


class Solution(object):
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        count = 0
        for _, c in enumerate(s[::-1]):
            if c != "-":
                count += 1
                res += c.upper()
                if count % k == 0:
                    res += "-"
            else:
                continue
        return res[::-1] if count % k != 0 else res[:-1][::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "5F3Z-2e-9-w"
        k = 4
        self.assertEqual("5F3Z-2E9W", Solution().licenseKeyFormatting(s, k))

    def test2(self):
        s = "--a-a-a-a--"
        k = 2
        self.assertEqual("AA-AA", Solution().licenseKeyFormatting(s, k))

    def test3(self):
        s = "a-a-a-a-"
        k = 1
        self.assertEqual("A-A-A-A", Solution().licenseKeyFormatting(s, k))


if __name__ == '__main__':
    unittest.main()
