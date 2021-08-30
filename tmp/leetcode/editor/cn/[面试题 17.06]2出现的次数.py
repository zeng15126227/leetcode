# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。 
# 
#  示例: 
# 
#  输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次) 
# 
#  提示： 
# 
#  
#  n <= 10^9 
#  
#  Related Topics 递归 数学 动态规划 
#  👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def numberOf2sInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:return 0

        #求位数
        #digit = int(math.log(n,10))+1
        digit = len(str(n))

        #dp[i][0] = num2(n) 1～i位组成的数包含2的个数
        #dp[i][1] = num2(i个9) 保存i位均为9包含2的个数
        dp = [[0]*2 for _ in range(digit+1)]
        #下标从1开始，初始化第一位，区分有没有2
        dp[1][0] = 1 if n%10>=2 else 0
        dp[1][1] = 1

        for i in range(2,digit+1):
            #取第i位，用pow(10,i-1)去掉i之后位数，%10取末尾值
            k = int(n//math.pow(10,i-1)%10)
            #注意0也需要计入，当前位位0，如果前面有数据则需要0，如果前面没有数据则会退化
            dp[i][0] = k*dp[i-1][1]+dp[i-1][0]
            if k==2:
                dp[i][0] += int(n%(math.pow(10,i-1)))+1
            if k>2:
                dp[i][0] += int(math.pow(10,i-1))

            dp[i][1] = 10*dp[i-1][1]+int(math.pow(10,i-1))

        return dp[digit][0]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().numberOf2sInRange(1000000000)
    print(res)

