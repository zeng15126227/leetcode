# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#  Related Topics 字符串 动态规划 
#  👍 1191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if n * m == 0:
            return n + m


        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,n+1):
            dp[0][i]=i
        for j in range(1,m+1):
            dp[j][0]=j
        for i in range(1,m+1):
            for j in range(1, n + 1):
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+int(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
        # visited = set()
        # queue = collections.deque([(word1, word2, 0)])
        #
        # while True:
        #     w1, w2, d = queue.popleft()
        #     if (w1, w2) not in visited:
        #         if w1 == w2:
        #             return d
        #         visited.add((w1, w2))
        #         while w1 and w2 and w1[0] == w2[0]:
        #             w1 = w1[1:]
        #             w2 = w2[1:]
        #         d += 1
        #         queue.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().minDistance("int","exe")
    print(res)
