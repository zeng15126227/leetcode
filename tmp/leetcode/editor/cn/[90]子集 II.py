# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 位运算 数组 回溯 
#  👍 639 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        n = len(nums)
        path = []
        res = [[]]
        nums.sort()

        def dfs(start):
            if start == n:
                return
            for i in range(start, n):
                # 同层去重,前一个相同的元素在同一层
                if nums[i] == nums[i - 1] and i > start:
                    continue
                #添加状态
                path.append(nums[i])
                res.append(path[:])
                dfs(i+1)
                #撤销状态
                path.pop()

        dfs(0)

        return res
if __name__ == '__main__':
    res = Solution().subsetsWithDup([1,2,2])
    print(res)
