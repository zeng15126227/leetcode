# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。 
# 
#  字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit 
# 
#  示例 2： 
# 
#  
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length, t.length <= 1000 
#  s 和 t 由英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 587 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j]表示t[0:j-1]在s[0:i-1]中出现的次数
        dp = [[0] * (len(t) + 1) for _ in range((len(s) + 1))]
        for i in range(len(dp)):
            dp[i][0]=1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().numDistinct("babgbag","bag")
    print(res)
