# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            # 用递归函数，比较左节点，右节点

        return dfs(root, root)


if __name__ == "__main__":
    root = TreeNode(2)
    a = TreeNode(3)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(4)

    root.left=a
    root.right=b
    a.left=c
    a.right=d
    b.right=e



    res = Solution().isSymmetric(root)
    print(res)

