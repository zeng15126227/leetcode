# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“
# 房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。 
# 
#  计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。 
# 
#  示例 1: 
# 
#  输入: [3,2,3,null,3,null,1]
# 
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7. 
# 
#  示例 2: 
# 
#  输入: [3,4,5,1,3,null,1]
# 
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#  
#  Related Topics 树 深度优先搜索 
#  👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def rob(node):
            if not node:
                return [0,0]
            #res的0表示不偷该节点的最大收益，1表示偷该节点的最大收益
            res=[]
            left = rob(node.left)
            right = rob(node.right)
            #不偷node
            res.append(max(left) + max(right))
            #偷node
            res.append(node.val + left[0] + right[0])

            return res

        res = rob(root)
        return max(res)

        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(1)
    a.left=b
    a.right=c
    b.left=d
    b.right=e
    c.right=f

    res = Solution().rob(a)
    print(res)
