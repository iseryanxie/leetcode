import unittest

"""
write down thoughts
in pop method, the queue is iterated to the end to get the last element, the second queue is acting as a space
to store the emptied queue.
"""

from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._top = None
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._top = x
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1)>1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if len(self.q1)>0 else True


class TestSolution(unittest.TestCase):
    def test1(self):
        obj = MyStack()
        obj.push(1)
        obj.push(2)
        self.assertEqual(2,obj.top())
        self.assertEqual(2,obj.pop())
        self.assertEqual(False,obj.empty())
        self.assertEqual(1, obj.pop())
        self.assertEqual(True, obj.empty())


if __name__ == '__main__':
    unittest.main()
