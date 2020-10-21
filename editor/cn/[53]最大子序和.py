# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2483 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: list) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        for n in nums:
            cur_sum = n+cur_sum
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum<0:
                cur_sum=0
        return max_sum

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
