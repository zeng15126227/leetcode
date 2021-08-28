# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心 哈希表 双指针 字符串 
#  👍 553 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []

        # 标识片段最左边
        start=0
        # 标识片段最右边
        end=0

        dic = [0]*26
        #保存所有元素最远下标
        for i in range(len(s)):
            dic[ord(s[i]) - ord('a')]=i

        for i in range(len(s)):
            end = max(end,dic[ord(s[i]) - ord('a')])
            if end == i:
                res.append(end-start+1)
                start=i+1
        return res


# leetcode submit region end(Prohibit modification and deletion)
