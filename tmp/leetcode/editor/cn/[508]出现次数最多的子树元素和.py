# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。 
# 
#  你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。 
# 
#  
# 
#  示例 1： 
# 输入: 
# 
#    5
#  /  \
# 2   -3
#  
# 
#  返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。 
# 
#  示例 2： 
# 输入： 
# 
#    5
#  /  \
# 2   -5
#  
# 
#  返回 [2]，只有 2 出现两次，-5 只出现 1 次。 
# 
#  
# 
#  提示： 假设任意子树元素和均可以用 32 位有符号整数表示。 
#  Related Topics 树 深度优先搜索 哈希表 二叉树 
#  👍 120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        rem = {}

        def dfs(root):
            if not root:return 0

            left = dfs(root.left)
            right = dfs(root.right)
            cur = left+right+root.val
            if cur in rem:
                rem[cur]+=1
            else:
                rem[cur]=1
            return cur

        dfs(root)

        res=[]
        tmp=0
        for i in rem:
            if(rem[i]>tmp):
                res=[]
                res.append(i)
                tmp=rem[i]
            elif(rem[i]==tmp):
                res.append(i)

        return res




# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a=TreeNode(5)
    b = TreeNode(2)
    c = TreeNode(-3)
    a.left=b
    a.right=c
    res = Solution().findFrequentTreeSum(a)
    print(res)
