# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4206 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        remSet=set()
        length = len(s)
        res=0
        left,right=0,0

        for left in range(length):

            if left!=0:
                remSet.remove(s[left-1])


            while (right < length and s[right] not in remSet):
                remSet.add(s[right])
                right += 1

            res = max(res,right-left)



        return res







# leetcode submit region end(Prohibit modification and deletion)



if __name__ == "__main__":
    res=Solution().lengthOfLongestSubstring("pwwkew")
    print(res)

