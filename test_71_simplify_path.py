import unittest

"""
write down thoughts
first split, then push to stack
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for directory in path:
            if not directory or directory.strip()==".": #.strip() is optional, it removes leading and trailing spaces
                continue
            elif directory.strip()=="..":
                if stack: # test if is already root, handles cases like "/../"
                    stack.pop()
            else:
                stack.append(directory) # ... is considered a regular directory
        return "/"+"/".join(stack)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("/c", Solution().simplifyPath("/a/./b/../../c/"))
    def test2(self):
        self.assertEqual("/", Solution().simplifyPath("/../"))


if __name__ == '__main__':
    unittest.main()
