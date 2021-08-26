# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 124 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            res_seg=[]
            for i in range(length):
                node = queue.popleft()
                res_seg.append(node.val)
                if node.left:queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(res_seg if len(res)%2==0 else res_seg[::-1])

        return res
# leetcode submit region end(Prohibit modification and deletion)
