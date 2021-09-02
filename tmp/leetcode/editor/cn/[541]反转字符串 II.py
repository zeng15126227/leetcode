# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由小写英文组成 
#  1 <= k <= 104 
#  
#  Related Topics 双指针 字符串 
#  👍 185 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        for i in range(0,n,2*k):
            s[i:i+k]=self._reverse(s[i:i+k])
        return s

    def _reverse(self,s):
        l=0
        r=len(s)-1
        while l<=r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # res = Solution().reverseStr("abcdefg",2)
    # print(res)
    a = "asd"
    a[0]=a[len(a)-1]
    print(a[0])
