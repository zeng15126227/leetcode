class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res=0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        cur=self.count(root,sum)
        left_count=self.pathSum(root.left,)
        right_count = self.pathSum(root.right)
        return cur + left_count + right_count

    def count(self,root,sum):
        if not root:
            return
        sum = sum - root.val
        if sum==0:
            self.res+=1
        self.count(root.left,sum)
        self.count(root.right,sum)

if __name__ == "__main__":
    Solution().pathSum()