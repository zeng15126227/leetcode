# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。 
# 
#  说明： 
# 
#  
#  所有数字都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: k = 3, n = 7
# 输出: [[1,2,4]]
#  
# 
#  示例 2: 
# 
#  输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#  
#  Related Topics 数组 回溯 
#  👍 345 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        path=[]
        def backtracking(start_idx,target):
            if len(path)==k:
                if target==0:
                    res.append(path[:])
                return
            for i in range(start_idx,9 - (k - len(path)) + 2):
                if i>target:return
                path.append(i)  # 处理
                backtracking(i + 1,target-i)  # 递归
                path.pop()  # 回溯

        backtracking(1,n)
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().combinationSum3(3,9)
    print(res)
