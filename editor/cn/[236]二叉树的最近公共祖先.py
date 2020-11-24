# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#  
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉树中。 
#  
#  Related Topics 树 
#  👍 840 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        flag = False
        res = None

        def dfs(root, p, q):
            #嵌套函数变量
            nonlocal flag
            nonlocal res
            #递归条件判断
            if not root:
                return False
            #判断左右子树是否包含目标
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            #记录公共父节点，
            if (not flag) and ((left and right) or ((root.val==p.val or root.val==q.val) and (left or right))):
                res = root
                flag=True
            #返回当前节点是否包含目标
            return left or right or root.val==p.val or root.val==q.val



        dfs(root,p,q)
        return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    a=TreeNode(1)
    b=TreeNode(2)
    c=TreeNode(3)
    a.left=b
    a.right=c

    res = Solution().lowestCommonAncestor(a,b,c)
    print(res.val)
