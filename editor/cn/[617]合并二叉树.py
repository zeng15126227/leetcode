# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1 and not t2:
            return 0
        if not t1:
            return t2
        if not t2:
            return t1

        tree1=[]
        tree2=[]
        queue=[]
        queue.append(t1)
        while queue:
            cur = queue.pop(0)
            if 