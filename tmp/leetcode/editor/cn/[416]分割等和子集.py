# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 929 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        n=len(nums)
        if total%2==1:return False
        target = total//2

        #初始化
        dp = [0]*(target+1)
        for i in range(len(dp)):
            if i>=nums[0]:
                dp[i]=nums[0]

        for i in range(1,len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
            print(dp)


        #物品重量和价值都是nums，所以物品价值和不会超过背包容量，如果背包重量和==物品价值和，则可以找到
        if target==dp[-1]:
            return True
        else:
            return False





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().canPartition([1,2,5])
    print(res)
