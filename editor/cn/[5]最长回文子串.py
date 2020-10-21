# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2611 👎 0


#递归+备忘录
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    dic={}

    def longestPalindrome(self, s):
        if s in self.dic:
            return self.dic[s]
        if self.is_pla(s):
            self.dic[s]=s
            return s
        left=self.longestPalindrome(s[1:])
        right=self.longestPalindrome(s[:-1])
        if len(left)>len(right):
            self.dic[s] = left
            return left
        else:
            self.dic[s] = right
            return right

        # if s == '':
        #     return ''
        # lens = len(s)
        # if lens == 1 or s == s[::-1]:
        #     return s
        # max_len = 1
        # start = 0
        # for i in range(1, lens):
        #     even = s[i - max_len: i + 1]
        #     odd = s[i - max_len - 1: i + 1]
        #     if i - max_len - 1 >= 0 and odd == odd[::-1]:
        #         start = i - max_len - 1
        #         max_len += 2
        #         continue
        #     if i - max_len >= 0 and even == even[::-1]:
        #         start = i - max_len
        #         max_len += 1
        #         continue
        # return s[start:start + max_len]



    def is_pla(self,s):
        return True if s[::-1]==s else False

    # def reverse(self, x: int) -> int:
    #     s = str(x)
    #     sym = "-" if s[0] == "-" else ""
    #     r = s[1:][::-1] if s[0] == "-" else s[::-1]
    #     return int(sym+r) if 2**31-1>=int(sym+r)>=-2**31 else 0



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    res=Solution().longestPalindrome("")
    print(res)




