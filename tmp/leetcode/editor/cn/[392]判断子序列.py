# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。 
# 
#  进阶： 
# 
#  如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代
# 码？ 
# 
#  致谢： 
# 
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10^4 
#  两个字符串都只由小写字符组成。 
#  
#  Related Topics 双指针 字符串 动态规划 
#  👍 503 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #双指针
        # i = 0
        # j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # if i<len(s):
        #     return False
        # else:return True

        #动态规划
        #dp[i][j]表示s[i-1],t[j-1]最长公共串
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[-1][-1]==len(s)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().isSubsequence("abc","ahbgdc")
    print(res)