# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 751 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:

        # if not root:
        #     return []
        #
        # stack = []
        # stack.append(root)
        # res = []
        # visited=[]
        #
        # while stack:
        #     cur = stack.pop()
        #     if not cur.left or cur.left in visited:
        #         res.append(cur.val)
        #         visited.append(cur)
        #         if cur.right and cur.right not in stack:
        #             stack.append(cur.right)
        #     else:
        #         if cur.right:
        #             stack.append(cur.right)
        #         stack.append(cur)
        #         stack.append(cur.left)
        #
        # return res

        res=[]
        stack=[]

        cur=root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res





        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    root=TreeNode(3)
    b=TreeNode(1)
    c=TreeNode(2)
    root.left=b
    root.right=c

    res = Solution().inorderTraversal(root)
    print(res)
