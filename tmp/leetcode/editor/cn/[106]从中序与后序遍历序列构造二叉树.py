# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 
#  👍 561 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # 左右中
        # 左中右
        def mybuildTree(i: list, p: list):
            if not p:
                return
            # 后序遍历最后一个节点是根
            root = TreeNode(p[-1])
            # 跟节点在中序遍历中的下标
            idx = i.index(p[-1])
            # 后序用长度分割，中序用下标分割
            root.left = mybuildTree(i[:idx], p[:idx])
            root.right = mybuildTree(i[idx + 1:], p[idx:-1])
            return root

        return mybuildTree(inorder, postorder)
# leetcode submit region end(Prohibit modification and deletion)
