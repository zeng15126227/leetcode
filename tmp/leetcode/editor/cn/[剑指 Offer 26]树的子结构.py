# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) 
# 
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。 
# 
#  例如: 
# 给定的树 A: 
# 
#  3 
#  / \ 
#  4 5 
#  / \ 
#  1 2 
# 给定的树 B： 
# 
#  4 
#  / 
#  1 
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。 
# 
#  示例 1： 
# 
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true 
# 
#  限制： 
# 
#  0 <= 节点个数 <= 10000 
#  Related Topics 树 深度优先搜索 二叉树 
#  👍 329 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if (not A or not B):
            return False

        # 以An为root，与B匹配
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        # 中序遍历A的所有子节点，分别为root与B匹配
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().isSubStructure()
