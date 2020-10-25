# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack=[]
        stack.append(root)
        res=0


        while stack:
            res+=1
            i = len(stack)

            for i in range(i):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return res



        return res



        # def find_d(node):
        #     if not node:
        #         return 0
        #     else:
        #         return max(find_d(node.left),find_d(node.right))+1
        #
        # return find_d(root)





if __name__ == "__main__":
    root=TreeNode(3)
    b=TreeNode(1)
    c=TreeNode(2)
    root.left=b
    root.right=c

    res = Solution().maxDepth(root)
    print(res)
