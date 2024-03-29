# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
#  
# 
#  示例 2: 
# 
#  
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2 * 105 
#  字符串 s 由 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 
#  👍 405 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0
        tail = len(s) - 1

        while (head <= tail):
            while (head <= tail and not s[head].isalnum()):
                head += 1
            while (head <= tail and not s[tail].isalnum()):
                tail -= 1
            if(head<=tail):
                if(s[head].lower()!=s[tail].lower()):
                    return False
                else:
                    head+=1
                    tail-=1
        return True



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().isPalindrome("A man, a plan, a canal: Panama")
    print(res)
