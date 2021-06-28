import unittest

"""
write down thoughts
basic stack and another stack to keep track of the minimum value at the top of the stack, in order to support
getMin method. 
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val) # the minimum number as of this layer of the stack
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        minStack = MinStack()
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        self.assertEqual(0, minStack.top())
        self.assertEqual(-2, minStack.getMin())



if __name__ == '__main__':
    unittest.main()
