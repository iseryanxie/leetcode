import unittest
import bisect

"""
write down thoughts
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in s[::-1]:
            if c == " ":
                if count==0:
                    continue
                else:
                    break
            else:
                count += 1

        return count


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, Solution().lengthOfLastWord("Hello World"))

    def test2(self):
        self.assertEqual(10, Solution().lengthOfLastWord("HelloWorld"))

    def test3(self):
        self.assertEqual(1, Solution().lengthOfLastWord("a "))
    def test4(self):
        self.assertEqual(0, Solution().lengthOfLastWord(" "))


if __name__ == '__main__':
    unittest.main()
