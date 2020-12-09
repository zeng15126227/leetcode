# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。 
# 
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
# 
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
# 
#  示例: 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
#  
#  Related Topics 数组 
#  👍 509 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    #注意下标与数值取值范围相同的问题处理思路
    def findDisappearedNumbers(self, nums: list) -> list:
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result

        
# leetcode submit region end(Prohibit modification and deletion)
