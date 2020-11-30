class Solution:
    def coinChange(self, coins: list, amount: int) -> int:

        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >=0 and not (dp[i-coin]==amount+1):
                    dp[i]=min(dp[i],dp[i-coin]+1)
        if dp[amount] == amount + 1:
            dp[amount] = -1

        return dp[amount]

if __name__ == "__main__":

    res = Solution().coinChange([1, 2, 5],11)
    print(res)
