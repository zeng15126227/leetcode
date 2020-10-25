# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        t=root

        while t:
            if t.left:
                tmp = t.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right=t.right
                t.right=t.left
                t.left=None
            t=t.right



