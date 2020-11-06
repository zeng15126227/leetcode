# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 822 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: list) -> int:

        if not nums:
            return 0

        res_max=nums[0]
        # 表示以i结尾的最大乘积，最小乘积用于负号相乘
        dfmax = [nums[0] for _ in nums]
        dfmin = [nums[0] for _ in nums]
        for i in range(1, len(nums)):
            dfmax[i] = max(nums[i], dfmax[i - 1] * nums[i], dfmin[i-1]*nums[i])
            dfmin[i] = min(nums[i], dfmin[i - 1] * nums[i], dfmax[i-1]*nums[i])
            res_max=max(res_max,dfmax[i])
        return res_max

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().maxProduct([-1,-2,-9,-6])
    print(res)
