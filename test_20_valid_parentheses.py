import unittest

"""
write down thoughts
use a stack 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        last_open = []
        for c in s:
            if c == '(':
                last_open.append('p')
            elif c == ')':
                if len(last_open) == 0 or last_open[-1] != 'p':
                    return False
                last_open.pop()
            elif c == '[':
                last_open.append('b')
            elif c == ']':
                if len(last_open) == 0 or last_open[-1] != 'b':
                    return False
                last_open.pop()
            elif c == '{':
                last_open.append('c')
            elif c == '}':
                if len(last_open) == 0 or last_open[-1] != 'c':
                    return False
                last_open.pop()
            else:
                return False

        return (len(last_open) == 0)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isValid("()"))

    def test2(self):
        self.assertEqual(False, Solution().isValid("([)]"))

    def test3(self):
        self.assertEqual(True, Solution().isValid("()[]{}"))


if __name__ == '__main__':
    unittest.main()
