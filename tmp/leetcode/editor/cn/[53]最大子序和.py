# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [-1]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [-100000]
# 输出：-100000
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治 动态规划 
#  👍 3650 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        #dp[i]表示以第i个元素结尾的最大和子序列
        dp=[0]*(len(nums)+1)
        for i in range(1,len(dp)):
            dp[i] = max(nums[i-1],dp[i-1]+nums[i-1])
            res = max(res,dp[i])

        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
