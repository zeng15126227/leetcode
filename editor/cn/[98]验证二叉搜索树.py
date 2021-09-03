# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 
#  👍 814 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # if not root:
        #     return True
        #
        # up = float('inf')
        # low = float('-inf')
        #
        # def check(node,up,low):
        #     if node.val >= up  or node.val <= low :
        #         return False
        #     left=True
        #     right=True
        #     if node.left:
        #         left = check(node.left,node.val,low)
        #     if node.right:
        #         right = check(node.right,up,node.val)
        #     return left and right
        #
        # return check(root,up,low)

        if not root:
            return True
        # 二叉搜索树中序遍历是从小到大，所以我们只需要不断验证下边界

        lower_boundary = float('-inf')

        def dfs(root):
            nonlocal lower_boundary
            #空节点认为是二叉搜索树
            left=True
            right=True
            #左
            if root.left:
                left = dfs(root.left)
            #中
            if root.val > lower_boundary:
                lower_boundary = root.val
            else:
                return False
            #右
            if root.right:
                right = dfs(root.right)

            return left and right

        return dfs(root)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    root.left = b
    root.right = c
    res = Solution().isValidBST(root)
    print(res)
