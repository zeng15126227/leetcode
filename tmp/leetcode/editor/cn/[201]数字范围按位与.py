# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）
# 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：left = 5, right = 7
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：left = 0, right = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：left = 1, right = 2147483647
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= left <= right <= 231 - 1 
#  
#  Related Topics 位运算 
#  👍 313 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left==right or left==0:
            return left

        move=0
        while left!=right:
            left = left>>1
            right = right>>1
            move+=1
        left = left<<move

        return left

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().rangeBitwiseAnd(5,7)
    print(res)
