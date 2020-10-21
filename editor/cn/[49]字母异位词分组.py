# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 479 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def groupAnagrams(self, strs: list):
        ans = {}
        for s in strs:
            key_ele = "".join(sorted(s))
            if key_ele in ans:
                ans[key_ele].append(s)
            else:
                ans[key_ele]=[s]
        return list(ans.values())
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)
