# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def mybuildTree(p: list, i: list):
            if not p:
                return None
            root = TreeNode(p[0])
            idx = i.index(p[0])
            root.left = mybuildTree(p[1:idx + 1], i[0:idx])
            root.right = mybuildTree(p[idx + 1:], i[idx + 1:])
            return root

        return mybuildTree(preorder, inorder)


if __name__ == "__main__":
    res = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(res)
