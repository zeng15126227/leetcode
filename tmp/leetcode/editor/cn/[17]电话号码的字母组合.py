# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
#  Related Topics 哈希表 字符串 回溯 
#  👍 1476 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # if digits == "": return []
        # dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # res=[]
        # path=""
        # n=len(digits)
        # def backtracking(index):
        #     nonlocal path
        #     #终止条件
        #     if len(path)==n:
        #         res.append(path)
        #         return
        #     for i in dic[digits[index]]:
        #         path+=i
        #         backtracking(index+1)
        #         path=path[:-1]
        #
        # backtracking(0)
        # return res

        if digits == "": return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        queue=[]
        for i in dic[digits[0]]:
            queue.append(i)

        index=1
        start=0
        while index<len(digits):
            tmp = len(queue)
            for x in queue[start:]:
                for y in dic[digits[index]]:
                    queue.append(x+y)
            start = tmp
            index+=1
        return queue[start:]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().letterCombinations("23")
    print(res)
