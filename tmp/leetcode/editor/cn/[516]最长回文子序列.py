# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。 
# 
#  子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 612 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j]表示以i到j的子串最长回文序列长度
        dp = [[0] * len(s) for _ in s]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    # a、aa
                    if j - i == 0:
                        dp[i][j] = 1
                    elif j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().longestPalindromeSubseq("bbbab")
    print(res)

# [1, 2, 3, 3, 4],
# [0, 1, 2, 2, 3],
# [0, 0, 1, 1, 3],
# [0, 0, 0, 1, 1],
# [0, 0, 0, 0, 1]

# [1, 2, 3, 1, 3],
# [0, 1, 2, 1, 3],
# [0, 0, 1, 1, 3],
# [0, 0, 0, 1, 1],
# [0, 0, 0, 0, 1]
