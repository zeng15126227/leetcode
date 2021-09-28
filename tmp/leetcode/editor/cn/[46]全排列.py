# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 
#  👍 1532 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = [0 for _ in nums]
        n = len(nums)

        def backtracking():
            #终止条件
            if len(path)==n:
                res.append(path[:])
                return
            #单层遍历，所有元素
            for i in range(n):
                if used[i]==1:  #去重
                    continue
                #添加元素
                used[i]=1
                path.append(nums[i])
                #递归
                backtracking()
                #回溯
                path.pop()
                used[i]=0

        backtracking()
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().permute([1,2,3])
    print(res)
