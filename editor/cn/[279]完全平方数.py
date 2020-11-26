# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  示例 1: 
# 
#  输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4. 
# 
#  示例 2: 
# 
#  输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9. 
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
class Solution:
    def numSquares(self, n: int) -> int:
        #DFS
        # memo={}
        #
        # def minNumSquares(k):
        #     """ recursive solution """
        #     # bottom cases: find a square number
        #     if k in memo:
        #         return memo[k]
        #
        #
        #     square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        #     if k in square_nums:
        #         memo[k]=1
        #         return 1
        #     min_num = float('inf')
        #
        #     # Find the minimal value among all possible solutions
        #     for square in square_nums:
        #         if k < square:
        #             break
        #         new_num = minNumSquares(k - square) + 1
        #         min_num = min(min_num, new_num)
        #     memo[k]=min_num
        #     return min_num
        #
        # return minNumSquares(n)

        #动态规划
        # square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        #
        # dp = [float('inf')] * (n + 1)
        # dp[0] = 0
        #
        # for i in range(1, n + 1):
        #     for square in square_nums:
        #         if i < square:
        #             break
        #         dp[i] = min(dp[i], dp[i - square] + 1)
        #
        # return dp[-1]


        #BFS
        # level=0
        # queue = []
        # visited = []
        # queue.append(n)
        # while queue:
        #     level+=1
        #     size = len(queue)
        #     for i in range(size):
        #         cur = queue.pop(0)
        #         j=1
        #         while j*j<=cur:
        #             if cur-j*j==0:
        #                 return level
        #             if cur-j*j not in visited:
        #                 queue.append(cur - j * j)
        #             j+=1




# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().numSquares(12)
    print(res)
