# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表 
#  👍 421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        res=[]
        from collections import Counter
        p_len=len(p)
        s_len=len(s)
        dict_p=Counter(p)

        p_start=0
        p_end=0
        dict_s={}
        while p_end<s_len:
            cur = p_end
            p_end+=1
            dict_s[s[cur]]=dict_s.get(s[cur],0)+1
            while s[cur] in dict_s and s[cur] not in dict_p:
                dict_s[s[p_start]] -= 1
                if dict_s[s[p_start]] == 0:
                    dict_s.pop(s[p_start])
                p_start += 1

            if s[cur] in dict_s:
                while dict_s[s[cur]] > dict_p[s[cur]]:
                    dict_s[s[p_start]] -= 1
                    if dict_s[s[p_start]] == 0:
                        dict_s.pop(s[p_start])
                    p_start += 1

            if (cur-p_start+1)==p_len:
                res.append(p_start)
        return res

if __name__ == "__main__":
    res=Solution().findAnagrams("cbaebabacd","abc")
    print(res)





        
# leetcode submit region end(Prohibit modification and deletion)
