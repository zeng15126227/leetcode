# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 数组 回溯 
#  👍 790 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = [0 for _ in nums]
        n = len(nums)
        nums.sort()

        def backtracking():
            # 终止条件
            if len(path) == n:
                res.append(path[:])
                return
            # 单层遍历，所有元素
            for i in range(n):
                if used[i] == 1:  # 路径去重
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0: #层去重
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = 0

        backtracking()
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().permuteUnique([1])
    print(res)