# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法 
#  👍 919 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
     def letterCombinations(self, digits: str) -> list:
    #
    #
    #     if digits == '':
    #         return []
    #
    #     dic = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}
    #     index=0
    #
    #     queue = []
    #     for j in dic[digits[0]]:
    #         queue.append(j)
    #
    #     i=1
    #     while i<len(digits):
    #         cnode=dic[digits[i]]
    #         qlens=len(queue)
    #         for k1 in queue[index:]:
    #             for k2 in cnode:
    #                 queue.append(k1+k2)
    #         index = qlens
    #         i+=1
    #
    #     return queue[index:]


        def dfs(cstr, index):
            if index >= l:
                res.append(cstr)
                return
            for i in dic[digits[index]]:
                dfs(cstr + i, index + 1)

        if digits == '':
            return []

        l = len(digits)
        res = []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        dfs("", 0)

        return res





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().letterCombinations("23")
    print(res)
