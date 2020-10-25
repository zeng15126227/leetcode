# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:

        if not root:
            return []

        stack=[]
        stack.append(root)
        res=[]

        while stack:
            i = len(stack)
            level=[]
            for i in range(i):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                level.append(cur.val)
            res.append(level)

        return res

if __name__ == "__main__":
    root=TreeNode(3)
    b=TreeNode(1)
    c=TreeNode(2)
    root.left=b
    root.right=c

    res = Solution().levelOrder(root)
    print(res)





