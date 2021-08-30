# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
# 
#  
# 
#  提示： 
# 
#  
#  -100.0 < x < 100.0 
#  -231 <= n <= 231-1 
#  -104 <= xn <= 104 
#  
#  Related Topics 递归 数学 
#  👍 724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def caculate(n):
            if n == 0:
                return 1.0
            y = caculate(n//2)
            if n%2==0:
                tmp = y*y
            else:
                tmp = y*y*x

            return tmp

        return caculate(n) if n>=0 else 1/caculate(-n)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().myPow(2,10)
    print(res)