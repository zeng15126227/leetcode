# 计算给定二叉树的所有左叶子之和。 
# 
#  示例： 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24 
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 340 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0

            # 一个节点最多一个左叶子结点
            cur_value = 0
            if root.left and not root.left.left and not root.left.right:
                cur_value = root.left.val

            left_val = dfs(root.left)
            right_val = dfs(root.right)

            return left_val + right_val + cur_value

        return dfs(root)

# leetcode submit region end(Prohibit modification and deletion)
