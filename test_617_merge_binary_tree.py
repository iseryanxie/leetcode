# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        return root1

if __name__ == '__main__':
    leaf5 = TreeNode(val=5)
    branch3 = TreeNode(val=3, left=leaf5)
    branch2 = TreeNode(val=2)
    root1 = TreeNode(val=1, left=branch3, right=branch2)
    leaf4 = TreeNode(val=4)
    leaf7 = TreeNode(val=7)
    branch1 = TreeNode(val=1, right=leaf4)
    branch3 = TreeNode(val=3, right=leaf7)
    root2 = TreeNode(val=2, left=branch1, right=branch3)
    ans = Solution().mergeTrees(root1,root2)
    print(ans)


