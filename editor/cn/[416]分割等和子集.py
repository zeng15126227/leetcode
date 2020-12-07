class Solution:
    def canPartition(self, nums: list) -> bool:
        total = sum(nums)
        if total & 1 == 1:
            return False
        tar = total >> 1
        n = len(nums)
        dp = [0 for _ in range(tar + 1)]
        # 初始化第一个物品
        dp[0] = 1
        if nums[0] <= tar:
            dp[nums[0]] = 1

        for i in range(1, n):
            for j in range(tar,-1,-1):
                if nums[i] <= j:
                    dp[j] = dp[j - nums[i]] or dp[j]

        return dp[-1] == 1

        # total_sum = sum(nums)
        # n = len(nums)
        # if total_sum & 1 == 1:
        #     return False
        # half_sum = total_sum >> 1
        # dp = [0 for _ in range(half_sum + 1)]
        # dp[0] = 1
        # if nums[0] <= half_sum:
        #     dp[nums[0]] = 1
        # for i in range(1, n):
        #     for j in range(half_sum, -1, -1):
        #         if nums[i] <= j:
        #             dp[j] = dp[j] or dp[j - nums[i]]
        # return True if dp[-1] else False


if __name__ == "__main__":
    res = Solution().canPartition([1,2,5])
    print(res)

