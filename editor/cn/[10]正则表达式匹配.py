# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 1488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m= len(s)
        n=len(p)
        #判断字符是否匹配
        #i，j表示字符串第i个，和模式串第j个字符
        def match(i,j):
            if(i==0):
                return False
            if(p[j-1]=='.'):
                return True
            else:
                return s[i-1]==p[j-1]

        #初始化状态图
        f=[[False]*(n+1) for _ in range(m+1)]
        #s,p为空串时匹配成功
        f[0][0]=True
        for i in range(m+1):
            for j in range(1,n+1):
                if(p[j-1]=='*'):
                    if(match(i,j-1)):
                        f[i][j]=f[i-1][j]|f[i][j-2]
                    else:
                        f[i][j]=f[i][j-2]
                else:
                    if(match(i,j)):
                        f[i][j] = f[i - 1][j - 1]

        return f[m][n]



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    #res=Solution().isMatch("aaa","ab*a*c*a")
    res = Solution().isMatch("a", "ab*a*")
    print(res)
