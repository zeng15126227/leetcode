# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划 
#  👍 1181 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        # dp = [1] * len(nums)
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)

        #fastDP
        dp = []
        for i in nums:
            if not dp or i>dp[-1]:
                dp.append(i)
            elif i<dp[-1]:
                idx=len(dp)-2
                while idx>=0 and i<=dp[idx]:
                    idx-=1
                dp[idx+1]=i
        return len(dp)


        # fasterDP
        # dp = []
        # for i in nums:
        #     if not dp or i>dp[-1]:
        #         dp.append(i)
        #     else:
        #         l = 0
        #         r = len(dp) - 1
        #         while l < r:
        #             mid = (l + r) >> 1
        #             if dp[mid] < i:
        #                 l = mid + 1
        #             else:
        #                 r = mid
        #         dp[l] = i

        return len(dp)






# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    print(res)
