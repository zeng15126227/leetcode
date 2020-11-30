# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 lef
# t 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  说明: 
# 
#  
#  你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。 
#  0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 
#  
# 
#  示例: 
# 
#  输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#  
#  Related Topics 分治算法 动态规划 
#  👍 581 👎 0

#删除元素后，左右邻居发生变化，用动态规划无法计算
#反过来思考，从一个空列表插入节点
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: list) -> int:
        n=len(nums)
        #在nums头尾添加哨兵1
        nums.insert(0,1)
        nums.insert(n+1,1)
        #构造dp数组
        dp = [[0] * (n+2) for i in range(n+2)]
        #i<k<j,计算dp[i,j]时会使用到dp[i,k],dp[k,j],分别在dp[i][j]的左边和下边，
        #所以i从下往上算，j从左往右算
        for i in range(n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    #动态方程
                    total = nums[i]*nums[k]*nums[j]
                    total+=dp[i][k]+dp[k][j]
                    dp[i][j]=max(total,dp[i][j])
        return dp[0][n+1]



        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().maxCoins([3,1,5,8])
    print(res)
