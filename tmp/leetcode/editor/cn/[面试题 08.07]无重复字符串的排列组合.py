# 无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。 
# 
#  示例1: 
# 
#  
#  输入：S = "qwe"
#  输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
#  
# 
#  示例2: 
# 
#  
#  输入：S = "ab"
#  输出：["ab", "ba"]
#  
# 
#  提示: 
# 
#  
#  字符都是英文字母。 
#  字符串长度在[1, 9]之间。 
#  
#  Related Topics 字符串 回溯 
#  👍 52 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S or S=='' or S==' ':
            return []
        ret = []
        l = []
        for t in S:
            l.append(t)

        def dfs(path:str,res:list):
            if not res:
                ret.append(path)
                return
            for i in res:
                copy = res.copy()
                copy.remove(i)
                dfs(path+i,copy)

        dfs("",l)
        return ret





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().permutation("qwe")
    print(res)
