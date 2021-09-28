# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [2, 105] 内。 
#  -109 <= Node.val <= 109 
#  所有 Node.val 互不相同 。 
#  p != q 
#  p 和 q 均存在于给定的二叉树中。 
#  
#  Related Topics 树 深度优先搜索 二叉树 
#  👍 1273 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #注意条件
        # 1. 树中节点互不相同
        # 2. pq都存在
        if not root:
            return False

        def dfs(root,p,q):
            if not root:return False
            #终止条件：找到任意一个就返回当前节点
            if root==p or root==q:
                return root
            #找父亲节点，是从下往上的过程，先处理子节点再处理父亲节点
            #后序遍历
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)

            if left and right:  #找到公共父亲节点
                return root
            elif left:      #还没有找到公共父亲节点
                return left
            else:
                #返回右子树或者False
                return right

        return dfs(root,p,q)


        
# leetcode submit region end(Prohibit modification and deletion)
