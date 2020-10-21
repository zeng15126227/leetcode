# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 694 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[grid[0][0]] * n for _ in range(m)]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j - 1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    param = [[1,2,5],[3,2,1]]
    res = Solution().minPathSum(param)
    print(res)
