# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 数组 哈希表 分治 二叉树 
#  👍 543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        # 快速在中序列表查询位置
        rem = {element: i for i, element in enumerate(inorder)}

        def buildTreeSeg(pre_start, pre_end, in_start, in_end):
            # 递归结束条件
            if (pre_start > pre_end): return None

            # 前序遍历root位置
            pre_root = pre_start
            # 中序遍历root位置
            in_root = rem[preorder[pre_root]]
            # 子树长度
            seg_len = in_root - in_start
            # 构建跟节点
            root = TreeNode(preorder[pre_start])
            # 构建左子树
            root.left = buildTreeSeg(pre_root + 1, pre_root + seg_len, in_start, in_root - 1)
            # 构建右子树
            root.right = buildTreeSeg(pre_root + seg_len + 1, pre_end, in_root + 1, in_end)
            return root

        length = len(inorder)
        return buildTreeSeg(0, length - 1, 0, length - 1)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().buildTree([1, 2], [2, 1])
