# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。 
# 
#  
# 
#  示例： 
# 
#  输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定单词的长度不超过500。 
#  给定单词中的字符只含有小写字母。 
#  
#  Related Topics 字符串 动态规划 
#  👍 228 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #dp[i][j]表示word1以i-1结尾、word2以j-1结尾达到相等移除的最小元素数量
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        #初始化第一行，第一列，代表一个空串和另外一个字符串要达到相等只需要删除每一个元素的步数
        for i in range(len(dp)):
            dp[i][0]=i
        for j in range(len(dp[0])):
            dp[0][j]=j
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().minDistance("sea", "eat")
    print(res)
