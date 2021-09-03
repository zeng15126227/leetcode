# 给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。 
# 
#  有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 
# 和 "192.168@1.1" 是 无效 IP 地址。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "1111"
# 输出：["1.1.1.1"]
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3000 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯 
#  👍 664 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        param:list = s
        n = len(param)
        path=[]

        def is_valid(s):
            if len(s) > 1 and s[0] == "0":
                return False
            if 0 <= int(s) <= 255:
                return True
            return False

        def backTrack(start_idx):
            if len(path)==4:
                res.append(".".join(path))
            for end in range(start_idx+1,n+1):
               #剪枝
               if n-end > 3*(4-len(path)-1):
                   continue
               seg = param[start_idx:end]
               if is_valid(seg):
                   path.append(seg)
                   backTrack(end)
                   path.pop()

        #剪枝
        if len(s) > 3 * 4:
            return []

        backTrack(0)

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().restoreIpAddresses("25525511135")
    print(res)
