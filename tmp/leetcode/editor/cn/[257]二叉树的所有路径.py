# 给定一个二叉树，返回所有从根节点到叶子节点的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  输入:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
#  Related Topics 树 深度优先搜索 字符串 二叉树 
#  👍 566 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res=[]

        def dfs(root,path):
            if (not root):return
            path+=str(root.val)
            if not root.left and not root.right:
                res.append(path)
            else:
                path+="->"
            dfs(root.left,path)
            dfs(root.right,path)


        dfs(root,"")

        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    a.left=b
    a.right=c
    b.right=d
    res = Solution().binaryTreePaths(a)
    print(res)
