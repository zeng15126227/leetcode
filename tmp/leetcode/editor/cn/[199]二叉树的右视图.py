# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,null,3]
# 输出: [1,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  -100 <= Node.val <= 100 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 525 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        rem = {}

        queue = collections.deque()
        #元素，层数
        queue.append((root, 0))
        while (queue):
            node, depth = queue.popleft()
            #<层数,元素>保存在map中，因为每一层遍历是从左到右，所以最终map里保存的是最右边元素
            rem[depth] = node
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return [rem[t].val for t in rem]




# leetcode submit region end(Prohibit modification and deletion)
