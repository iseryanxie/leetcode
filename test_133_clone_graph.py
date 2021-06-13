import unittest

"""
write down thoughts
1. create a hashmap to map old node to new node
2. use dfs, which returns a copy of the node that has value and all of its neighbor created
    1. if node already exists, return the new node found in the hashmap
    2. otherwise, create copy of the current node, copy value
    3. for each neighbor in the current node, dfs(neighbor)
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy  # must add to hashmap before calling recursive dfs
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


class TestSolution(unittest.TestCase):
    def test1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node4]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        clone_node = Solution().cloneGraph(node1)
        self.assertEqual(1, clone_node.val)
        self.assertEqual([2, 4], [n.val for n in clone_node.neighbors])


if __name__ == '__main__':
    unittest.main()
