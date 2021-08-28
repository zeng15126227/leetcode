# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  例如，给出 n = 3，生成结果为： 
# 
#  
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 85 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(path, left, right):
            if left > n or right > left:
                return
            if left == right == n:
                res.append(path)
                return
            dfs(path + '(', left + 1, right)
            dfs(path + ')', left, right + 1)

        dfs('',0,0)
        return res


if __name__ == '__main__':
    res = Solution().generateParenthesis(3)
    print(res)
