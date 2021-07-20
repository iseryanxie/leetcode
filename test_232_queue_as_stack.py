import unittest

"""
write down thoughts
use two stacks to implement the queue, similar to LC 225
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = None
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        if self.s2:
            self.front = self.s2[-1]  # -1 will get index error when s2 is empty
        else:
            self.front = None
        while self.s2:
            self.s1.append(self.s2.pop())

        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


class TestSolution(unittest.TestCase):
    def test1(self):
        myQueue = MyQueue()
        myQueue.push(1)  # queue is: [1]
        myQueue.push(2)  # queue is: [1, 2](leftmost is front of the queue)
        self.assertEqual(1, myQueue.peek())  # return 1
        self.assertEqual(1, myQueue.pop())  # return 1, queue is [2]
        self.assertEqual(False, myQueue.empty())  # return false
    def test2(self):
        myQueue = MyQueue()
        myQueue.push(1)  # queue is: [1]
        self.assertEqual(1, myQueue.pop())  # return 1, queue is [2]
        self.assertEqual(True, myQueue.empty())  # return false


if __name__ == '__main__':
    unittest.main()
