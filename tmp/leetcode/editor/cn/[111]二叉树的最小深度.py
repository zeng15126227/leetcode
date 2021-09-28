# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 105] 内 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):

            # 单节点
            if not root.left and not root.right:
                return 1

            min_dep = float('inf')
            # 只有存在叶子结点才比较
            if root.left:
                min_dep = min(dfs(root.left), min_dep)
            if root.right:
                min_dep = min(dfs(root.right), min_dep)

            return min_dep + 1

        return dfs(root)

        # if not root:
        #     return 0
        #
        # stack = []
        # stack.append(root)
        # res = 0
        #
        # while stack:
        #     res += 1
        #
        #     i = len(stack)
        #
        #     for i in range(i):
        #         cur = stack.pop(0)
        #         #剪枝
        #         if not cur.left and not cur.right:
        #             return res
        #
        #         if cur.left:
        #             stack.append(cur.left)
        #         if cur.right:
        #             stack.append(cur.right)

# leetcode submit region end(Prohibit modification and deletion)
