# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 
# 
#  假设二叉树中至少有一个节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1,104] 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 197 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        res = 0
        max_deep = -1

        def dfs(root, deep):
            nonlocal res, max_deep

            if not root:
                return
            if not root.left and not root.right:
                #用第一次deep的更新判断是不是一层的最左元素
                if deep > max_deep:
                    max_deep = deep
                    res = root.val
            dfs(root.left, deep + 1)
            dfs(root.right, deep + 1)

        dfs(root, 0)

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left=b
    a.right=c
    res = Solution().findBottomLeftValue(a)
    print(res)
