# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。 
# 
#  示例1: 
# 
#  
#  输入：A = 1, B = 10
#  输出：10
#  
# 
#  示例2: 
# 
#  
#  输入：A = 3, B = 4
#  输出：12
#  
# 
#  提示: 
# 
#  
#  保证乘法范围不会溢出 
#  
#  Related Topics 位运算 递归 数学 
#  👍 46 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if B==0 or A==0:
            return 0
        if(A<B):
            return B+self.multiply(A-1,B)
        else:
            return A+self.multiply(A,B-1)
# leetcode submit region end(Prohibit modification and deletion)
