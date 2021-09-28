# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 822 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path=[]
        res=[]
        n=len(s)

        def is_palindrome(s):
            l=0
            r=len(s)-1
            while l<=r and r<len(s):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtracking(start_idx):
            #遍历完所有元素说明找到可行解
            if start_idx == n:
                res.append(path[:])
                return
            for i in range(start_idx,n):
                if is_palindrome(s[start_idx:i+1]):
                    path.append(s[start_idx:i+1]) #添加元素
                    backtracking(i + 1) #递归
                    path.pop() #回溯


        backtracking(0)

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':

    res = Solution().partition("aab")
    print(res)