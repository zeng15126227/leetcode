# 给你一个整数数组 A，对于每个整数 A[i]，可以选择 x = -K 或是 x = K （K 总是非负整数），并将 x 加到 A[i] 中。 
# 
#  在此过程之后，得到数组 B。 
# 
#  返回 B 的最大值和 B 的最小值之间可能存在的最小差值。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [1,3,6], K = 3
# 输出：3
# 解释：B = [4,6,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  0 <= K <= 10000 
#  
#  Related Topics 贪心 数组 数学 排序 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = nums[n-1]-nums[0]
        for i in nums:
            t_max = max(nums[i]+k,nums[n-1]-k)
            t_min = min(nums[0]+k,nums[i+1]-k)
            diff = t_max-t_min
            res = min(res,diff)

        return res


# leetcode submit region end(Prohibit modification and deletion)
