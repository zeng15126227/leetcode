# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。 
# 
#  
# 
#  示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
# 
# 输入：S = "12345"
# 输出：["12345"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 的长度不超过12。 
#  S 仅由数字和字母组成。 
#  
#  Related Topics 位运算 字符串 回溯 
#  👍 298 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = ['']
        for i in s:
            n = len(res)
            if i.isalpha():
                copy = res.copy()
                for j in range(n):
                    res[j]=res[j]+i.lower()
                for j in range(n):
                    res.append(copy[j]+i.upper())
            else:
                for j in range(n):
                    res[j]=res[j]+i

        return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().letterCasePermutation("a1b2")
    print(res)
    # res=['']
    # res[0]=res[0]+'a'
    # res.append(''+'b'.upper())
    # print(res)

