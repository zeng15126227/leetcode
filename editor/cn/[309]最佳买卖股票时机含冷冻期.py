# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
#  Related Topics 动态规划 
#  👍 613 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0

        n = len(prices)
        #三维数组i表示第i天，列有三种状态：
        # f[i][0]:表示第i天持有股票,包括买入，卖出，持有三种情况
        # f[i][1]:表示第i天没有持有股票且处于冷冻期
        # f[i][2]:表示第i天没有持有股票处于非冷冻期
        dp = [-prices[0], 0, 0]
        #买入盈利记为-，卖出盈利记为+
        for i in range(1,n):
            dp_t=[]
            #第i天持有股票，可以是：1）i-1天已经持有 2）第i天买入
            dp_t.append(max(dp[0],dp[2]-prices[i]))
            #第i天没有持有股票且处于冷冻期，可以是：1）i-1天持有股票并卖出
            dp_t.append(dp[0] + prices[i])
            # 第i天没有持有股票且处于非冷冻期，可以是：1）i-1没有持有股票且处于冷冻期 2）i-1天没有持有股票且处于非冷冻期
            dp_t.append(max(dp[1], dp[2]))
            dp=dp_t
        return max(dp[1],dp[2])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().maxProfit([1,2,3,0,2])
    print(res)
