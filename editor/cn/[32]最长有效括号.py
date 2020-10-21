# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 981 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=len(s)
        df=[0 for _ in range(l)]

        if l<2:
            return 0

        for i in range(1,l):
            if s[i]==')':
                if s[i-1]=='(':
                    df[i] = df[i-2]+2
                if s[i-1]==')':
                    if s[i-df[i-1]-1]=='(' and i-df[i-1]-1>=0:
                        df[i] = df[i-1]+2+df[i-df[i-1]-2]

        return max(df)

        # l=len(s)
        # max_len=0
        # stack = []
        # #精髓
        # stack.append(-1)
        # for i in range(l):
        #     if s[i]=='(':
        #         stack.append(i)
        #     if s[i]==')':
        #         #精髓
        #         t=stack.pop()
        #         if len(stack)==0:
        #             stack.append(i)
        #         else:
        #             max_len=max(max_len,i-stack[len(stack)-1])
        # return max_len




# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().longestValidParentheses("(()")
    print(res)
