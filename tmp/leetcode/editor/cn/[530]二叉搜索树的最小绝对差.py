# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。 
# 
#  
# 
#  示例： 
# 
#  输入：
# 
#    1
#     \
#      3
#     /
#    2
# 
# 输出：
# 1
# 
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中至少有 2 个节点。 
#  本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 
# 相同 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 
#  👍 268 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_res = float('inf')
        pre = None

        def dfs(root):
            nonlocal min_res
            nonlocal pre

            if not root:
                return

            if root.left:
                dfs(root.left)

            if pre:
                min_res = min(min_res,root.val-pre.val)
            pre = root

            if root.right:
                dfs(root.right)

        dfs(root)
        return min_res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(236)
    b = TreeNode(104)
    c = TreeNode(701)
    d = TreeNode(227)
    e = TreeNode(911)
    root.left = b
    root.right = c
    b.right=d
    c.right=e
    res = Solution().getMinimumDifference(root)
    print(res)
