# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 842 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: list) -> list:
        res=[]
        res.append([])
        tmp=[]
        l = len(nums)


        def dfs(start,tmp):
            for i in range(start,l):
                tmp.append(nums[i])
                res.append(tmp.copy())
                dfs(i+1,tmp)
                tmp.pop()

        dfs(0,tmp)

        return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().subsets([1,2,3])
    print(res)
