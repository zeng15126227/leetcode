# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应
# 该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。 
# 
#  所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,0,2], low = 1, high = 2
# 输出：[1,null,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# 输出：[3,2,null,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1], low = 1, high = 2
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,null,2], low = 1, high = 3
# 输出：[1,null,2]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2], low = 2, high = 4
# 输出：[2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数在范围 [1, 104] 内 
#  0 <= Node.val <= 104 
#  树中每个节点的值都是唯一的 
#  题目数据保证输入是一棵有效的二叉搜索树 
#  0 <= low <= high <= 104 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 
#  👍 420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root: return None
        # 小于下边界的遍历右子树
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 大于上边界的遍历左子树
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 在范围内的节点
        # 对有效范围内的节点重新连接左右孩子
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

# leetcode submit region end(Prohibit modification and deletion)
