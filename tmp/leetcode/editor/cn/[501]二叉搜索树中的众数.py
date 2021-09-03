# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。 
# 
#  假定 BST 有如下定义： 
# 
#  
#  结点左子树中所含结点的值小于等于当前结点的值 
#  结点右子树中所含结点的值大于等于当前结点的值 
#  左子树和右子树都是二叉搜索树 
#  
# 
#  例如： 
# 给定 BST [1,null,2,2], 
# 
#     1
#     \
#      2
#     /
#    2
#  
# 
#  返回[2]. 
# 
#  提示：如果众数超过1个，不需考虑输出顺序 
# 
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内） 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 
#  👍 341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        pre = None
        count=0
        max_count=0
        res=[]

        def dfs(root):
            nonlocal pre
            nonlocal count
            nonlocal max_count
            nonlocal res

            if not root:
                return
            #左
            if root.left:
                dfs(root.left)
            #中
            if not pre:  #第一个节点
                count=1
            elif pre.val==root.val:  #遍历到相同元素
                count+=1
            else:   #遍历到不同元素
                count=1
            #对最大值，结果数组进行更新
            if count == max_count:
                res.append(root.val)
            elif count > max_count:
                res = [root.val]
                max_count = count
            pre = root

            #右
            if root.right:
                dfs(root.right)

        dfs(root)
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    b = TreeNode(2)
    root.right = b
    res = Solution().findMode(root)
    print(res)
