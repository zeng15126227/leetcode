# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1321 👎 0

#回溯即递归

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> list:

        # res=[];
        #
        # def dfs(str,left,right):
        #     if left==0 and right==0:
        #         res.append(str)
        #         return
        #     if left>right:
        #         return
        #     if left>0:
        #         dfs(str+'(',left-1,right)
        #     if right>0:
        #         dfs(str+')',left,right-1)
        #
        #
        # dfs('',n,n)
        #
        # return res

        #df[i] = '('+df[j]+')'+df[i-1-j]

        if n==0:return []

        res=[None for _ in range(n+1)]
        res[0]=[""]

        for i in range(1,n+1):
            cur=[]
            for j in range(i):
                for s1 in res[j]:
                    for s2 in res[i-1-j]:
                        cur.append('('+s1+')'+s2)
            res[i]=cur
        return res[n]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    res = Solution().generateParenthesis(2)
    print(res)