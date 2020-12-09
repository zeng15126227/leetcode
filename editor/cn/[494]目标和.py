# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选
# 择一个符号添加在前面。 
# 
#  返回可以使最终数组和为目标数 S 的所有添加符号的方法数。 
# 
#  
# 
#  示例： 
# 
#  输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
#  
# 
#  
# 
#  提示： 
# 
#  
#  数组非空，且长度不会超过 20 。 
#  初始的数组的和不会超过 1000 。 
#  保证返回的最终结果能被 32 位整数存下。 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: list, S: int) -> int:
        #sum(+) + sum(-) = sum
        #sum(+) - sum(-) = target
        #sum(+) + sum(-) + sum(+) - sum(-) = 2sum(+) = target + sum
        #sum(+)=(target + sum)/2
        #求在列表中找出某些物品，使其重量为(target + sum)/2的所有方法

        all_sum = sum(nums)
        target = S + all_sum
        if all_sum<S or target%2==1:
            return 0
        dp=[0 for _ in range((target//2)+1)]
        dp[0]=1
        for i in range(len(nums)):
            for j in range((target//2),nums[i]-1,-1):
                dp[j]=dp[j]+dp[j-nums[i]]
        return dp[-1]

        # if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        # P = (sum(nums) + S) // 2
        # dp = [1] + [0 for _ in range(P)]
        # for num in nums:
        #     for j in range(P, num - 1, -1): dp[j] += dp[j - num]
        # return dp[P]



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().findTargetSumWays([1,1,1,1,1],3)
    print(res)