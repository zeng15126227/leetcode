# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 660 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #中心扩展
        # if not s:
        #     return
        #
        # n = len(s)
        # count = 0
        # #2*n-1个回文中心
        # for i in range(2 * n - 1):
        #     # 回文中心左边界
        #     l = i // 2
        #     # 回文中心右边界
        #     r = i // 2 + i % 2
        #     while (0<l and r<n and s[l] == s[r]):
        #         l -= 1
        #         r += 1
        #         count += 1
        # return count

        #动态规划
        #dp[i][j]表示字符串从i到j是不是回文
        dp=[[0]*len(s) for _ in s]
        res=0
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    #a、aa
                    if j-i<2:
                        dp[i][j]=True
                        res+=1
                    #acbca
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
                    else:dp[i][j]=False
                else:
                    dp[i][j] = False

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().countSubstrings("abc")
    print(res)